import json
from collections import defaultdict

# Open the NDJSON file and parse each line as an individual JSON object
data = []
with open(r"dummy.json path", "r") as f:
    for line in f:
        if line.strip():  # skip empty lines
            data.append(json.loads(line))

# In case it's just one object, wrap it
if isinstance(data, dict):
    data = [data]

# Flatten JSON function (same as before)
def flatten_json(y, prefix=''):
    out = {}
    for key, val in y.items():
        new_key = f"{prefix}.{key}" if prefix else key
        if isinstance(val, dict):
            out.update(flatten_json(val, new_key))
        elif isinstance(val, list) and all(isinstance(v, dict) for v in val):
            for idx, item in enumerate(val):
                out.update(flatten_json(item, f"{new_key}[{idx}]"))
        else:
            out[new_key] = val
    return out

# Extract unique values
unique_values = defaultdict(set)

for item in data:
    flat = flatten_json(item)
    for k, v in flat.items():
        unique_values[k].add(json.dumps(v))

# Convert back from JSON strings to normal Python objects
unique_values_cleaned = {k: [json.loads(x) for x in v] for k, v in unique_values.items()}

# Save to file
with open("value_pools.json", "w") as f:
    json.dump(unique_values_cleaned, f, indent=2)

print("✅ Unique value pools saved to value_pools.json")
