import jsonschema
from .db import db_manager
# Für falsche Dinge value error throwen mit nachricht was es ist
MAX_SUPPLIER_NAME_LEN = 500
MIN_SUPPLIER_NAME_LEN = 2
MAX_SUPPLIER_NOTES_LEN = 5000

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
        "supplier": {
            "description": "Name of the supplier to which the smartmeter should be added",
            "type": "string",
            "minLength": MIN_SUPPLIER_NAME_LEN,
            "maxLength": MAX_SUPPLIER_NAME_LEN
        },
        "smartmeter": {
            "description": "The serial number of the smartmeter that should be added to the supplier",
            "type": "string"
        }
    },
    "required": ["supplier", "smartmeter"]

}

def frontend_smartmeter() -> list(dict):
    
    output = []

    all_readers_raw = db_manager.frontend_smartmeter()
    keys = ["uuid", "type", "latitude", "longitude", "supplier"]

    all_readers = [dict(zip(keys, reader)) for reader in all_readers_raw]

    keys = ["timestamp", "actual_timestamp", "reading"]

    for reader in all_readers:
        # query all readings of that reader and append everything to the output list together with the other data just like defined

        raw_data = db_manager.frontend_smartmeter_getAllMeterData(reader["uuid"])

        reader["data"] = [dict(zip(keys, row)) for row in raw_data]

    return all_readers


def frontend_smartmeter_reading() -> list(dict):
    return

def frontend_smartmeter_revoke(uuid: str):
    # Here we need to contact endpoint of CA
    return

def frontend_smartmeter_supplier() -> dict:
    return

def frontend_supplier() -> list(dict):
    return

def frontend_supplier_smartmeter() -> list(dict):
    return

def frontend_supplier_add(json: dict) -> dict:
    # Here we also need to contact the CA
    return

def frontend_supplier_assign(json: dict):
    return
