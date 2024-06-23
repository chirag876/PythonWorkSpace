import json
import csv
from jsonschema import validate, ValidationError

def validate_json(schema_file, json_file):
    # Load JSON Schema
    with open(schema_file, 'r') as f:
        schema = json.load(f)
    
    # Load JSON Document
    with open(json_file, 'r') as f:
        json_data = json.load(f)
    
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
        if prop in json_data["output"][0]["ACORD125(2016/03)"]["Page_1"]:
            expected_type = prop_schema.get("type")
            if expected_type:
                expected_type = type_mapping.get(expected_type)
                actual_value = json_data["output"][0]["ACORD125(2016/03)"]["Page_1"][prop]
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


schema_file = 'C:/Workspaces/CodeSpaces/Python_Work/PyDataScanner/pydatascanner/AcordJsonSchema/acord125_V2016_03.json'
json_file = 'C:/Workspaces/CodeSpaces/Python_Work/PyDataScanner/pydatascanner/AcordJsonSchema/ACORD125output.json'
validate_json(schema_file, json_file)
