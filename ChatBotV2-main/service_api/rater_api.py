import requests

def rater():
    data = {
            "InsuredInfo": {
                "InsuredName": "John Doe",
                "Address1": "47 W 13TH ST",
                "Address2": "",
                "City": "NEW YORK",
                "State": "NY",
                "Zipcode": "10011-7956",
                "Coverage": "FullCoverage"
            },
            "RentersBasicsDetail": {
                "UnitOfSite": "10",
                "YearBuilt": "2",
                "GatedCommunity": "Yes",
                "ProfessionallyManaged": "3-5"       
            },
            "InteriorBasicsDetail": {        
                "FireAlarm": "Central Alarm (Alerts Monitoring Center)"      
            },
            "CoveragesInfoPersonalLibility": {
                "LiabilityMedPayLimit": "$100,000 / $1,000",
                "AnimalLiabilityBuyBack": "100000",
                "NamedInsured": "3",
                "MandLiabilityCovg": "New York Liability Only Policy DL 24 01,Animal Liability Limitation Endorsement BR HO4 ALL,Special Provisions Endorsement DL 25 31,Certain Residence Employees Workers Compensation Endorsement DL 24 15",
                "ExpenseConstant": 20000,
                "LocalTaxesAndAssessments": 10000,
                "StateAssessmentsAndSurcharge": 50000,
                "LimitOfLiability": 0,
                "EmergencyAssesmentCharge": 0,
                "PolicyFee": 0
            },
            "CoveragesInfoPersonalProperty": {
                "PersonalPropLimit": 43800,
                "Deductible": "250 All Other Perils/500 Theft",
                "PaymentPlan": "Annual",
                "IsIncludeLossOfUseCoverage": "Yes",
                "LossOfUseCoverageLimit": 10000,
                "PersonalPropertyCoverage": "null",
                "Jewelry": 15000,
                "Furs": 20000,
                "Silverware": 0,
                "FineArts": 0,
                "Cameras": 0,
                "MusicalEquipment": 0,
                "GolfersEquipment": 0,
                "StampCollections": 0,
                "WomensJewelry": 0,
                "MensJewelry": 0,
                "MusicalInstruments": 0,
                "UnscheduledJewelryWatchesFurs": 20000,
                "UnscheduledSilverwareGoldwareAndPewterware": 10000,
                "OptionalPersonalPropCov": "Pet Damage Endorsement,Water Backup of Sewers and drains Endorsement,Renters Plus Package,Personal Property Replacement Cost Endorsement",
                "MandatoryPersonalPropCov": "Special Provisions New York HO 01 31,New York Renters Mandatory Endorsement BR HO4 TM,Animal Liability Limitation Endorsement BR HO4 ALL",
                "LimitedBegBugCoverages": "false",
                "LimitedBegBugLimit": 0,
                "LimitedFungiWetDryRot": "false",
                "LimitedFungiWetDryRotLimit": "",
                "NJWorkersEndorsement": "false",
                "ResidenceEmployeesClassCount": []
            }
        }

    if data:
        try:
            headers = {'Content-Type': 'application/json'}
            url = "http://apiv2uat.conveloins.com/AgentPortal/HORenters/GetPremium"
            response = requests.post(url, json= data, headers=headers).json()
            #print(data)
            print(response)
            return response
        except:
            return "We are unable to process your request. Please try again in sometime"