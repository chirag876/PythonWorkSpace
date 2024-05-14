import pandas as pd
import numpy as np
import datetime
from faker import Faker
from datetime import datetime, timedelta
import json

fake = Faker()

# Set the random seed for reproducibility
np.random.seed(42)

# Generate random data for the insurance dataset
#num_records = 1144681
num_records = 1000

# Generate customer information
#quote_ids = ['Q' + str(i) for i in range(1001, num_records + 1001)]
#claim_ids = ['C' + str(i) for i in range(1001, num_records + 1001)]
customer_ids = range(1, num_records + 1)
customer_names = [fake.name() for _ in range(num_records)]
given_Name=[]
surname=[]

for full_name in customer_names:
    components = full_name.split()
    given_Name.append(components[0])
    surname.append(components[-1])

# Generate policy information
policy_ids = range(1001, num_records + 1001)
line_of_business = np.random.choice(['General Liability', 'Workers Compensation',
                                     'Professional Liability', 'Product Liability', 'Automobile Liability'], num_records)
#number=['POLICY987654321']* num_records
claims_count = np.random.randint(0, 10, num_records)

total_premium = np.round(np.random.uniform(1000, 1000000, num_records), 2)

claim_Amount = [np.round(premium - 500, 2) if count != 0 else 0 for count, premium in zip(claims_count, total_premium)]

# Generate policy durations
#original_Effective_Date=['2022-11-04'] * num_records
policy_effective_dates = datetime(pd.date_range(start ='1960-1-1',periods = 1000, freq ='D'))
#policy_effective_dates = pd.date_range(start ='1-1-1960',end ='8-01-2090', freq ='H')
policy_expiration_dates = datetime(policy_effective_dates + pd.DateOffset(years=1))

# print(policy_effective_dates[0].strftime('%Y-%m-%d'))
print(len(policy_expiration_dates))


# Generate renewal information
renewal_premiums = np.round(total_premium * np.random.uniform(0.95, 1.05, num_records), 2)

# Generate cancellation dates between policy start and end dates
# Set some cancellation dates as null (None)
# cancellation_dates = [
#     fake.date_between_dates(policy_effective_dates, policy_expiration_dates) if np.random.choice(
#     [True, False]) else None for policy_effective_dates, policy_expiration_dates in zip(policy_effective_dates, policy_expiration_dates)
# ]

cancellation_dates = [
    datetime(fake.date_between_dates(datetime(policy_effective_dates[i]), datetime(policy_expiration_dates[i]))
    if np.random.choice([True, False]) else None
    for i in range(num_records))
]


# Generate renewal_dates
# Set some renewal_dates as null (None)
renewal_dates = [
    datetime(policy_expiration_dates[i] +
    pd.DateOffset(days=1) if np.random.choice([True, False]) else None
    for i in range(num_records))
]

# Generate other columns
number_of_employees = np.random.randint(1, 100, num_records)
business_industries = np.random.choice(['Construction', 'Retail','Manufacturing', 'Technology', 'Consulting'], num_records)
annual_revenues = np.round(np.random.uniform(100000, 10000000, num_records), 2)
payment_methods = np.random.choice(['Credit Card', 'Cheque', 'ACH Transfer', 'Cash', 'Online'], num_records)

#duration_in_months = [12, 24, 36, 48, 60] 
#parent_Entity_Id=['ENTITY456'] * num_records
#parent_Entity_Type_Name=['Business'] * num_records
#status_Code =['ACTIVE'] * num_records
cancellation_reason_description= np.random.choice(['Cancellation due to non-payment','Cancellation due to another carrer', 'Cancellation due to unfulfillment of obligations under the policy agreement.', 'Cancellation due to company bankruptcy', 'Cancellation due to significant changes in risk'],num_records)   

controlling_State_Or_ProvinceCode= np.random.choice(['NY', 'TX', 'CA', 'FL', 'PA'], num_records)

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

cancellation_reason_description = [reason if date is not None else '' for reason, date in zip(cancellation_reason_description, cancellation_dates)]

status_Code = ['INACTIVE' if date is not None else 'ACTIVE' for date in cancellation_dates]

# print(renewal_dates)

#Update renewal status based on cancellation and renewal dates (for training dataset)
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
    'customerId': customer_ids,
    'customerName': customer_names,
    'givenName':given_Name,
    'surname':surname,
    'controllingStateOrProvinceCode': controlling_State_Or_ProvinceCode,
    'id': policy_ids,
    'lineOfBusinessCode': line_of_business,
    'totalPremium': total_premium,
    'effectiveDate': pd.to_datetime(policy_effective_dates),
    'cancellationDate':pd.to_datetime(cancellation_dates),
    'expirationDate': pd.to_datetime(policy_expiration_dates),
    'RenewalDate': pd.to_datetime(renewal_dates),
    'status_Code': status_Code,
    'cancelReasonDescription':cancellation_reason_description,
    'renewalPremium': renewal_premiums,
    'numberOfEmployees': number_of_employees,
    'businessIndustry': business_industries,
    'annualRevenue': annual_revenues,
    'paymentMethod': payment_methods,
    'claimsCount': claims_count,
    'claimAmount':claim_Amount,
    'RenewalStatus': renewal_status
})

# Save the dataset to a CSV file
data.to_csv('C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\csv\PolicyDataExtraction\V1_train.csv', index=False)