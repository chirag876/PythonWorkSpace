import json
import csv
from jsonschema import validate, ValidationError
import pymongo


def validate_json(schema_collection, json_file, schema_key):
  """
  Validates a JSON document against a schema stored in MongoDB and attempts to fix data type mismatches.

  Args:
      schema_collection (str): Name of the MongoDB collection containing the schema document.
      json_file (str): Path to the JSON file to be validated.
      schema_key (str): Key within the schema document that holds the actual schema definition.

  Returns:
      dict: The modified JSON document (may contain attempted data type conversions), or None if errors occur.
  """

  # Connect to MongoDB
  client = pymongo.MongoClient("mongodb://root:wIntEr%40!%23%24@125.20.10.50:27017/")  # Replace with your connection details
  db = client["datapulse0"]
  collection = db[schema_collection]

  # Load JSON Document
  with open(json_file, 'r') as f:
    json_data = json.load(f)

  # Fetch Schema from MongoDB
  schema_document = collection.find_one()
  if not schema_document:
    print("Error: Schema not found in collection", schema_collection)
    return None
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

  modified_data = json_data.copy()  # Create a copy to avoid modifying original
  errors = []
  for prop, prop_schema in schema["properties"]["Page_1"]["properties"].items():
    if prop in modified_data["output"][0][schema_key]["Page_1"]:
      expected_type = prop_schema.get("type")
      if expected_type:
        expected_type = type_mapping.get(expected_type)
        actual_value = modified_data["output"][0][schema_key]["Page_1"][prop]
        if not isinstance(actual_value, expected_type):
          try:
            # Attempt to convert the value to the expected type
            modified_data["output"][0][schema_key]["Page_1"][prop] = expected_type(actual_value)
          except (ValueError, TypeError):
            errors.append(f"Data type mismatch for property '{prop}'. Expected type '{expected_type}', but found '{type(actual_value)}'. Conversion failed.")
      else:
        errors.append(f"Property '{prop}' has no type definition in the schema.")
    else:
      errors.append(f"Property '{prop}' is missing in the JSON document.")

  # Write errors to CSV file (optional, not included here)

  if errors:
    print("Validation failed. Errors:")
    for err in errors:
      print(err)
    return None  # Return None on errors
  else:
    print("JSON document is valid according to the schema.")

  return modified_data  # Return the modified JSON document


# Example usage
schema_collection = 'acord_form'
schema_key = "ACORD125(2016/03)"
json_file = 'C:/Workspaces/CodeSpaces/Python_Work/PyDataScanner/pydatascanner/AcordJsonSchema/ACORD125output.json'
modified_json = validate_json(schema_collection, json_file, schema_key)

# Use the modified_json for further processing
if modified_json:
  print(modified_json)
else:
  print("Validation failed. Processing aborted.")
