import json
from faker import Faker
from decimal import Decimal
import os
from datetime import date, datetime

fake = Faker()

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, (date, datetime)):
        return obj.isoformat() + "Z"
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

def generate_fake_data():
    fake_data = {
        # "_id": {"$oid": fake.uuid4()},
        "CorrelationId": fake.uuid4(),
        "AuditableRequestId": fake.uuid4(),
        "AuditableRequestName": fake.word(),
        "AuditableSourceEventName": fake.word(),
        "CreatedBy": fake.name(),
        "CreatedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "UpdatedBy": fake.name(),
        "UpdatedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "UpdateReason": fake.sentence(),
        "OwnerId": fake.uuid4(),
        "IsActive": fake.boolean(),
        "IsDeleted": fake.boolean(),
        "IsApproved": fake.boolean(),
        "ApproverId": fake.uuid4(),
        "ApprovedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "IsAuthorized": fake.boolean(),
        "AuthorizedById": fake.uuid4(),
        "AuthorizedDateTime": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "SysData": fake.word(),
        "TenantId": fake.uuid4(),
        "SubTenantId": fake.uuid4(),
        "QuoteId": fake.uuid4(),
        "CancellationDate": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "CancelReasonDescription": fake.sentence(),
        "ControllingStateOrProvinceCode": fake.word(),
        "EffectiveDate": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "ExpirationDate": {"$date": fake.date_time_between_dates().isoformat() + "Z"},
        "PolicyId": fake.uuid4(),
        "LineOfBusinessCode": fake.word(),
        "Number": "POL" + str(fake.random_int(min=100000000, max=999999999)),
        "OriginalEffectiveDate": {"$date": {"$numberLong": "-62135596800000"}},
        "ParentEntityId": fake.uuid4(),
        "ParentEntityTypeName": fake.word(),
        "StatusCode": fake.word(),
        "TotalPremium": fake.pyfloat(),
        "AgentCode": fake.random_int(min=0, max=999),
        "AccountingDate": {"$date": {"$numberLong": "-62135596800000"}},
        "ReferalCode": fake.random_int(min=0, max=999),
        "RenewalStatus": fake.word(),
        "TransactionType": fake.word(),
        "address": [generate_fake_address()],
        "exposure": [generate_fake_exposure()],
        "insured": [generate_fake_insured()],
        "producer": generate_fake_producer(),
        "reference": [generate_fake_reference()],
        "underwriter": generate_fake_underwriter(),
        "claim": generate_fake_claim()
    }

    return fake_data

def generate_fake_address():
    return {
        "City": fake.city(),
        "CountryCode": fake.country_code(),
        "CountryName": fake.country(),
        "Line1": fake.street_address(),
        "Line2": fake.secondary_address(),
        "PostalCode": fake.zipcode(),
        "StateOrProvinceCode": fake.state_abbr(),
        "StateOrProvinceName": fake.state(),
        "DetailAddress": {
            "PostDirectionCode": fake.word(),
            "PreDirectionCode": fake.word(),
            "StreetName": fake.street_name(),
            "StreetNumber": fake.building_number(),
            "StreetTypeCode": fake.word(),
            "UnitNumber": fake.random_int(min=1, max=100)
        },
        "Reference": fake.word()
    }

def generate_fake_exposure():
    return {
        "_id": fake.uuid4(),
        "coverageName": fake.word(),
        "perils": [
            {
                "exposureid": fake.uuid4(),
                "name": fake.word(),
                "renewalGroup": fake.word(),
                "characteristics": [
                    {
                        "_id": fake.uuid4(),
                        "exposureCharacteristicsid": fake.uuid4(),
                        "perilid": fake.uuid4(),
                        "indemnityPerItem": f"${fake.random_int(min=1, max=999)},000",
                        "indemnityPerEvent": f"${fake.random_int(min=1, max=999)},000",
                        "indemnityInAggregate": f"${fake.random_int(min=1, max=999)},000",
                        "lumpSumPayment": f"${fake.random_int(min=1, max=999)},000",
                        "deductible": f"${fake.random_int(min=1, max=999)},000"
                    }
                ],
                "policyholderid": fake.uuid4(),
                "productid": fake.uuid4(),
                "policyid": fake.uuid4(),
                "createdTimestamp": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
                "updatedTimestamp": {"$date": fake.date_time_this_decade().isoformat() + "Z"}
            }
        ]
    }

