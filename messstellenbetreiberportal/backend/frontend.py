import jsonschema

frontend_supplier_add_schema = {
    "type": "object",
    "properties": {
        "name": {
            "description": "Name of the supplier",
            "type": "string",
            "minLength": 2,
            "maxLength": 500    # Completely arbitrary, just to make sure that it's not too large for the TEXT Type in the DB
        },
        "notes": {
            "description": "Additional notes regarding the supplier",
            "type": "string",
            "maxLength": 5000   # Again, completely arbitrary
        }
    },
    "required": ["name", "notes"]
}

def frontend_smartmeter() -> list(dict):
    return

def frontend_smartmeter_reading() -> list(dict):
    return

def frontend_smartmeter_usage() -> list(dict):
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
