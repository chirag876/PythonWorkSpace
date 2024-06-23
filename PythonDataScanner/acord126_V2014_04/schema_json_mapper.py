import json

def acord126_mapper(schema_data,json_data,file_name):
    try:
        # Load the source JSON data
        source_data = json_data

        # Load the schema JSON data
        # with open('acord126_V2014_04/schema/updated_schema.json', 'r') as schema_file:
        #     schema_data = json.load(schema_file)


        # Manual Mapping

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["FILE NAME"] = source_data.get("File name", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PAGE COUNT"] = source_data.get("Page count", "")    
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["AGENCY CUSTOMER ID"] = source_data["Page_1"]["all_kvs"].get("AGENCY CUSTOMER ID", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["DATE (MM/DD/YYYY)"] = source_data["Page_1"]["all_kvs"].get("DATE MM DD/YYYY)", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["AGENCY"] = source_data["Page_1"]["all_kvs"].get("AGENCY", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CARRIER"] = source_data["Page_1"]["all_kvs"].get("CARRIER", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["NAIC CODE"] = source_data["Page_1"]["all_kvs"].get("NAIC CODE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["POLICY NUMBER"] = source_data["Page_1"]["all_kvs"].get("POLICY NUMBER", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EFFECTIVE DATE"] = source_data["Page_1"]["all_kvs"].get("EFFECTIVE DATE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["APPLICANT / FIRST NAMED INSURED"] = source_data["Page_1"]["all_kvs"].get("APPLICANT / FIRST NAMED INSURED", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["COVERAGES"]["COMMERCIAL GENERAL LIABILITY"] = source_data["Page_1"]["all_kvs"].get("COMMERCIAL GENERAL LIABILITY", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["COVERAGES"]["CLAIMS MADE"] = source_data["Page_1"]["all_kvs"].get("CLAIMS MADE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["COVERAGES"]["OCCURRENCE"] = source_data["Page_1"]["all_kvs"].get("OCCURRENCE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["COVERAGES"]["OWNER'S & CONTRACTOR'S PROTECTIVE"] = source_data["Page_1"]["all_kvs"].get("OWNER'S & CONTRACTOR'S PROTECTIVE", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["DEDUCTIBLES"]["PROPERTY DAMAGE"] = source_data["Page_1"]["all_kvs"].get("PROPERTY DAMAGE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["DEDUCTIBLES"]["BODILY INJURY"] = source_data["Page_1"]["all_kvs"].get("BODILY INJURY", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["DEDUCTIBLES"]["PER CLAIM"] = source_data["Page_1"]["all_kvs"].get("PER CLAIM", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["DEDUCTIBLES"]["PER OCCURRENCE"] = source_data["Page_1"]["all_kvs"].get("PER OCCURRENCE", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["LIMITS"]["GENERAL AGGREGATE"] = source_data["Page_1"]["all_kvs"].get("GENERAL AGGREGATE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["LIMITS"]["LIMIT APPLIES PER"]["POLICY"] = source_data["Page_1"]["all_kvs"].get("POLICY", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["LIMITS"]["LIMIT APPLIES PER"]["PROJECT"] = source_data["Page_1"]["all_kvs"].get("PROJECT", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["LIMITS"]["LIMIT APPLIES PER"]["LOCATION"] = source_data["Page_1"]["all_kvs"].get("LOCATION", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["LIMITS"]["LIMIT APPLIES PER"]["OTHER"] = source_data["Page_1"]["all_kvs"].get("OTHER", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PRODUCTS & COMPLETED OPERATIONS AGGREGATE"] = source_data["Page_1"]["all_kvs"].get("PRODUCTS & COMPLETED OPERATIONS AGGREGATE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PERSONAL & ADVERTISING INJURY"] = source_data["Page_1"]["all_kvs"].get("PERSONAL & ADVERTISING INJURY", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EACH OCCURRENCE"] = source_data["Page_1"]["all_kvs"].get("EACH OCCURRENCE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["DAMAGE TO RENTED PREMISES (each occurrence)"] = source_data["Page_1"]["all_kvs"].get("DAMAGE TO RENTED PREMISES (each occurrence)", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["MEDICAL EXPENSE (Any one person)"] = source_data["Page_1"]["all_kvs"].get("MEDICAL EXPENSE (Any one person)", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EMPLOYEE BENEFITS"] = source_data["Page_1"]["all_kvs"].get("EMPLOYEE BENEFITS", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PREMIUMS"]["PREMISES/OPERATIONS"] = source_data["Page_1"]["all_kvs"].get("PREMISES/OPERATIONS", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PREMIUMS"]["PRODUCTS"] = source_data["Page_1"]["all_kvs"].get("PRODUCTS", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PREMIUMS"]["OTHER"] = source_data["Page_1"]["all_kvs"].get("OTHER", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["PREMIUMS"]["TOTAL"] = source_data["Page_1"]["all_kvs"].get("TOTAL", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["OTHER COVERAGES, RESTRICTIONS AND/OR ENDORSEMENTS (For hired/non-owned auto coverages attach the applicable state Business Auto Section, ACORD 137)"] = source_data["Page_1"]["all_kvs"].get("OTHER COVERAGES, RESTRICTIONS AND/OR ENDORSEMENTS (For hired/non-owned auto coverages attach the applicable state Business Auto Section, ACORD 137)", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["APPLICABLE ONLY IN WISCONSIN: IF NON-OWNED ONLY AUTO COVERAGE IS TO BE PROVIDED UNDER THE POLICY:"]["1. UM / UIM COVERAGE"]["IS"] = source_data["Page_1"]["all_kvs"].get("IS", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["APPLICABLE ONLY IN WISCONSIN: IF NON-OWNED ONLY AUTO COVERAGE IS TO BE PROVIDED UNDER THE POLICY:"]["1. UM / UIM COVERAGE"]["IS NOT AVAILABLE"] = source_data["Page_1"]["all_kvs"].get("IS NOT AVAILABLE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["APPLICABLE ONLY IN WISCONSIN: IF NON-OWNED ONLY AUTO COVERAGE IS TO BE PROVIDED UNDER THE POLICY:"]["2. MEDICAL PAYMENTS COVERAGE"]["IS"] = source_data["Page_1"]["all_kvs"].get("IS", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["APPLICABLE ONLY IN WISCONSIN: IF NON-OWNED ONLY AUTO COVERAGE IS TO BE PROVIDED UNDER THE POLICY:"]["2. MEDICAL PAYMENTS COVERAGE"]["IS NOT AVAILABLE"] = source_data["Page_1"]["all_kvs"].get("IS NOT AVAILABLE", "")

        ###############################################################################################################################

        # Initialize "SCHEDULE OF HAZARDS" as an empty list for the schema data
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["SCHEDULE OF HAZARDS"] = []

        # Iterate over each row in the source table_3 data
        for row in source_data["Page_1"]["table_data"]["table_3"]:
            # Map each row to the schema structure for "SCHEDULE OF HAZARDS"
            hazard_entry = {
                "LOC": row.get(".", ""),
                "HAZ": row.get(",", ""),
                "CLASSIFICATION": row.get("CLASSIFICATION", ""),
                "CLASS CODE": row.get("CODE", ""),
                "PREMIUM BASIS": row.get("BASIS", ""),
                "EXPOSURE": row.get("EXPOSURE", ""),
                "TERR": row.get("TERR", ""),
                "RATE": {
                    "PREM/OPS": row.get("PREMOPS", {}),  
                    "PRODUCTS": row.get("PRODUCTS", {})
                },
                "PREMIUM": {
                    "PREM/OPS": row.get("PREMIOPS", {}),
                    "PRODUCTS": row.get("PREMIUM", {})
                }
            }
            # Append this hazard entry to the list in the schema
            schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["SCHEDULE OF HAZARDS"].append(hazard_entry)

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["1"]["PROPOSED RETROACTIVE DATE"] = source_data["Page_1"]["all_kvs"].get("1. PROPOSED RETROACTIVE DATE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["1"]["Y / N"] = source_data["Page_1"]["all_kvs"].get("1. PROPOSED RETROACTIVE DATE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["2"]["ENTRY DATE INTO UNINTERRUPTED CLAIMS MADE COVERAGE"] = source_data["Page_1"]["all_kvs"].get("2. ENTRY DATE INTO UNINTERRUPTED CLAIMS MADE COVERAGE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["2"]["Y / N"] = source_data["Page_1"]["all_kvs"].get("2. ENTRY DATE INTO UNINTERRUPTED CLAIMS MADE COVERAGE", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["3"]["HAS ANY PRODUCT, WORK, ACCIDENT, OR LOCATION BEEN EXCLUDED, UNINSURED OR SELF-INSURED FROM ANY PREVIOUS COVERAGE?"] = source_data["Page_1"]["all_kvs"].get("3. HAS ANY PRODUCT, WORK, ACCIDENT, OR LOCATION BEEN EXCLUDED, UNINSURED OR SELF-INSURED FROM ANY PREVIOUS COVERAGE?", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["3"]["Y / N"] = source_data["Page_1"]["all_kvs"].get("3. HAS ANY PRODUCT, WORK, ACCIDENT, OR LOCATION BEEN EXCLUDED, UNINSURED OR SELF-INSURED FROM ANY PREVIOUS COVERAGE?", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["4"]["WAS TAIL COVERAGE PURCHASED UNDER ANY PREVIOUS POLICY?"] = source_data["Page_1"]["all_kvs"].get("4. WAS TAIL COVERAGE PURCHASED UNDER ANY PREVIOUS POLICY?", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["CLAIMS MADE (Explain all 'Yes' responses)"]["EXPLAIN ALL 'YES' RESPONSES"]["4"]["Y / N"] = source_data["Page_1"]["all_kvs"].get("4. WAS TAIL COVERAGE PURCHASED UNDER ANY PREVIOUS POLICY?", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EMPLOYEE BENEFITS LIABILITY"]["1. DEDUCTIBLE PER CLAIM"] = source_data["Page_1"]["all_kvs"].get("1. DEDUCTIBLE PER CLAIM", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EMPLOYEE BENEFITS LIABILITY"]["2. NUMBER OF EMPLOYEES"] = source_data["Page_1"]["all_kvs"].get("2. NUMBER OF EMPLOYEES", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EMPLOYEE BENEFITS LIABILITY"]["3. NUMBER OF EMPLOYEES COVERED BY EMPLOYEE BENEFITS PLANS"] = source_data["Page_1"]["all_kvs"].get("3. NUMBER OF EMPLOYEES COVERED BY EMPLOYEE BENEFITS PLANS", "")
        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["EMPLOYEE BENEFITS LIABILITY"]["4. RETROACTIVE DATE"] = source_data["Page_1"]["all_kvs"].get("4. RETROACTIVE DATE", "")

        ###############################################################################################################################

        schema_data["Page_1"]["COMMERCIAL GENERAL LIABILITY SECTION"]["ACORD"] = source_data["Page_1"]["all_kvs"].get("ACORD", "")

        ###############################################################################################################################
        # # Correcting the structure and mapping approach

        # # First, ensure the "EXPLAIN ALL 'YES' RESPONSES" section is properly initialized
        # contractors_section = "EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"
        # schema_data["Page_1"]["CONTRACTORS"][contractors_section] = {}

        # # Iterating through each question and mapping it directly without appending to a list
        # # Assuming there's one entry per question in the source
        # for row in source_data["Page_2"]["table_data"]["table_1"]:
        #     question_detail = row["EXPLAIN ALL \"YES\" RESPONSES (For all past or present operations"]
        #     yes_no_response = row["Y / N"]

        #     # Assuming the question_detail starts with "1.", "2.", etc., which indicates the question number
        #     question_number = question_detail.split(".")[0]

        #     # Mapping the details directly under the respective question number without creating a list
        #     schema_data["Page_1"]["CONTRACTORS"][contractors_section][question_number] = {
        #         "QUESTION": question_detail[len(question_number)+2:],  # Removes the "1. " part and gets the rest of the question
        #         "Y / N": yes_no_response
        #     }

        # # Note: This approach assumes each row in your table_1 uniquely corresponds to a different question.
        # # If there are multiple entries for the same question number that need to be captured, further adjustments are needed.

        ###############################################################################################################################

        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["1"]["DOES APPLICANT DRAW PLANS, DESIGNS, OR SPECIFICATIONS FOR OTHERS?"] = source_data["Page_2"]["all_kvs"].get("1. DOES APPLICANT DRAW PLANS DESIGNS OR SPECIFICATIONS FOR OTHERS?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["1"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("1. DOES APPLICANT DRAW PLANS DESIGNS OR SPECIFICATIONS FOR OTHERS?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["2"]["DO ANY OPERATIONS INCLUDE BLASTING OR UTILIZE OR STORE EXPLOSIVE MATERIAL?"] = source_data["Page_2"]["all_kvs"].get("2. DO ANY OPERATIONS INCLUDE BLASTING OR UTILIZE OR STORE EXPLOSIVE MATERIAL?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["2"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("2. DO ANY OPERATIONS INCLUDE BLASTING OR UTILIZE OR STORE EXPLOSIVE MATERIAL?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["3"]["DO ANY OPERATIONS INCLUDE EXCAVATION, TUNNELING, UNDERGROUND WORK OR EARTH MOVING?"] = source_data["Page_2"]["all_kvs"].get("3. DO ANY OPERATIONS INCLUDE EXCAVATION, TUNNELING, UNDERGROUND WORK OR EARTH MOVING?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["3"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("3. DO ANY OPERATIONS INCLUDE EXCAVATION, TUNNELING, UNDERGROUND WORK OR EARTH MOVING?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["4"]["DO YOUR SUBCONTRACTORS CARRY COVERAGES OR LIMITS LESS THAN YOURS?"] = source_data["Page_2"]["all_kvs"].get("4. DO YOUR SUBCONTRACTORS CARRY COVERAGES OR LIMITS LESS THAN YOURS?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["4"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("4. DO YOUR SUBCONTRACTORS CARRY COVERAGES OR LIMITS LESS THAN YOURS?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["5"]["ARE SUBCONTRACTORS ALLOWED TO WORK WITHOUT PROVIDING YOU WITH A CERTIFICATE OF INSURANCE?"] = source_data["Page_2"]["all_kvs"].get("5. ARE SUBCONTRACTORS ALLOWED TO WORK WITHOUT PROVIDING YOU WITH A CERTIFICATE OF INSURANCE?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["5"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("5. ARE SUBCONTRACTORS ALLOWED TO WORK WITHOUT PROVIDING YOU WITH A CERTIFICATE OF INSURANCE?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["6"]["DOES APPLICANT LEASE EQUIPMENT TO OTHERS WITH OR WITHOUT OPERATORS?"] = source_data["Page_2"]["all_kvs"].get("6. DOES APPLICANT LEASE EQUIPMENT TO OTHERS WITH OR WITHOUT OPERATORS?", "")
        schema_data["Page_2"]["CONTRACTORS"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["6"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("6. DOES APPLICANT LEASE EQUIPMENT TO OTHERS WITH OR WITHOUT OPERATORS?", "")

        ###############################################################################################################################

        schema_data["Page_2"]["DESCRIBE THE TYPE OF WORK SUBCONTRACTED"]["$ PAID TO SUBCONTRACTORS"] = source_data["Page_2"]["all_kvs"].get("SPAID TO SUB- CONTRACTORS", "")
        schema_data["Page_2"]["DESCRIBE THE TYPE OF WORK SUBCONTRACTED"]["% OF WORK SUBCONTRACTED"] = source_data["Page_2"]["all_kvs"].get("% OF WORK SUBCONTRACTED", "")
        schema_data["Page_2"]["DESCRIBE THE TYPE OF WORK SUBCONTRACTED"]["# FULL TIME STAFF"] = source_data["Page_2"]["all_kvs"].get("FULL TIME STAFF", "")
        schema_data["Page_2"]["DESCRIBE THE TYPE OF WORK SUBCONTRACTED"]["# PARTTIME STAFF"] = source_data["Page_2"]["all_kvs"].get("PART TIME STAFF", "")

        ###############################################################################################################################

        # Initialize "PRODUCTS / COMPLETED OPERATIONS" as an empty list for the schema data
        schema_data["Page_2"]["PRODUCTS / COMPLETED OPERATIONS"] = []

        # Iterate over each row in the source table_3 data
        for row in source_data["Page_2"]["table_data"]["table_2"]:
            # Map each row to the schema structure for "PRODUCTS / COMPLETED OPERATIONS"
            products_completed_operations = {
                "PRODUCTS": row.get("PRODUCTS", ""),
                "ANNUAL GROSS SALES": row.get("ANNUAL GROSS SALES", ""),
                "# OF UNITS": row.get(". OF UNITS", ""),
                "TIME IN MARKET": row.get("TIME IN MARKET", ""),
                "EXPECTED LIFE": row.get("EXPECTED LIFE", ""),
                "INTENDED USE": row.get("INTENDED USE", ""),
                "PRINCIPAL COMPONENTS": row.get("PRINCIPAL COMPONENTS", ""),
            }
            # Append this hazard entry to the list in the schema
            schema_data["Page_2"]["PRODUCTS / COMPLETED OPERATIONS"].append(products_completed_operations)

        ###############################################################################################################################

        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["1"]["DOES APPLICANT INSTALL, SERVICE OR DEMONSTRATE PRODUCTS?"] = source_data["Page_2"]["all_kvs"].get("1. DOES APPLICANT INSTALL, SERVICE OR DEMONSTRATE PRODUCTS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["1"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("1. DOES APPLICANT INSTALL, SERVICE OR DEMONSTRATE PRODUCTS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["2"]["FOREIGN PRODUCTS SOLD, DISTRIBUTED, USED AS COMPONENTS? (If 'YES', attach ACORD 815)"] = source_data["Page_2"]["all_kvs"].get("2. FOREIGN PRODUCTS SOLD, DISTRIBUTED, USED AS COMPONENTS? (If 'YES', attach ACORD 815)", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["2"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("2. FOREIGN PRODUCTS SOLD, DISTRIBUTED, USED AS COMPONENTS? (If 'YES', attach ACORD 815)", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["3"]["RESEARCH AND DEVELOPMENT CONDUCTED OR NEW PRODUCTS PLANNED?"] = source_data["Page_2"]["all_kvs"].get("3. RESEARCH AND DEVELOPMENT CONDUCTED OR NEW PRODUCTS PLANNED?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["3"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("3. RESEARCH AND DEVELOPMENT CONDUCTED OR NEW PRODUCTS PLANNED?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["4"]["GUARANTEES, WARRANTIES, HOLD HARMLESS AGREEMENTS?"] = source_data["Page_2"]["all_kvs"].get("4. GUARANTEES, WARRANTIES, HOLD HARMLESS AGREEMENTS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["4"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("4. GUARANTEES, WARRANTIES, HOLD HARMLESS AGREEMENTS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["5"]["PRODUCTS RELATED TO AIRCRAFT/SPACE INDUSTRY?"] = source_data["Page_2"]["all_kvs"].get("5. PRODUCTS RELATED TO AIRCRAFT/SPACE INDUSTRY?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["5"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("5. PRODUCTS RELATED TO AIRCRAFT/SPACE INDUSTRY?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["6"]["PRODUCTS RECALLED, DISCONTINUED, CHANGED?"] = source_data["Page_2"]["all_kvs"].get("6. PRODUCTS RECALLED, DISCONTINUED, CHANGED?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["6"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("6. PRODUCTS RECALLED, DISCONTINUED, CHANGED?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["7"]["PRODUCTS OF OTHERS SOLD OR RE-PACKAGED UNDER APPLICANT LABEL?"] = source_data["Page_2"]["all_kvs"].get("7. PRODUCTS OF OTHERS SOLD OR RE-PACKAGED UNDER APPLICANT LABEL?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["7"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("7. PRODUCTS OF OTHERS SOLD OR RE-PACKAGED UNDER APPLICANT LABEL?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["8"]["PRODUCTS UNDER LABEL OF OTHERS?"] = source_data["Page_2"]["all_kvs"].get("8. PRODUCTS UNDER LABEL OF OTHERS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["8"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("8. PRODUCTS UNDER LABEL OF OTHERS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["9"]["VENDORS COVERAGE REQUIRED?"] = source_data["Page_2"]["all_kvs"].get("9. VENDORS COVERAGE REQUIRED?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["9"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("9. VENDORS COVERAGE REQUIRED?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["10"]["DOES ANY NAMED INSURED SELL TO OTHER NAMED INSUREDS?"] = source_data["Page_2"]["all_kvs"].get("10. DOES ANY NAMED INSURED SELL TO OTHER NAMED INSUREDS?", "")
        schema_data["Page_2"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present products or operations) PLEASE ATTACH LITERATURE, BROCHURES, LABELS, WARNINGS, ETC."]["10"]["Y / N"] = source_data["Page_2"]["all_kvs"].get("10. DOES ANY NAMED INSURED SELL TO OTHER NAMED INSUREDS?", "")

        ###############################################################################################################################
        
        schema_data["Page_2"]["ACORD"] = source_data["Page_2"]["all_kvs"].get("ACORD", "")

        ###############################################################################################################################

        schema_data["Page_3"]["ADDITIONAL INTEREST / CERTIFICATE RECIPIENT"] = source_data["Page_3"]["all_kvs"].get("ADDITIONAL INTEREST / CERTIFICATE RECIPIENT", "")

        ###############################################################################################################################

        schema_data["Page_3"]["INTEREST"]["ADDITIONAL INSURED"] = source_data["Page_3"]["all_kvs"].get("ADDITIONAL INSURED", "")
        schema_data["Page_3"]["INTEREST"]["EMPLOYEE AS LESSOR"] = source_data["Page_3"]["all_kvs"].get("EMPLOYEE AS LESSOR", "")
        schema_data["Page_3"]["INTEREST"]["LIENHOLDER"] = source_data["Page_3"]["all_kvs"].get("LIENHOLDER", "")
        schema_data["Page_3"]["INTEREST"]["LOSS PAYEE"] = source_data["Page_3"]["all_kvs"].get("LOSS PAYEE", "")
        schema_data["Page_3"]["INTEREST"]["MORTGAGEE"] = source_data["Page_3"]["all_kvs"].get("MORTGAGEE", "")

        ###############################################################################################################################

        schema_data["Page_3"]["NAME AND ADDRESS"] = source_data["Page_3"]["all_kvs"].get("NAME AND ADDRESS", "")
        schema_data["Page_3"]["RANK"] = source_data["Page_3"]["all_kvs"].get("RANK", "")
        schema_data["Page_3"]["EVIDENCE"] = source_data["Page_3"]["all_kvs"].get("EVIDENCE", "")
        schema_data["Page_3"]["CERTIFICATE"] = source_data["Page_3"]["all_kvs"].get("CERTIFICATE", "")
        schema_data["Page_3"]["REFERENCE / LOAN #"] = source_data["Page_3"]["all_kvs"].get("REFERENCE / LOAN #", "")

        ###############################################################################################################################

        schema_data["Page_3"]["INTEREST IN ITEM NUMBER"]["LOCATION"] = source_data["Page_3"]["all_kvs"].get("LOCATION", "")
        schema_data["Page_3"]["INTEREST IN ITEM NUMBER"]["BUILDING"] = source_data["Page_3"]["all_kvs"].get("BUILDING", "")
        schema_data["Page_3"]["INTEREST IN ITEM NUMBER"]["ITEM CLASS"] = source_data["Page_3"]["all_kvs"].get("ITEM CLASS", "")
        schema_data["Page_3"]["INTEREST IN ITEM NUMBER"]["ITEM"] = source_data["Page_3"]["all_kvs"].get("ITEM", "")
        schema_data["Page_3"]["INTEREST IN ITEM NUMBER"]["ITEM DESCRIPTION"] = source_data["Page_3"]["all_kvs"].get("ITEM DESCRIPTION", "")

        ###############################################################################################################################

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["1"]["ANY MEDICAL FACILITIES PROVIDED OR MEDICAL PROFESSIONALS EMPLOYED OR CONTRACTED?"] = source_data["Page_3"]["all_kvs"].get("1. ANY MEDICAL FACILITIES PROVIDED OR MEDICAL PROFESSIONALS EMPLOYED OR CONTRACTED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["1"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("1. ANY MEDICAL FACILITIES PROVIDED OR MEDICAL PROFESSIONALS EMPLOYED OR CONTRACTED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["2"]["ANY EXPOSURE TO RADIOACTIVE/NUCLEAR MATERIALS?"] = source_data["Page_3"]["all_kvs"].get("2. ANY EXPOSURE TO RADIOACTIVE/NUCLEAR MATERIALS?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["2"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("2. ANY EXPOSURE TO RADIOACTIVE/NUCLEAR MATERIALS?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["3"]["DO/HAVE PAST, PRESENT OR DISCONTINUED OPERATIONS INVOLVE(D) STORING, TREATING, DISCHARGING, APPLYING, DISPOSING, OR TRANSPORTING OF HAZARDOUS MATERIAL? (e.g. landfills, wastes, fuel tanks, etc)"] = source_data["Page_3"]["all_kvs"].get("3. DO/HAVE PAST, PRESENT OR DISCONTINUED OPERATIONS INVOLVE(D) STORING, TREATING, DISCHARGING, APPLYING, DISPOSING, OR TRANSPORTING OF HAZARDOUS MATERIAL? (e.g. landfills, wastes, fuel tanks, etc)", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["3"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("3. DO/HAVE PAST, PRESENT OR DISCONTINUED OPERATIONS INVOLVE(D) STORING, TREATING, DISCHARGING, APPLYING, DISPOSING, OR TRANSPORTING OF HAZARDOUS MATERIAL? (e.g. landfills, wastes, fuel tanks, etc)", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["4"]["ANY OPERATIONS SOLD, ACQUIRED, OR DISCONTINUED IN LAST FIVE (5) YEARS?"] = source_data["Page_3"]["all_kvs"].get("4. ANY OPERATIONS SOLD, ACQUIRED, OR DISCONTINUED IN LAST FIVE (5) YEARS?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["4"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("4. ANY OPERATIONS SOLD, ACQUIRED, OR DISCONTINUED IN LAST FIVE (5) YEARS?", "")

        # schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["5"]["DO YOU RENT OR LOAN EQUIPMENT TO OTHERS?"]["EQUIPMENT"]["TYPE OF EQUIPMENT"]["SMALL TOOLS"] = source_data["Page_3"]["all_kvs"].get("SMALL TOOLS", "")
        # schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["5"]["DO YOU RENT OR LOAN EQUIPMENT TO OTHERS?"]["EQUIPMENT"]["TYPE OF EQUIPMENT"]["LARGE EQUIPMENT"] = source_data["Page_3"]["all_kvs"].get("LARGE EQUIPMENT", "")
        # schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["5"]["DO YOU RENT OR LOAN EQUIPMENT TO OTHERS?"]["EQUIPMENT"]["INSTRUCTION GIVEN (Y/N)"] = source_data["Page_3"]["all_kvs"].get("INSTRUCTION GIVEN (Y/N)", "")
        # schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["5"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("5. DO YOU RENT OR LOAN EQUIPMENT TO OTHERS?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["6"]["ANY WATERCRAFT, DOCKS, FLOATS OWNED, HIRED OR LEASED?"] = source_data["Page_3"]["all_kvs"].get("6. ANY WATERCRAFT, DOCKS, FLOATS OWNED, HIRED OR LEASED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["6"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("6. ANY WATERCRAFT, DOCKS, FLOATS OWNED, HIRED OR LEASED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["7"]["ANY PARKING FACILITIES OWNED/RENTED?"] = source_data["Page_3"]["all_kvs"].get("7. ANY PARKING FACILITIES OWNED/RENTED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["7"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("7. ANY PARKING FACILITIES OWNED/RENTED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["8"]["IS A FEE CHARGED FOR PARKING?"] = source_data["Page_3"]["all_kvs"].get("8. IS A FEE CHARGED FOR PARKING?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["8"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("8. IS A FEE CHARGED FOR PARKING?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["9"]["RECREATION FACILITIES PROVIDED?"] = source_data["Page_3"]["all_kvs"].get("9. RECREATION FACILITIES PROVIDED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["9"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("9. RECREATION FACILITIES PROVIDED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["10"]["ARE THERE ANY LODGING OPERATIONS INCLUDING APARTMENTS? (If 'YES', answer the following):"]["# APTS"] = source_data["Page_3"]["all_kvs"].get(". APTS", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["10"]["ARE THERE ANY LODGING OPERATIONS INCLUDING APARTMENTS? (If 'YES', answer the following):"]["TOTAL APT AREA"] = source_data["Page_3"]["all_kvs"].get("TOTAL APT AREA", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["10"]["ARE THERE ANY LODGING OPERATIONS INCLUDING APARTMENTS? (If 'YES', answer the following):"]["DESCRIBE OTHER LODGING OPERATIONS"] = source_data["Page_3"]["all_kvs"].get("DESCRIBE OTHER LODGING OPERATIONS", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["10"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("10. ARE THERE ANY LODGING OPERATIONS INCLUDING APARTMENTS (If \"YES\" answer the following)", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["APPROVED FENCE"] = source_data["Page_3"]["all_kvs"].get("APPROVED FENCE", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["LIMITED ACCESS"] = source_data["Page_3"]["all_kvs"].get("LIMITED ACCESS", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["DIVING BOARD"] = source_data["Page_3"]["all_kvs"].get("DIVING BOARD", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["SLIDE"] = source_data["Page_3"]["all_kvs"].get("SLIDE", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["ABOVE GROUND"] = source_data["Page_3"]["all_kvs"].get("ABOVE GROUND", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["IN GROUND"] = source_data["Page_3"]["all_kvs"].get("IN GROUND", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)"]["LIFE GUARD"] = source_data["Page_3"]["all_kvs"].get("LIFE GUARD", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["11"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("IS THERE A SWIMMING POOL ON PREMISES? (Check all that apply)", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["12"]["ARE SOCIAL EVENTS SPONSORED?"] = source_data["Page_3"]["all_kvs"].get("12. ARE SOCIAL EVENTS SPONSORED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["12"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("12. ARE SOCIAL EVENTS SPONSORED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["ARE ATHLETIC TEAMS SPONSORED?"]["TYPE OF SPORT"] = source_data["Page_3"]["all_kvs"].get("TYPE OF SPORT", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["ARE ATHLETIC TEAMS SPONSORED?"]["CONTACT SPORT (Y/N)"] = source_data["Page_3"]["all_kvs"].get("CONTACT SPORT (Y/N)", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["ARE ATHLETIC TEAMS SPONSORED?"]["AGE GROUP"]["12 & UNDER"] = source_data["Page_3"]["all_kvs"].get("12 UNDER", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["ARE ATHLETIC TEAMS SPONSORED?"]["AGE GROUP"]["13 - 18"] = source_data["Page_3"]["all_kvs"].get("13-18", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["ARE ATHLETIC TEAMS SPONSORED?"]["AGE GROUP"]["OVER 18"] = source_data["Page_3"]["all_kvs"].get("OVER 18", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["ARE ATHLETIC TEAMS SPONSORED?"]["EXTENT OF SPONSORSHIP"] = source_data["Page_3"]["all_kvs"].get("EXTENT OF SPONSORSHIP", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["13"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("13. ARE ATHLETIC TEAMS SPONSORED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["14"]["ANY STRUCTURAL ALTERATIONS CONTEMPLATED?"] = source_data["Page_3"]["all_kvs"].get("14. ANY STRUCTURAL ALTERATIONS CONTEMPLATED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["14"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("14. ANY STRUCTURAL ALTERATIONS CONTEMPLATED?", "")

        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["15"]["ANY DEMOLITION EXPOSURE CONTEMPLATED?"] = source_data["Page_3"]["all_kvs"].get("15. ANY DEMOLITION EXPOSURE CONTEMPLATED?", "")
        schema_data["Page_3"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["15"]["Y / N"] = source_data["Page_3"]["all_kvs"].get("15. ANY DEMOLITION EXPOSURE CONTEMPLATED?", "")

        schema_data["Page_3"]["ACORD"] = source_data["Page_3"]["all_kvs"].get("ACORD", "")

        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["16"]["HAS APPLICANT BEEN ACTIVE IN OR IS CURRENTLY ACTIVE IN JOINT VENTURES?"] = source_data["Page_4"]["all_kvs"].get("16. HAS APPLICANT BEEN ACTIVE IN OR IS CURRENTLY ACTIVE IN JOINT VENTURES?", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["16"]["Y / N"] = source_data["Page_4"]["all_kvs"].get("16. HAS APPLICANT BEEN ACTIVE IN OR IS CURRENTLY ACTIVE IN JOINT VENTURES?", "")

        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["17"]["DO YOU LEASE EMPLOYEES TO OR FROM OTHER EMPLOYERS?"]["LEASE TO"] = source_data["Page_4"]["all_kvs"].get("LEASE TO", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["17"]["DO YOU LEASE EMPLOYEES TO OR FROM OTHER EMPLOYERS?"]["WORKERS COMPENSATION COVERAGE CARRIED (Y/N)"] = source_data["Page_4"]["all_kvs"].get("WORKERS COMPENSATION COVERAGE CARRIED (Y/N)", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["17"]["Y / N"] = source_data["Page_4"]["all_kvs"].get("DO YOU LEASE EMPLOYEES TO OR FROM OTHER EMPLOYERS?", "")

        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["18"]["IS THERE A LABOR INTERCHANGE WITH ANY OTHER BUSINESS OR SUBSIDIARIES?"] = source_data["Page_4"]["all_kvs"].get("18. IS THERE A LABOR INTERCHANGE WITH ANY OTHER BUSINESS OR SUBSIDIARIES?", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["18"]["Y / N"] = source_data["Page_4"]["all_kvs"].get("18. IS THERE A LABOR INTERCHANGE WITH ANY OTHER BUSINESS OR SUBSIDIARIES?", "")

        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["19"]["ARE DAY CARE FACILITIES OPERATED OR CONTROLLED?"] = source_data["Page_4"]["all_kvs"].get("19. ARE DAY CARE FACILITIES OPERATED OR CONTROLLED?", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["19"]["Y / N"] = source_data["Page_4"]["all_kvs"].get("19. ARE DAY CARE FACILITIES OPERATED OR CONTROLLED?", "")

        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["20"]["HAVE ANY CRIMES OCCURRED OR BEEN ATTEMPTED ON YOUR PREMISES WITHIN THE LAST THREE (3) YEARS?"] = source_data["Page_4"]["all_kvs"].get("20. HAVE ANY CRIMES OCCURRED OR BEEN ATTEMPTED ON YOUR PREMISES WITHIN THE LAST THREE (3) YEARS?", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["20"]["Y / N"] = source_data["Page_4"]["all_kvs"].get("20. HAVE ANY CRIMES OCCURRED OR BEEN ATTEMPTED ON YOUR PREMISES WITHIN THE LAST THREE (3) YEARS?", "")

        ###############################################################################################################################

        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["22"]["DOES THE BUSINESSES' PROMOTIONAL LITERATURE MAKE ANY REPRESENTATIONS ABOUT THE SAFETY OR SECURITY OF THE PREMISES?"] = source_data["Page_4"]["all_kvs"].get("22. DOES THE BUSINESSES' PROMOTIONAL LITERATURE MAKE ANY REPRESENTATIONS ABOUT THE SAFETY OR SECURITY OF THE PREMISES?", "")
        schema_data["Page_4"]["GENERAL INFORMATION"]["EXPLAIN ALL 'YES' RESPONSES (For all past or present operations)"]["22"]["Y / N"] = source_data["Page_4"]["all_kvs"].get("22. DOES THE BUSINESSES' PROMOTIONAL LITERATURE MAKE ANY REPRESENTATIONS ABOUT THE SAFETY OR SECURITY OF THE PREMISES?", "")
        ###############################################################################################################################

        schema_data["Page_4"]["REMARKS (ACORD 101, Additional Remarks Schedule, may be attached if more space is required)"] = source_data["Page_4"]["all_kvs"].get("REMARKS (ACORD 101, Additional Remarks Schedule, may be attached if more space is required)", "")
        schema_data["Page_4"]["PRODUCER'S SIGNATURE"] = source_data["Page_4"]["all_kvs"].get("PRODUCER'S SIGNATURE", "")
        schema_data["Page_4"]["PRODUCER'S NAME (Please Print)"] = source_data["Page_4"]["all_kvs"].get("PRODUCER'S NAME (Please Print)", "")
        schema_data["Page_4"]["STATE PRODUCER LICENSE NO (Required on Florida)"] = source_data["Page_4"]["all_kvs"].get("STATE PRODUCER LICENSE NO (Required on Florida", "")
        schema_data["Page_4"]["APPLICANT'S SIGNATURE"] = source_data["Page_4"]["all_kvs"].get("APPLICANT'S SIGNATURE", "")
        schema_data["Page_4"]["DATE"] = source_data["Page_4"]["all_kvs"].get("DATE", "")
        schema_data["Page_4"]["NATIONAL PRODUCER NUMBER"] = source_data["Page_4"]["all_kvs"].get("NATIONAL PRODUCER NUMBER", "")
        
        schema_data["Page_4"]["ACORD"] = source_data["Page_4"]["all_kvs"].get("ACORD", "")

        ###############################################################################################################################

        file_name = file_name.split("/")[1].replace(' ', '')

        # Save the modified schema JSON to a new file
        output_file_path = f"acord126_V2014_04/output/{file_name.split('.')[0]}.json"
        # with open(output_file_path, 'w') as output_file:
        #     json.dump(schema_data, output_file, indent=4)

        print(f"Data has been successfully mapped and saved to {output_file_path}")
        return schema_data

    except Exception as e:
        print("Error occured in acord126_mapper", e)
        return "None"