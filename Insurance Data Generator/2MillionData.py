import pandas as pd
import numpy as np
from faker import Faker

import json

fake = Faker()

# Set the random seed for reproducibility
np.random.seed(42)

# Generate random data for the insurance dataset
num_records = 1148599

# Generate customer information
quote_ids = ['Q' + str(i) for i in range(1049577, num_records + 1049577)]
claim_ids = ['C' + str(i) for i in range(1049577, num_records + 1049577)]
customer_ids = range(1049577, num_records + 1049577)
customer_names = [fake.name() for _ in range(num_records)]
given_Name=[]
surname=[]

for full_name in customer_names:
    components = full_name.split()
    given_Name.append(components[0])
    surname.append(components[-1])

# Generate policy information
policy_ids = range(1049577, num_records + 1049577)
line_of_business = ['General Liability'] * num_records
number=['POLICY987654321']* num_records
total_premium = np.round(np.random.uniform(1000, 1000000, num_records), 2)
claim_Amount=np.round(total_premium-500,2)

# Generate policy durations
original_Effective_Date=['2022-11-04'] * num_records
policy_effective_dates = pd.date_range(start ='1-1-1960',end ='8-01-2090', freq ='H')
policy_expiration_dates = policy_effective_dates + pd.DateOffset(years=1)
print(len(policy_expiration_dates))


# Generate renewal information
renewal_premiums = np.round(total_premium * np.random.uniform(0.95, 1.05, num_records), 2)

# Generate cancellation dates between policy start and end dates
# Set some cancellation dates as null (None)
cancellation_dates = [
    fake.date_between_dates(policy_effective_dates, policy_expiration_dates) if np.random.choice(
    [True, False]) else None for policy_effective_dates, policy_expiration_dates in zip(policy_effective_dates, policy_expiration_dates)
]

# Generate renewal_dates
# Set some renewal_dates as null (None)
renewal_dates = [
    policy_expiration_dates[i] +
    pd.DateOffset(days=1) if np.random.choice([True, False]) else None
    for i in range(num_records)
]

# Generate other columns
number_of_employees = np.random.randint(1, 100, num_records)
business_industries = ['Construction', 'Retail','Manufacturing', 'Technology', 'Consulting']
annual_revenues = np.round(np.random.uniform(100000, 10000000, num_records), 2)
payment_methods = ['Credit Card', 'Cheque', 'ACH Transfer']
claims_count = np.random.randint(0, 2, num_records)
duration_in_months = [12] * num_records
parent_Entity_Id=['ENTITY456'] * num_records
parent_Entity_Type_Name=['Business'] * num_records
status_Code =['ACTIVE'] * num_records
cancellation_reason_description=['Cancellation due to non-payment'] * num_records
controlling_State_Or_ProvinceCode=['NY'] * num_records

# Generate renewal status labels
renewal_status = np.random.choice([0, 1], num_records, p=[0.2, 0.8])

# Generate cancellation and renewal information
cancellation_dates = []
renewal_dates = []

for i in range(num_records):
    cancellation_date = None
    renewal_date = None

    # Generate cancellation date if not generating renewal date
    if np.random.choice([True, False]):
        cancellation_date = fake.date_between_dates(
            policy_effective_dates[i], policy_expiration_dates[i])
    else:
        renewal_date = policy_expiration_dates[i] + pd.DateOffset(days=1)

    cancellation_dates.append(cancellation_date)
    renewal_dates.append(renewal_date)

# Update renewal status based on cancellation and renewal dates (for training dataset)
for i in range(num_records):
    if cancellation_dates[i] and not renewal_dates[i]:
        renewal_status[i] = 0
    elif not cancellation_dates[i] and renewal_dates[i]:
        renewal_status[i] = 1
    elif cancellation_dates[i] and renewal_dates[i]:
        renewal_status[i] = 0  # Update as per your requirement

# For generating testing dataset
# renewal_status = None

# Create the dataframe
data = pd.DataFrame({
    'quoteId': quote_ids,
    'claimId': claim_ids,
    'customerId': customer_ids,
    'customerName': customer_names,
    'givenName':given_Name,
    'surname':surname,
    'cancelReasonDescription':cancellation_reason_description,
    'controllingStateOrProvinceCode': controlling_State_Or_ProvinceCode,
    'id': policy_ids,
    'statusCode':status_Code,
    'parentEntityId':parent_Entity_Id,
    'parentEntityTypeName':parent_Entity_Type_Name,
    'lineOfBusinessCode': line_of_business,
    'number':number,
    'totalPremium': total_premium,
    'effectiveDate': policy_effective_dates[:num_records],
    'originalEffectiveDate':original_Effective_Date,
    'cancellationDate': cancellation_dates,
    'expirationDate': policy_expiration_dates[:num_records],
    'RenewalDate': renewal_dates,
    'renewalPremium': renewal_premiums,
    'numberOfEmployees': number_of_employees,
    'businessIndustry': np.random.choice(business_industries, num_records),
    'annualRevenue': annual_revenues,
    'paymentMethod': np.random.choice(payment_methods, num_records),
    'claimsCount': claims_count,
    'claimAmount':claim_Amount,
    'durationInMonths': duration_in_months,
    'RenewalStatus': renewal_status
})

# Save the dataset to a CSV file
data.to_csv('C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\csv\PolicyDataExtraction\V1_policy_data_extraction_train1.csv')
# out = data.to_json(orient='records')[1:-1].replace('},{', '} {')
# with open('file_name.json', 'w') as f:
#     f.write(out)

