import json
import csv
from jsonschema import validate, ValidationError
import pymongo

def validate_json(schema_collection, json_file, schema_key):
    # Connect to MongoDB
    client = pymongo.MongoClient("mongodb://root:wIntEr%40!%23%24@125.20.10.50:27017/")
    db = client["datapulse0"]
    collection = db[schema_collection]

    # Load JSON Document
    with open(json_file, 'r') as f:
        json_data = json.load(f)

    # Fetch Schema from MongoDB
    schema_document = collection.find_one()
    schema = json.loads(schema_document["StaiJsonSchemaV1"])

    # Mapping of type strings to Python types
    type_mapping = {
        "string": str,
        "integer": int,
        "number": (int, float),
        "boolean": bool,
        "array": list,
        "object": dict
    }
    
    # Validate JSON Document against Schema
    errors = []
    for prop, prop_schema in schema["properties"]["Page_1"]["properties"].items():
        if prop in json_data["output"][0][schema_key]["Page_1"]:
            expected_type = prop_schema.get("type")
            if expected_type:
                expected_type = type_mapping.get(expected_type)
                actual_value = json_data["output"][0][schema_key]["Page_1"][prop]
                if not isinstance(actual_value, expected_type):
                    errors.append(f"Data type mismatch for property '{prop}'. Expected type '{expected_type}', but found '{type(actual_value)}'.")
        else:
            errors.append(f"Property '{prop}' is missing in the JSON document.")

    # Write errors to CSV file
    if errors:
        csv_file = json_file.replace('.json', '_validation_errors.csv')
        with open(csv_file, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Error'])
            for err in errors:
                writer.writerow([err])
        print(f"Validation failed. Errors appended to '{csv_file}'")
    else:
        print("JSON document is valid according to the schema.")

    if errors:
        txt_file = json_file.replace('.json', '_validation_errors.txt')
        with open(txt_file, 'w') as txtfile:
            for err in errors:
                txtfile.write(err + '/n')
        print(f"Validation failed. Errors appended to '{txt_file}'")
    else:
        print("JSON document is valid according to the schema.")
        
schema_key = "ACORD125(2016/03)"
schema_collection = 'acord_form'
json_file = 'C:/Workspaces/CodeSpaces/Python_Work/PyDataScanner/pydatascanner/AcordJsonSchema/ACORD125output.json'
validate_json(schema_collection, json_file, schema_key)
