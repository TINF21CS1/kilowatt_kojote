import base64
import jsonschema
import logging
import requests
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.serialization import pkcs12
from .db import db_manager
# Für falsche Dinge value error throwen mit nachricht was es ist
MAX_SUPPLIER_NAME_LEN = 500
MIN_SUPPLIER_NAME_LEN = 2
MAX_SUPPLIER_NOTES_LEN = 5000

CA_DOMAIN_NAME = "http://ca.kilowattkojote.de/api"
CERTIFICATE_PASSPHRASE = b"kilowattkojote"
logger = logging.getLogger('waitress')

frontend_supplier_add_schema = {
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the supplier",
            "type": "string",
            "minLength": MIN_SUPPLIER_NAME_LEN,
            "maxLength": MAX_SUPPLIER_NAME_LEN
        },
        "notes": {
            "description": "Additional notes regarding the supplier",
            "type": "string",
            "maxLength": MAX_SUPPLIER_NOTES_LEN
        }
    },
    "required": ["name", "notes"]
}

frontend_supplier_assign_schema = {
    "type": "object",
    "properties": {
        "uuid": {
            "type": "string",
            "minLength": 1,
        },
        "smartmeter": {
            "description": "The serial number of the smartmeter that should be added to the supplier",
            "type": "string",
            "minLength": 1
        }
    },
    "required": ["uuid", "smartmeter"]

}

uuid_schema = {
    "type": "string",
    "minLength": 1,
}

def frontend_smartmeter() -> list:

    all_readers_raw = db_manager.frontend_smartmeter()
    keys = ["uuid", "type", "latitude", "longitude", "supplier"]

    all_readers = [dict(zip(keys, reader)) for reader in all_readers_raw]

    keys = ["timestamp", "actual_timestamp", "reading"]

    for reader in all_readers:
        # query all readings of that reader and append everything to the output list together with the other data just like defined

        raw_data = db_manager.frontend_smartmeter_getAllMeterData(reader["uuid"])

        reader["data"] = [dict(zip(keys, row)) for row in raw_data]

    return all_readers


def frontend_smartmeter_reading(uuid: str) -> list:
    
    try:
        jsonschema.validate(uuid, uuid_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"UUID Validation from Frontend failed:\n{e}")
        raise JSONValidationError("UUID has an invalid format")

    raw_output = db_manager.frontend_smartmeter_getAllMeterData(uuid)
    keys = ["timestamp", "actual_timestamp", "reading"]

    return [dict(zip(keys, row)) for row in raw_output]
    

def frontend_smartmeter_revoke(uuid: str):

    try:
        jsonschema.validate(uuid, uuid_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"UUID Validation from Frontend failed:\n{e}")
        raise JSONValidationError("UUID has an invalid format")

    logger.info(f"Revoked the certificate of smartmeter with serial number {uuid}")
    # Here we need to contact endpoint of CA
    response = requests.get(CA_DOMAIN_NAME + "/revoke?serial=" + uuid)


def frontend_smartmeter_supplier(uuid: str) -> dict:
    
    try:
        jsonschema.validate(uuid, uuid_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"UUID Validation from Frontend failed:\n{e}")
        raise JSONValidationError("UUID has an invalid format")
    
    raw_data = db_manager.frontend_smartmeter_supplier(uuid)
    keys = ["supplier"]

    return dict(zip(keys, raw_data))

def frontend_supplier() -> list:
    
    raw_data = db_manager.frontend_supplier()
    keys = ["uuid", "supplier", "notes"]

    return [dict(zip(keys, row)) for row in raw_data]


def frontend_supplier_smartmeter(uuid: str) -> list:

    try:
        jsonschema.validate(uuid, uuid_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"UUID Validation from Frontend failed:\n{e}")
        raise JSONValidationError("UUID has an invalid format")
    
    raw_data = db_manager.frontend_supplier_smartmeter(uuid)
    keys = ["uuid", "type", "latitude", "longitude"]

    return [dict(zip(keys, row)) for row in raw_data]

def frontend_supplier_add(json: dict) -> dict:

    try:
        jsonschema.validate(json, frontend_supplier_add_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"Validation of adding a supplier from frontend failed:\n{e}")
        raise JSONValidationError("Validation of data failed")

    # Here we also need to contact the CA to get the certificate returned
    response = requests.get(CA_DOMAIN_NAME + "/create?name=" + json["name"])
    certificate_b64 = response.content

    certificate_decoded = base64.b64decode(certificate_b64)

    private_key, certificate, additional_certs = pkcs12.load_key_and_certificates(certificate_decoded, CERTIFICATE_PASSPHRASE, default_backend)
    supplier_serial = str(certificate.serial_number)
    logger.info(f"Created a supplier '{json["name"]}' and the corresponding certificate with serial number {supplier_serial}")

    db_manager.frontend_supplier_add(supplier_serial, json["name"], json["notes"])

    return {"certificate": certificate_b64}

def frontend_supplier_assign(json: dict):
    
    try:
        jsonschema.validate(json, frontend_supplier_assign_schema)
    except jsonschema.ValidationError as e:
        logger.info(f"Validation of assigning a supplier from frontend failed:\n{e}")
        raise JSONValidationError("Validation of data failed")
    
    db_manager.frontend_supplier_assign(json["uuid"], json["smartmeter"])


class JSONValidationError(Exception):
    # Error to be thrown when JSON Schema validation fails
    def __init__(self, message) -> None:
        self.message = message
        super().__init__(self.message)