import json
import random

from tqdm import tqdm

# Load value pools
with open("value_pools.json", "r") as f:
    pools = json.load(f)

def sample_from(key):
    values = pools.get(key)
    if values:
        return random.choice(values)
    return None  # No default fallback

def generate_credits():
    credit_fields = ["name", "amount", "full_name", "id", "type"]
    credit_entry = {}

    for field in credit_fields:
        key = f"credits[1].{field}"
        values = pools.get(key)
        if values:
            credit_entry[field] = random.choice(values)

    return [credit_entry] if credit_entry else []

def generate_project_labels():
    keys = pools.get("project.labels[0].key")
    values = pools.get("project.labels[0].value")

    if keys and values:
        # Allow mismatch in length by pairing random key with random value
        return [{"key": random.choice(keys), "value": random.choice(values)}]
    return []

def generate_project_ancestors():
    ancestors = []

    for i in range(3):  # for [0, 1, 2]
        resource_key = f"project.ancestors[{i}].resource_name"
        display_key = f"project.ancestors[{i}].display_name"

        resource_names = pools.get(resource_key)
        display_names = pools.get(display_key)

        if resource_names and display_names:
            ancestor = {
                "resource_name": random.choice(resource_names),
                "display_name": random.choice(display_names)
            }
            ancestors.append(ancestor)

    return ancestors

def generate_labels():
    keys = pools.get("labels[0].key")
    values = pools.get("labels[0].value")

    if not keys or not values:
        return []

    return [
        {
            "key": random.choice(keys),
            "value": random.choice(values)
        }
        for _ in range(random.randint(1, 3))
    ]

def generate_system_labels():
    keys = pools.get("system_labels[0].key")
    values = pools.get("system_labels[0].value")

    if not keys or not values:
        return []

    return [
        {
            "key": random.choice(keys),
            "value": random.choice(values)
        }
        for _ in range(random.randint(1, 2))
    ]


def generate_from_pools():

    return {
        "billing_account_id": sample_from("billing_account_id"),
        "service": {
            "id": sample_from("service.id"),
            "description": sample_from("service.description")
        },
        "sku": {
            "id": sample_from("sku.id"),
            "description": sample_from("sku.description")
        },
        "usage_start_time": sample_from("usage_start_time"),
        "usage_end_time": sample_from("usage_end_time"),
        "project": {
            "id": sample_from("project.id"),
            "number": sample_from("project.number"),
            "name": sample_from("project.name"),
            "labels": generate_project_labels(),
            "ancestry_numbers": sample_from("project.ancestry_numbers"),
            "ancestors": generate_project_ancestors()
        },
        "labels":generate_labels(),
        "system_labels": generate_system_labels(),
        "location": {
            "location": sample_from("location.location"),
            "country": sample_from("location.country"),
            "region": sample_from("location.region")
        },
        "tags": [],
        "transaction_type": sample_from("transaction_type"),
        "seller_name": sample_from("seller_name"),
        "export_time": sample_from("export_time"),
        "cost": sample_from("cost"),
        "currency": sample_from("currency"),
        "currency_conversion_rate": 1,
        "usage": {
            "amount": sample_from("usage.amount"),
            "unit": sample_from("usage.unit"),
            "amount_in_pricing_units": sample_from("usage.amount_in_pricing_units"),
            "pricing_unit": sample_from("usage.pricing_unit")
        },
        "credits": generate_credits(),
        "invoice": {
            "month": sample_from("invoice.month"),
            "publisher_type": sample_from("invoice.publisher_type")
        },
        "cost_type": sample_from("cost_type"),
        "adjustment_info": {},
        "cost_at_list": sample_from("cost_at_list")
    }

# Write each record as plain JSON object per line
output_file = "streamed_json_records.json"
with open(output_file, "w", encoding="utf-8") as f:
    for _ in tqdm(range(10), desc="Writing JSON records"):
        obj = generate_from_pools()
        f.write(json.dumps(obj) + "\n")
