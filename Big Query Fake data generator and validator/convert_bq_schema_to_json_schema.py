import json

def bq_type_to_json_type(bq_type):
    mapping = {
        "STRING": {"type": "string"},
        "INTEGER": {"type": "integer"},
        "FLOAT": {"type": "number"},
        "BOOLEAN": {"type": "boolean"},
        "TIMESTAMP": {"type": "string", "format": "date-time"},
        "RECORD": {"type": "object"},
    }
    return mapping.get(bq_type, {"type": "string"})

def convert_bq_schema_to_json_schema(bq_fields):
    properties = {}
    required = []

    for field in bq_fields:
        name = field["name"]
        bq_type = field["type"]
        mode = field.get("mode", "NULLABLE")

        json_type = bq_type_to_json_type(bq_type)

        if bq_type == "RECORD":
            nested_fields = convert_bq_schema_to_json_schema(field.get("fields", []))
            json_type["properties"] = nested_fields["properties"]
            if nested_fields.get("required"):
                json_type["required"] = nested_fields["required"]

        if mode == "REPEATED":
            json_type = {
                "type": "array",
                "items": json_type
            }
        elif mode == "REQUIRED":
            required.append(name)

        properties[name] = json_type

    # Ensure "required" is always an array
    return {
        "type": "object",
        "properties": properties,
        "required": required if required else []  # Change None to an empty array
    }


# Load the BigQuery schema (assumes it's in a file)
with open("bq_billing_schema.json", "r") as f:
    bq_schema = json.load(f)

json_schema = convert_bq_schema_to_json_schema(bq_schema)

# Save it
with open("converted_bq_billing_json_schema.json", "w") as f:
    json.dump(json_schema, f, indent=2)

print("✅ Converted schema saved to billing_json_schema.json")
