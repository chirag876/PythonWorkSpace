import csv
import json
from Policy import *


def convert_csv_to_json(csv_file_path, json_output_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            root = {
                'RetrievePolicyRequest': {
                    'messageInformation': ResponseMessageInformation().__dict__,
                    'policy': {
                        'cancellationDate': row['cancellationDate'],
                        'effectiveDate': row['effectiveDate'],
                        'expirationDate': row['expirationDate'],
                        'id': row['id'],
                        'lineofBusinessCode': RequestPolicy().lineofBusinessCode,
                        'number': RequestPolicy().number,
                        'originalEffectiveDate': RequestPolicy().originalEffectiveDate,
                        'parentEntityId': RequestPolicy().parentEntityId,
                        'parentEntityTypeName': RequestPolicy().parentEntityTypeName,
                        'cancelReasonDescription': RequestPolicy().cancelReasonDescription,
                        'controllingStateOrProvinceCode': RequestPolicy().controllingStateOrProvinceCode,
                        'statusCode': RequestPolicy().statusCode
                    },
                    'insured': {
                        'id': RequestInsured().id,
                        'parentEntityTypeName': RequestInsured().parentEntityTypeName,
                        'typeCode': RequestInsured().typeCode,
                        'otherGivenName': RequestInsured().otherGivenName,
                        'suffix': RequestInsured().suffix,
                        'titlePrefix': RequestInsured().titlePrefix,
                        'parentEntityId': row['id'],
                        'fullName': row['customerName'],
                        'givenName': row['givenName'],
                        'surname': row['surname']
                    }
                },
                'RetrievePolicyResponse': {
                    'messageInformation': {
                        'businessPurposeTypeCode': RequestMessageInformation().businessPurposeTypeCode,
                        'effectiveDate': RequestMessageInformation().effectiveDate,
                        'trackingNumber': RequestMessageInformation().trackingNumber,
                        'messageStatus': [
                            MessageStatus().__dict__
                        ]
                    },
                    'Quote': {
                        'id': row['quoteId']
                    },
                    'policyHolder': {
                        'CustomerID': row['customerId'],
                        'CustomerName': row['customerName']
                    },
                    'policy': {
                        'cancelReasonDescription': ResponsePolicy().cancelReasonDescription,
                        'controllingStateOrProvinceCode': ResponsePolicy().controllingStateOrProvinceCode,
                        'lineofBusinessCode': ResponsePolicy().lineofBusinessCode,
                        'number': ResponsePolicy().number,
                        'originalEffectiveDate': ResponsePolicy().originalEffectiveDate,
                        'parentEntityId': ResponsePolicy().parentEntityId,
                        'parentEntityTypeName': ResponsePolicy().parentEntityTypeName,
                        'statusCode': ResponsePolicy().statusCode,
                        'claimsCount': row['claimsCount'],
                        'cancellationDate': row['cancellationDate'],
                        'effectiveDate': row['effectiveDate'],
                        'expirationDate': row['expirationDate'],
                        'RenewalDate': row['RenewalDate'],
                        'id': row['id'],
                        'renewalPremium': row['renewalPremium'],
                        'numberOfEmployees': row['numberOfEmployees'],
                        'businessIndustry': row['businessIndustry'],
                        'annualRevenue': row['annualRevenue'],
                        'paymentMethod': row['paymentMethod'],
                        'durationInMonths': row['durationInMonths'],
                        'totalPremium': row['totalPremium'],
                        'renewalStatus': row['RenewalStatus'],
                        'address': [
                            {
                                'city': PolicyAddress().city,
                                'countryCode': PolicyAddress().countryCode,
                                'countryName': PolicyAddress().countryName,
                                'line1': PolicyAddress().line1,
                                'line2': PolicyAddress().line2,
                                'postalCode': PolicyAddress().postalCode,
                                'stateOrProvinceCode': PolicyAddress().stateOrProvinceCode,
                                'stateOrProvinceName': PolicyAddress().stateOrProvinceName,
                                'id': PolicyAddress().id,
                                'latitude': PolicyAddress().latitude,
                                'line3': PolicyAddress().line3,
                                'line4': PolicyAddress().line4,
                                'longitude': PolicyAddress().longitude,
                                'parentEntityId': PolicyAddress().parentEntityId,
                                'parentEntityTypeName': PolicyAddress().parentEntityTypeName,
                                'regionCode': PolicyAddress().regionCode,
                                'regionName': PolicyAddress().regionName,
                                'subRegionCode': PolicyAddress().subRegionCode,
                                'subRegionName': PolicyAddress().subRegionName,
                                'typeCode': PolicyAddress().typeCode,
                                'detailAddress': PolicyAddressDetailAddress().__dict__,
                                'reference': [
                                    {
                                        'appliesTo': 'Business',
                                        'description': 'Headquarters',
                                        'id': 'REF456',
                                        'name': 'HQ'
                                    }
                                ]
                            }
                        ],
                        'coverage': {
                            'cancellationDate': Coverage().cancellationDate,
                            'cancellationReasonCode': Coverage().cancellationReasonCode,
                            'description': Coverage().description,
                            'effectiveDate': Coverage().effectiveDate,
                            'expirationDate': Coverage().expirationDate,
                            'id': Coverage().id,
                            'inceptionDate': Coverage().inceptionDate,
                            'lineOfBusinessCode': Coverage().lineOfBusinessCode,
                            'parentEntityTypeName': Coverage().parentEntityTypeName,
                            'planName': Coverage().planName,
                            'premiumBasisCode': Coverage().premiumBasisCode,
                            'productCode': Coverage().productCode,
                            'typeCode': Coverage().typeCode,
                            'deductible': Coverage().deductible,
                            'limit': Coverage().limit,
                            'reference': Coverage().reference,
                            'scheduledItem': Coverage().scheduledItem,
                            'parentEntityId': row['id'],
                            'deductible': {
                                'amount': Deductible().amount,
                                'id': Deductible().id,
                                'parentEntityTypeName': Deductible().parentEntityTypeName,
                                'typeCode': Deductible().typeCode,
                                'parentEntityId': row['id']
                            },
                            'limit': {
                                'amount': Limit().amount,
                                'id': Limit().id,
                                'parentEntityTypeName': Limit().parentEntityTypeName,
                                'parentEntityId': row['id'],
                                'typeCode': Limit().typeCode
                            },
                            'reference': [
                                {
                                    'appliesTo': 'Coverage',
                                    'description': 'Additional insured endorsement',
                                    'id': 'REF789',
                                    'name': 'AI'
                                }
                            ],
                            'scheduledItem': [
                                {
                                    'categoryCode': ScheduledItem().categoryCode,
                                    'description': ScheduledItem().description,
                                    'effectiveDate': ScheduledItem().effectiveDate,
                                    'expirationDate': ScheduledItem().expirationDate,
                                    'id': ScheduledItem().id,
                                    'limit': Limit().__dict__,
                                    'parentEntityId': ScheduledItem().parentEntityId,
                                    'parentEntityTypeName': ScheduledItem().parentEntityTypeName,
                                    'purchasedDate': ScheduledItem().purchasedDate,
                                    'valuation':
                                    [
                                        {
                                            'description': Valuation().description,
                                            'effectiveDate': Valuation().effectiveDate,
                                            'id': Valuation().id,
                                            'parentEntityId': Valuation().parentEntityId,
                                            'parentEntityTypeName': Valuation().parentEntityTypeName,
                                            'typeCode': Valuation().typeCode,
                                            'amount': Amount().__dict__
                                        }
                                    ]
                                }
                            ]
                        },
                        'insured': [
                            {
                                'id': ResponseInsured().id,
                                'parentEntityTypeName': ResponseInsured().parentEntityTypeName,
                                'typeCode': ResponseInsured().typeCode,
                                'otherGivenName': ResponseInsured().otherGivenName,
                                'suffix': ResponseInsured().suffix,
                                'titlePrefix': ResponseInsured().titlePrefix,
                                'birthDate': ResponseInsured().birthDate,
                                'roleCode': ResponseInsured().roleCode,
                                'parentEntityId': row['id'],
                                'fullName': 'Kristen Santos',
                                'givenName': 'Kristen',
                                'surname': 'Santos',
                                'address':{
                                    'city': InsuredAddress().city,
                                    "countryCode": InsuredAddress().countryCode,
                                    "countryName": InsuredAddress().countryName,
                                    "line1": InsuredAddress().line1,
                                    "line2": InsuredAddress().line2,
                                    "postalCode": InsuredAddress().postalCode,
                                    "stateOrProvinceCode": InsuredAddress().stateOrProvinceCode,
                                    "stateOrProvinceName": InsuredAddress().stateOrProvinceName,
                                    "id": InsuredAddress().id,
                                    "latitude": InsuredAddress().latitude,
                                    "line3": InsuredAddress().line3,
                                    "line4": InsuredAddress().line4,
                                    "longitude": InsuredAddress().longitude,
                                    "parentEntityId": InsuredAddress().parentEntityId,
                                    "parentEntity": InsuredAddress().parentEntity,
                                    'typeName': InsuredAddress().typeName,
                                    'regionCode': InsuredAddress().regionCode,
                                    'regionName': InsuredAddress().regionName,
                                    'subRegionCode': InsuredAddress().subRegionCode,
                                    'subRegionName': "",
                                    'typeCode': InsuredAddress().typeCode,
                                    'detailAddress': InsuredAddressDetailAddress().__dict__,
                                    'reference': [],

                                }
                            }
                        ],
                        'producer': {
                            'branch': Producer().branch,
                            'id': Producer().id,
                            'number': Producer().number,
                            'parentEntityTypeName': Producer().parentEntityTypeName,
                            'fullName': Producer().fullName,
                            'givenName': Producer().givenName,
                            'otherGivenName': Producer().otherGivenName,
                            'suffix': Producer().suffix,
                            'surname': Producer().surname,
                            'titlePrefix': Producer().titlePrefix,
                            'parentEntityId': row['id']
                        },
                        'reference': [
                            {
                                'appliesTo': 'Policy',
                                'description': 'Additional insured endorsement',
                                'id': 'REF789',
                                'name': 'AI'
                            }
                        ],
                        'underwriter': {
                            'parentEntityId': row['id'],
                            'parentEntityTypeName': Underwriter().parentEntityTypeName,
                            'fullName': Underwriter().fullName,
                            'givenName': Underwriter().givenName,
                            'otherGivenName': Underwriter().otherGivenName,
                            'suffix': Underwriter().suffix,
                            'surname': Underwriter().surname,
                            'titlePrefix': Underwriter().titlePrefix,
                            'id': Underwriter().id
                        }
                    },
                    'claim': {
                        'parentEntityTypeName': Claim().parentEntityTypeName,
                        'lossDate': Claim().lossDate,
                        'reportDate': Claim().reportDate,
                        'status': Claim().status,
                        'description': Claim().description,
                        'reserveAmount': 0,
                        'id': row['claimId'],
                        'parentEntityId': row['id'],
                        'amount': row['claimAmount'],
                        'adjuster': {
                            'id': Adjuster().id,
                            'parentEntityTypeName': Adjuster().parentEntityTypeName,
                            'fullName': Adjuster().fullName,
                            'givenName': Adjuster().givenName,
                            'otherGivenName': Adjuster().otherGivenName,
                            'suffix': Adjuster().suffix,
                            'surname': Adjuster().surname,
                            'titlePrefix': Adjuster().titlePrefix,
                            'parentEntityId': row['id']
                        },
                        'reference': [
                            {
                                'appliesTo': 'Claim',
                                'description': 'Photos of damage',
                                'id': 'REF789',
                                'name': 'DamagePhotos'
                            }
                        ]
                    }
                }
            }

            json_output = json.dumps(
                root, default=lambda o: o.__dict__, indent=2)
            file_name = row['id']
            with open(f"{json_output_path}/{file_name}.json", "w") as json_file:
                json_file.write(json_output)
            print(f"Converted {file_name}.json")


# Converting the policy_data_extraction_train.csv file (having 1000 records) to 1000 PolicyJson
convert_csv_to_json("C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\csv\PolicyDataExtraction\V1_policy_data_extraction_train.csv",
                    "C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\Excel to json\Policytrainjson")