def generate_fake_insured():
    return {
        "InsuredId": fake.random_int(min=1, max=999),
        "ParentEntityId": fake.uuid4(),
        "ParentEntityTypeName": fake.word(),
        "TypeCode": fake.word(),
        "BirthDate": fake.date_of_birth(),
        "FullName": fake.company(),
        "GivenName": fake.first_name(),
        "Surname": fake.last_name(),
        "Address": generate_fake_address(),
        "CountryCode": fake.country_code()
    }

def generate_fake_producer():
    return {
        "Branch": fake.word(),
        "_id": fake.uuid4(),
        "Number": fake.uuid4(),
        "ParentEntityId": fake.uuid4(),
        "ParentEntityTypeName": fake.word(),
        "FullName": fake.company(),
        "GivenName": fake.first_name(),
        "Surname": fake.last_name()
    }

def generate_fake_reference():
    return {
        "AppliesTo": fake.word(),
        "Description": fake.sentence(),
        "_id": fake.uuid4(),
        "Name": fake.word()
    }

def generate_fake_underwriter():
    return {
        "_id": fake.uuid4(),
        "ParentEntityId": fake.uuid4(),
        "ParentEntityTypeName": fake.word(),
        "FullName": fake.name(),
        "GivenName": fake.first_name(),
        "Surname": fake.last_name()
    }

def generate_fake_claim():
    return {
        "ClaimId": fake.random_int(min=1, max=999),
        "ClaimNo": fake.random_int(min=1, max=999),
        "AccidentDate": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "ReportedDate": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "RegisterDate": fake.date_time_this_decade().isoformat() + "Z",
        "AccidentZipCode": fake.zipcode(),
        "AccidentLatitude": fake.latitude(),
        "AccidentLongitude": fake.longitude(),
        "AccidentMonth": fake.month(),
        "AccidentMonthOrder": fake.random_int(min=1, max=12),
        "ClaimSuffix": fake.random_int(min=0, max=999),
        "TypeOfLoss": fake.word(),
        "Adjuster": fake.name(),
        "AccidentQuarter": fake.word(),
        "AccidentQuarterOrder": fake.random_int(min=1, max=4),
        "Estado": fake.word(),
        "SuffixRegisterDate": {"$date": fake.date_time_this_decade().isoformat() + "Z"},
        "IdSuffixStatus": fake.random_int(min=0, max=999),
        "SuffixStatus": fake.word(),
        "FullName": fake.name(),
        "DateOfBirth": fake.date_of_birth(),
        "LicenseNo": fake.word(),
        "LossDescription": fake.sentence(),
        "Claimant": fake.name(),
        "ReportedBy": fake.word(),
        "Litigation": fake.word(),
        "AccidentCity": fake.city(),
        "AccidentCountry": fake.country(),
        "DriverState": fake.state_abbr(),
        "FirstClaimIndReserveDate": fake.date_time_this_decade().isoformat() + "Z",
        "FirstClaimExpReserveDate": fake.date_time_this_decade().isoformat() + "Z",
        "FirstClaimReserveDate": fake.date_time_this_decade().isoformat() + "Z",
        "FirstSuffixIndReserveDate": fake.date_time_this_decade().isoformat() + "Z",
        "FirstSuffixExpReserveDate": fake.date_time_this_decade().isoformat() + "Z",
        "FirstSuffixReserveDate": fake.date_time_this_decade().isoformat() + "Z"
    }

def save_generated_json(output_folder="generated_policy_json"):
    os.makedirs(output_folder, exist_ok=True)

    for idx, fake_data in enumerate([generate_fake_data() for _ in range(10000)], start=1):
        output_file_path = os.path.join(output_folder, f"policyjsondata_{idx}.json")
        with open(output_file_path, 'w') as output_file:
            json.dump(fake_data, output_file, indent=4, default=decimal_default)

        print(f"Fake Data {idx} saved to: {output_file_path}")

if __name__ == "__main__":
    save_generated_json()
