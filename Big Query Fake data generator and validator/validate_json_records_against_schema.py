import json

from jsonschema import ValidationError, validate

# Load schema
with open("billing_json_schema.json", "r") as schema_file:
    schema = json.load(schema_file)

# Load generated data
with open("streamed_json_records.json", "r") as data_file:
    lines = data_file.readlines()

errors = []

# Validate each record
for idx, line in enumerate(lines):
    try:
        record = json.loads(line)
        validate(instance=record, schema=schema)
    except ValidationError as e:
        errors.append((idx + 1, str(e)))

# Show results
if not errors:
    print("✅ All records are valid.")
else:
    print(f"❌ Found {len(errors)} invalid record(s):")
    for line_num, error in errors:
        print(f"\nRecord {line_num}:\n{error}")
