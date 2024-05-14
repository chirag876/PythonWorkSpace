import pandas as pd
import numpy as np
from faker import Faker

fake = Faker()

# Set the random seed for reproducibility
np.random.seed(42)

# Generate random data for the insurance dataset
num_records = 1000

# Generate customer information
customer_ids = range(1, num_records + 1)
customer_names = [fake.name() for _ in range(num_records)]

# Generate policy information
policy_ids = range(1001, num_records + 1001)
policy_types = ['General Liability'] * num_records
policy_premiums = np.random.uniform(1000, 10000, num_records)

# Generate policy durations
policy_start_dates = pd.date_range(start='2020-01-01', periods=num_records, freq='M')
policy_end_dates = policy_start_dates + pd.DateOffset(years=1)

# Generate renewal information
renewal_dates = policy_end_dates + pd.DateOffset(days=1)
renewal_premiums = policy_premiums * np.random.uniform(0.95, 1.05, num_records)

# Generate other columns
number_of_employees = np.random.randint(1, 100, num_records)
business_industries = ['Construction', 'Retail', 'Manufacturing', 'Technology', 'Consulting']
annual_revenues = np.random.randint(100000, 10000000, num_records)
payment_methods = ['Credit Card', 'Cheque', 'ACH Transfer']
claims_count = np.random.randint(0, 5, num_records)
duration_in_months = [12] * num_records

# Generate churn labels
churn_labels = np.random.choice([0, 1], num_records, p=[0.5, 0.5])
#churn_labels = None

# Create the dataframe
data = pd.DataFrame({
    'CustomerID': customer_ids,
    'CustomerName': customer_names,
    'PolicyID': policy_ids,
    'PolicyType': policy_types,
    'PolicyPremium': policy_premiums,
    #'PolicyStartDate': policy_start_dates,
    #'PolicyEndDate': policy_end_dates,
    #'RenewalDate': renewal_dates,
    'RenewalPremium': renewal_premiums,
    'NumberOfEmployees': number_of_employees,
    'BusinessIndustry': np.random.choice(business_industries, num_records),
    'AnnualRevenue': annual_revenues,
    'PaymentMethod': np.random.choice(payment_methods, num_records),
    'ClaimsCount': claims_count,
    'DurationInMonths': duration_in_months,
    'Churn': churn_labels
})

# Save the dataset to a CSV file
data.to_csv('C:\WorkSpaces\CodeSpaces\DataGenerator\Insurance Data Generator\csv\Renewal\policy_renewal_prediction_dataset_training.csv', index=False)
