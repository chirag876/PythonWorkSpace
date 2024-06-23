import json
from faker import Faker
from decimal import Decimal
import os
from datetime import date, datetime
import random
import string

fake = Faker()

def decimal_default(obj):
    if isinstance(obj, Decimal):
        return float(obj)
    elif isinstance(obj, (date, datetime)):
        return obj.isoformat()
    raise TypeError(f"Object of type {obj.__class__.__name__} is not JSON serializable")

cpu_utilization = random.uniform(0, 100)  # CPU utilization percentage
ram_usage = random.uniform(1, 64)         # RAM usage in GB (assuming a range of 1GB to 64GB)
rom_capacity = random.randint(128, 1024)  # ROM capacity in MB (assuming a range of 128MB to 1024MB)
network_throughput = random.uniform(1, 1000)  # Network throughput in MBPS/GPBS (assuming a range of 1MBPS to 1000MBPS)
system_uptime_days = random.randint(0, 30)   # System uptime in days
system_uptime_hours = random.randint(0, 23)  # System uptime in hours
system_uptime_minutes = random.randint(0, 59)


CancelReasonDescription = [
    "Customer changed insurance providers.",
    "Policy no longer meets customer's needs.",
    "Financial reasons.",
    "Moving to a different location.",
    "Policy coverage duplicated with another insurance plan.",
    "Unexpected change in personal circumstances.",
    "Unsatisfactory customer service experience.",
    "Found a better deal elsewhere.",
    "Policy terms and conditions were not clear.",
    "Insurance premiums became too expensive.",
    "Policyholder passed away.",
    "Vehicle or property covered by policy was sold or disposed of.",
    "Disagreement with claim settlement.",
    "Canceling due to policyholder's health reasons.",
    "Policyholder lost job and can no longer afford premiums.",
    "Policyholder's family circumstances changed.",
    "Policyholder going through divorce or separation."
]


