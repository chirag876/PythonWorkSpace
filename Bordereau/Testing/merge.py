import pandas as pd

# Specify the input CSV file path and the output file path
input_csv_path = 'D://Spectral Tech AI//Workspaces//Codespaces//MSIG//Documents//banchmark_output_file.csv'  # Change to the path of your CSV file
output_csv_path = 'D://Spectral Tech AI//Workspaces//Codespaces//MSIG//Documents//updated_banchmark_output_file.csv'  # Change to your desired output path

# Load the existing CSV file
benchmark_df = pd.read_csv(input_csv_path)

# List of new columns to add
new_columns = [
    "MGA", "Program Name", "Issuing Company", "Full policy number",
    "Policy Effective Date", "Policy Expiration Date", "Insured Name",
    "Insured Address", "Insured City", "Insured State", "Insured Zip",
    "Transaction Effective Date", "Transaction Expiration Date", "Premium",
    "Terrorism Premium", "Total Gross Premium including Terrorism",
    "Commission amount", "Net Premium", "Surcharge amount", "Surcharge type",
    "Tax Amount", "Tax Type", "Fee Amount", "Fee Type", "Payment terms",
    "Book or Process Date", "Policy Type", "Transaction Type",
    "Endorsement number", "Primary/Excess Indicator", "Attachment Point",
    "CM/Occ Indicator", "Retroactive date", "Risk/Location #",
    "Risk/Location Address", "Risk/Location City", "Risk/Location State",
    "Risk/Location Zip", "Risk/Location premium", "Technical Price",
    "IRPM (Individual Risk Premium Modification)", "Exposure Type",
    "Exposure Amount", "Policy Occurrence Limit", "Policy Aggregate Limit",
    "SIR/Deductible indicator", "SIR/Deductible amount", "SIR/Deductible type",
    "NAICS or SIC Code", "Annual Statement Line Code",
    "Annual Statement Line Description", "Expiring Policy Number",
    "Issue Date", "Policy Event Number", "Companion policy number",
    "Carrier %", "Carrier Limit", "Broker/Agent", "Broker/Agent Address",
    "Broker/Agent City", "Broker/Agent State", "Broker/Agent Zip",
    "Direct/Assumed", "Fac?", "Fac Reinsurance Attachment point",
    "Ceded Fac Reinsurance Carrier", "Ceded Premium to Fac Reinsurance",
    "Certificate number", "Coverage Ceded to Fac Reinsurer", "Home State",
    "SL Tax Broker Company", "SL Tax Broker Name", "SL Tax Broker Address",
    "SL Broker City", "SL Broker State", "SL Broker Zip", "SL License Number",
    "NJ Transaction Number", "Coverage Code", "Coverage Sub Code",
    "CA Limit", "MTC Limit", "APD Limit", "CA Deductible Amount",
    "MTC Deductible Amount", "APD Deductible Amount", "Rating Class Code",
    "Fleet Indicator", "Fleet size", "Hired Car", "Non Owned",
    "Drive Other Car", "Vehicle Number", "Coverage Symbol", "Cost New",
    "Vehicle Body Type", "Vehicle Type", "Radius Of Use", "Business Use Class",
    "Gross Vehicle Weight", "Vehicle Make", "Vehicle Model", "Model Year",
    "Axel count", "Vehicle Identification Number", "Tractor GCW", "Cost of Hire",
    "Specialized Vehicle Type", "Vehicle Number of Seats, Seating Capacity",
    "Occupancy", "Class Code", "Class Code Description", "100% Limit",
    "Building Value", "Coinsurance", "Building Valuation", "Agreed Value",
    "Contents Value", "BI/Rental Income Value", "Other Structure Limit", "TIV",
    "Construction", "Year Built", "# of Stories", "Square Footage",
    "AOP Deductible", "AOP Limit", "Flood Limit", "Flood % Deductible",
    "Flood Deducible", "Flood Zone", "Earthquake Limit",
    "Earthquake % Deductible", "Earthquake Deductible", "Earthquake Zone",
    "Wind Limit", "Wind Deductible", "Wind % Deducible",
    "Equipment Breakdown Limit", "Equipment Breakdown Deductible",
    "Protection Class", "100% Smoke Detectors", "Sprinkler Protection Type Code",
    "Percentage of sprinkler coverage", "Breach of Privacy Event",
    "Data and software loss", "Network service failure liabilities",
    "Business interruption", "Contingent Business Interruption",
    "Incident Response Costs", "Regulatory and defense coverage",
    "product and operations liability", "liability (Tech E&O)",
    "Liability (Professional Services)", "Liability (Directors and Officers)",
    "Media", "Financial Theft and fraud", "Reputational Damages",
    "Cyber Extortion", "Intellectual Property Theft",
    "Damage to Premises Rented to you Limit", "Medical Expense Limit Included",
    "Medical Expense Limit", "Personal and Advertising Injury Limit",
    "Products/Completed Operations Aggregate Limit", "2nd Layer Deductible - Per Occurrence",
    "2nd Layer Deductible Aggregate", "Stop Gap Limit", "Employee Benefits Limit",
    "Rate Per Member"
]

# Add new columns if they do not exist
for column in new_columns:
    if column not in benchmark_df.columns:
        benchmark_df[column] = None  # Use None to ensure the datatype is inferred correctly

# Save the updated DataFrame back to CSV
benchmark_df.to_csv(output_csv_path, index=False)

print(f"Updated CSV file saved to: {output_csv_path}")
