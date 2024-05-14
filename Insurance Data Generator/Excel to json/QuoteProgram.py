import csv
import json
from Quote import *

def convert_csv_to_json(csv_file_path, json_output_path):
    with open(csv_file_path, 'r') as csv_file:
        reader = csv.DictReader(csv_file)

        for row in reader:
            root = {
                'SubmitGeneralLiabilityQuoteRequest': {
                    'insured': {
                        'address': {
                            'city': Address().city,
                            'countryCode': Address().countryCode,
                            'countryName': Address().countryName,
                            'line1': Address().line1,
                            'postalCode': Address().postalCode,
                            'stateOrProvinceCode': Address().stateOrProvinceCode,
                            'stateOrProvinceName':Address().stateOrProvinceName,
                            'detailAddress': DetailAddress().__dict__,
                        },
                        'business': Business().__dict__,
                        'contact': {
                            'communication': [
                                Communication().__dict__
                            ],
                            'fullName': row['customerName']
                        }
                    },
                    'location': Location().__dict__,
                    'messageInformation': RequestMessageInformation().__dict__
                },
                'SubmitGeneralLiabilityQuoteResponse': {
                    'messageInformation': {
                        'businessPurposeTypeCode':RequestMessageInformation().businessPurposeTypeCode,
                        'messageStatus': [MessageStatus().__dict__]
                    },
                    'quote': {
                        'id': row['quoteId'],
                        'insured': {
                            'address': {
                                'city': Address().city,
                                'countryCode': Address().countryCode,
                                'countryName': Address().countryName,
                                'line1': Address().line1,
                                'postalCode': Address().postalCode,
                                'stateOrProvinceCode': Address().stateOrProvinceCode,
                                'stateOrProvinceName':Address().stateOrProvinceName,
                                'detailAddress': DetailAddress().__dict__
                            },
                            'business': Business().__dict__,
                            'contact': {
                                'communication': [
                                    Communication().__dict__
                                ],
                                'fullName': row['customerName']
                            }
                        },
                        'location': Location().__dict__,
                        'premium': {
                            'amount': float(row['totalPremium']),
                            'currencyCode':Premium().currencyCode,
                            'period': Period().__dict__
                        }
                    }
                }
            }

            json_output = json.dumps(root, default=lambda o: o.__dict__, indent=2)
            file_name = row['quoteId']
            with open(f"{json_output_path}/{file_name}.json", "w") as json_file:
                json_file.write(json_output)
            print(f"Converted {file_name}.json")


# Converting the policyComplete.csv file (having 1000 records) to 1000 QuoteJson
convert_csv_to_json("C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\csv\policyComplete.csv",
                    "C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\Excel to json\QuoteJson")