ControllingStateOrProvinceCode = ["AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DE", "FL", "GA", "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
"SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]


LineOfBusinessCode = ["PA - Personal Auto", "CA - Commercial Auto","HO - Homeowners","RE - Renters", "CP - Commercial Property",
    "IH - Individual Health", "GH - Group Health", "TL - Term Life", "WL - Whole Life", "UL - Universal Life", "GL - General Liability",
    "WC - Workers' Compensation", "PL - Professional Liability", "CY - Cyber Liability", "DNO - Directors and Officers (D&O)", "TR - Travel", "MC - Marine Cargo", "MH - Marine Hull", "AV - Aviation",  "UE - Umbrella/Excess"
]


ParentEntityTypeName = [
    "Bajaj Allianz Life Insurance Company Limited",
    "Birla Sun Life Insurance Co. Ltd",
    "HDFC Standard Life Insurance Co. Ltd",
    "ICICI Prudential Life Insurance Co. Ltd",
    "IndiaFirst Life Insurance Company Ltd",
    "ING Vysya Life Insurance Company Ltd.",
    "Life Insurance Corporation of India",
    "Max New York Life Insurance Co. Ltd",
    "Met Life India Insurance Company Ltd.",
    "Kotak Mahindra Old Mutual Life Insurance Limited",
    "SBI Life Insurance Co. Ltd",
    "Tata AIG Life Insurance Company Limited",
    "Reliance Life Insurance Company Limited.",
    "Aviva Life Insurance Company India Limited",
    "Sahara India Life Insurance Co, Ltd.",
    "Shriram Life Insurance Co, Ltd.",
    "Bharti AXA Life Insurance Company Ltd.",
    "Future Generali India Life Insurance Company Limited",
    "IDBI Fortis Life Insurance Company Ltd.",
    "Canara HSBC Oriental Bank of Commerce Life Insurance Company Ltd.",
    "Aegon Religare Life Insurance Company Limited",
    "DLF Pramerica Life Insurance Company Limited",
    "Star Union Dai-Ichi Life Insurance Company Limited",
    "IndiaFirst Life Insurance Company Limited",
    "Edelweiss Tokio Life Insurance Co. Ltd"
]

StatusCode = ["Active", "Expired", "Cancelled", "Pending", "Suspended","Under Review","Lapsed","Terminated"]

TotalPremium = round(random.uniform(100, 5000), 2)

AgentCode = random.randint(1000, 9999)

ReferalCode = random.randint(1000, 9999)

RenewalStatus = ["Renewed", "Renewal Pending"]

TransactionType = ["Sold Policy", "Renewal", "Endorsement", "Cancellation", "Reinstatement"]

def generate_fake_data():
    fake_data = {
        # "_id": {"$oid": fake.uuid4()},
        "CorrelationId": fake.uuid4(),
        "AuditableRequestId": fake.uuid4(),
        "AuditableRequestName": fake.word(),
        "AuditableSourceEventName": fake.word(),
        "CreatedBy": fake.name(),
        "CreatedDateTime": {"$date": fake.date_time_this_decade().isoformat()},
        "UpdatedBy": fake.name(),
        "UpdatedDateTime": {"$date": fake.date_time_this_decade().isoformat()},
        "UpdateReason": fake.sentence(),
        "OwnerId": fake.uuid4(),
        "IsActive": fake.boolean(),
        "IsDeleted": fake.boolean(),
        "IsApproved": fake.boolean(),
        "ApproverId": fake.uuid4(),
        "ApprovedDateTime": {"$date": fake.date_time_this_decade().isoformat()},
        "IsAuthorized": fake.boolean(),
        "AuthorizedById": fake.uuid4(),
        "AuthorizedDateTime": {"$date": fake.date_time_this_decade().isoformat()},
        "SysData": {
                                "CPU Utilization": f"{cpu_utilization:.2f}%",
                                "RAM Usage": f"{ram_usage:.2f} GB",            
                                "ROM Capacity": f"{rom_capacity} MB",
                                "Network Throughput": f"{network_throughput:.2f} MBPS", 
                                "System Uptime": f"{system_uptime_days} days, {system_uptime_hours} hours, {system_uptime_minutes} minutes"
                            },
        "TenantId": fake.uuid4(),
        "SubTenantId": fake.uuid4(),
        "QuoteId": fake.uuid4(),
        "CancellationDate": {"$date": fake.date_time_this_decade().isoformat()},
        "CancelReasonDescription": random.choice(CancelReasonDescription),
        "ControllingStateOrProvinceCode": random.choice(ControllingStateOrProvinceCode),
        "EffectiveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "ExpirationDate": {"$date": fake.date_time_between_dates().isoformat()},
        "PolicyId": fake.uuid4(),
        "LineOfBusinessCode": random.choice(LineOfBusinessCode),
        "Number": "POL" + str(fake.random_int(min=100000000, max=999999999)),
        "OriginalEffectiveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "ParentEntityId": fake.uuid4(),
        "ParentEntityTypeName": random.choice(ParentEntityTypeName),
        "StatusCode": random.choice(StatusCode),
        "TotalPremium": f"${TotalPremium}",
        "AgentCode": f"AG{AgentCode}",
        "AccountingDate": {"$date": fake.date_time_this_decade().isoformat()},
        "ReferalCode": f"REF{ReferalCode}",
        "RenewalStatus": random.choice(RenewalStatus),
        "TransactionType": random.choice(TransactionType),
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
    # Generate fake country name and country code
    country_name = fake.country()
    country_words = country_name.split()
    
    # Abbreviate country name based on the number of words
    if len(country_words) == 1:
        country_code = country_name[:2].upper()
    else:
        country_code = ''.join(word[0].upper() for word in country_words)
    
    StateOrProvinceName = fake.state()
    StateOrProvinceCodewords = StateOrProvinceName.split()
    
    if len(StateOrProvinceCodewords) == 1:
        StateOrProvinceCode = StateOrProvinceName[:2].upper()
    else:
        StateOrProvinceCode = ''.join(word[0].upper() for word in StateOrProvinceCodewords)
        
    pre_direction_codes = ['North', 'South', 'East', 'West']
    post_direction_codes = ['North', 'South', 'East', 'West']
    street_type_codes = ['St. - Street','Ave. - Avenue','Rd. - Road','Blvd. - Boulevard','Ln. - Lane','Dr. - Drive','Ct. - Court',
    'Pl. - Place','Pkwy. - Parkway','Way - Way']

    return {
        "City": fake.city(),
        "CountryCode": country_code,
        "CountryName": country_name,
        "Line1": fake.street_address(),
        "Line2": fake.secondary_address(),
        "PostalCode": fake.zipcode(),
        "StateOrProvinceCode": StateOrProvinceCode,
        "StateOrProvinceName": StateOrProvinceName,
        "DetailAddress": {
            "PostDirectionCode": random.choice(post_direction_codes),
            "PreDirectionCode": random.choice(pre_direction_codes),
            "StreetName": fake.street_name(),
            "StreetNumber": fake.building_number(),
            "StreetTypeCode": random.choice(street_type_codes),
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
                "createdTimestamp": {"$date": fake.date_time_this_decade().isoformat()},
                "updatedTimestamp": {"$date": fake.date_time_this_decade().isoformat()}
            }
        ]
    }

def generate_fake_insured():
    return {
        "InsuredId": fake.uuid4(),
        "ParentEntityId": fake.uuid4(),
        "ParentEntityTypeName": random.choice(ParentEntityTypeName),
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
        "AccidentDate": {"$date": fake.date_time_this_decade().isoformat()},
        "ReportedDate": {"$date": fake.date_time_this_decade().isoformat()},
        "RegisterDate": {"$date": fake.date_time_this_decade().isoformat()},
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
        "SuffixRegisterDate": {"$date": fake.date_time_this_decade().isoformat()},
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
        "FirstClaimIndReserveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "FirstClaimExpReserveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "FirstClaimReserveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "FirstSuffixIndReserveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "FirstSuffixExpReserveDate": {"$date": fake.date_time_this_decade().isoformat()},
        "FirstSuffixReserveDate": {"$date": fake.date_time_this_decade().isoformat()}
    }

def save_generated_json(output_folder="generated_policy_json2"):
    os.makedirs(output_folder, exist_ok=True)

    for idx, fake_data in enumerate([generate_fake_data() for _ in range(1)], start=1):
        output_file_path = os.path.join(output_folder, f"policyjsondata_{idx}.json")
        with open(output_file_path, 'w') as output_file:
            json.dump(fake_data, output_file, indent=4, default=decimal_default)
        print(f"Fake Data {idx} saved to: {output_file_path}")

if __name__ == "__main__":
    save_generated_json()


