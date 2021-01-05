import jsonschema

zendesk_schema = {
    "type": "object",
    "properties": {
        "name": {"type": "string"},
        "destination": {
            "type": "object",
            "properties": {
                "type": {"type": "string"},
                "url": {"type": "string"},
                "auth": {
                    "type": "object",
                    "properties": {
                        "type": {"type": "string"},
                        "config": {
                            "type": "object",
                            "properties": {
                                "user": {"type": "string"},
                                "password": {"type": "string"},
                            }
                        }
                    }
                },
            }
        },
        "template": {
            "type": "object",
            "properties": {
                "name": {"type": "string"},
                "path": {"type": "string"},
            }
        }
    },
    "required": []
}


def validate(config_: dict):
    jsonschema.validate(config_, zendesk_schema)
