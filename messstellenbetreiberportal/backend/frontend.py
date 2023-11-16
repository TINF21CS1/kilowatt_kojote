import jsonschema
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
            "maxLength": MAX_SUPPLIER_NAME_LEN    # Completely arbitrary, just to make sure that it's not too large for the TEXT Type in the DB
        },
        "notes": {
            "description": "Additional notes regarding the supplier",
            "type": "string",
            "maxLength": MAX_SUPPLIER_NOTES_LEN   # Again, completely arbitrary
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
    return

def frontend_smartmeter_reading() -> list(dict):
    return

def frontend_smartmeter_revoke(uuid: str):
    return

def frontend_smartmeter_supplier() -> dict:
    return

def frontend_supplier() -> list(dict):
    return

def frontend_supplier_smartmeter() -> list(dict):
    return

def frontend_supplier_add(json: dict) -> dict:
    return

def frontend_supplier_assign(json: dict):
    return
