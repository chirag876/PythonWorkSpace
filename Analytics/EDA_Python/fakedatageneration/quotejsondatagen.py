import os
import json
from faker import Faker
from faker.providers import phone_number, company
from datetime import date, datetime

fake = Faker()
fake.add_provider(phone_number)
fake.add_provider(company)

from decimal import Decimal

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, (date, datetime)):
        return obj.isoformat() + "Z"
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def generate_fake_data():
    return {
        # "_id": {
        #     "$oid": fake.uuid4()
        # },
        "CreatedBy": fake.name(),
        "CreatedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "UpdatedBy": fake.name(),
        "UpdatedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "UpdateReason": fake.text(),
        "OwnerId": fake.uuid4(),
        "IsActive": fake.boolean(),
        "IsDeleted": fake.boolean(),
        "IsApproved": fake.boolean(),
        "ApproverId": fake.uuid4(),
        "ApprovedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "IsAuthorized": fake.boolean(),
        "AuthorizedById": fake.uuid4(),
        "AuthorizedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "SysData": fake.text(),
        "TenantId": fake.uuid4(),
        "SubTenantId": fake.uuid4(),
        "QuoteId": fake.uuid4(),
        "insured": {
            "Address": {
                "City": fake.city(),
                "CountryCode": fake.country_code(),
                "CountryName": fake.country(),
                "Line1": fake.street_address(),
                "PostalCode": fake.zipcode(),
                "StateOrProvinceCode": fake.state_abbr(),
                "StateOrProvinceName": fake.state(),
                "detailAddress": {
                    "PreDirectionCode": fake.random_letter(),
                    "PostDirectionCode": fake.random_letter(),
                    "StreetName": fake.street_name(),
                    "StreetNumber": fake.building_number(),
                    "StreetTypeCode": fake.random_letter()
                }
            },
            "Business": {
                "AnnualSales": str(fake.random_int(min=100000, max=999999)),
                "BusinessName": fake.company(),
                "_id": str(fake.random_int(min=100000, max=999999)),
                "NAICS": str(fake.random_int(min=100000, max=999999)),
                "NumberOfEmployeeTotal": fake.random_int(min=1, max=5000),
                "SIC": str(fake.random_int(min=100000, max=999999))
            },
            "Contact": {
                "Communication": [
                    {
                        "PhoneTypeCode": fake.random_letter(),
                        "PhoneNumber": fake.phone_number(),
                        "WebsiteURL": fake.url()
                    }
                ],
                "FullName": fake.name()
            }
        },
        "location": {
            "City": fake.city(),
            "CountryCode": fake.country_code(),
            "EndDate": fake.date_between(start_date="today", end_date="+5y").strftime("%d/%m/%Y"),
            "Line1": fake.street_address(),
            "PostalCode": fake.zipcode(),
            "StateOrProvinceCode": fake.state_abbr(),
            "StartDate": fake.date_this_decade().strftime("%d/%m/%Y")
        },
        "premium": {
            "Amount": str(fake.random_int(min=1000, max=10000)),
            "CurrencyCode": fake.random_letter(),
            "period": {
                "EndDate": fake.date_between(start_date="today", end_date="+1y").strftime("%d/%m/%Y"),
                "StartDate": fake.date_this_decade().strftime("%d/%m/%Y")
            }
        },
        "quoteId": fake.uuid4()
    }

def save_generated_json(output_folder="generated_quote_json"):
    os.makedirs(output_folder, exist_ok=True)

    for idx, fake_data in enumerate([generate_fake_data() for _ in range(10000)], start=1):
        output_file_path = os.path.join(output_folder, f"quotejsondata_{idx}.json")
        with open(output_file_path, 'w') as output_file:
            json.dump(fake_data, output_file, indent=4, default=decimal_default)

        print(f"Fake Data {idx} saved to: {output_file_path}")

if __name__ == "__main__":
    save_generated_json()
