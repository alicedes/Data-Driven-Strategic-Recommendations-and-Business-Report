import pandas as pd


gcc = pd.read_csv("german credit card_better.csv")


mapping = {
    1: "less than 0 DM",
    2: "between 0 and 200 DM",
    3: "more than 200 DM",
    4: "no checking account"
}

# Replace the numeric values in the DataFrame with descriptions
gcc['checking'] = gcc['checking'].replace(mapping)

mapping = {
    0: "no credits taken/ all credits paid back duly",
    1: "all credits at this bank paid back duly",
    2: "existing credits paid back duly till now",
    3: "delay in paying off in the past",
    4: "critical account/ other credits existing"
}

# Replace the numeric values in the DataFrame with descriptions
gcc['history'] = gcc['history'].replace(mapping)

purpose_mapping = {
    0: "car (new)",
    1: "car (used)",
    2: "furniture/equipment",
    3: "radio/television",
    4: "domestic appliances",
    5: "repairs",
    6: "education",
    8: "retraining",
    9: "business",
    10: "others"
}

# Replace the numeric values in the 'purpose' column with descriptions
gcc['purpose'] = gcc['purpose'].replace(purpose_mapping)

new_column_names = {'checking': 'AccountStatus',
                    'duration': 'Duration',
                    'history': 'CreditHistory',
                    'purpose': 'Purpose',
                    'amount': 'CreditAmount',
                    'savings': 'Account',
                    'employed': 'EmploymentSince',
                    'installp': 'PrecentOfIncome',
                    'marital': 'PersonalStatus',
                    'coapp': 'OtherDebtors',
                    'resident': 'ResidenceSince',
                    'property': 'Property',
                    'age': 'Age',
                    'other': 'OtherInstallPlans',
                    'housing': 'Housing',
                    'existcr': 'NumExistingCredits',
                    'job': 'Job',
                    'depends': 'NumMaintenance',
                    'telephon': 'Telephone',
                    'foreign': 'ForeignWorker',
                    'good_bad': 'GoodCredit'}

# Rename the columns
gcc.rename(columns=new_column_names, inplace=True)

mapping = {
    1: "less than 100 DM",
    2: "between 100 and 500 DM",
    3: "between 500 and 1000 DM",
    4: "more than 1000 DM",
    5: "unknown/ no savings account"
}

# Replace the numeric values in the 'Account_Description' column with descriptions
gcc['Account'] = gcc['Account'].replace(mapping)


employment_mapping = {
    1: "unemployed",
    2: "less than 1 year",
    3: "between 1 and 4 years",
    4: "between 4 and 7 years",
    5: "more than 7 years"
}

# Replace the numeric values in the 'EmploymentSince' column with descriptions
gcc['EmploymentSince'] = gcc['EmploymentSince'].replace(employment_mapping)

personal_status_mapping = {
    1: "male - divorced/separated",
    2: "female - divorced/separated/married",
    3: "male - single",
    4: "male - married/widowed",
    5: "female - single"
}

# Replace the numeric values in the 'PersonalStatus' column with descriptions
gcc['PersonalStatus'] = gcc['PersonalStatus'].replace(personal_status_mapping)


other_debtors_mapping = {
    1: "none",
    2: "co-applicant",
    3: "guarantor"
}

# Replace the numeric values in the 'OtherDebtors' column with descriptions
gcc['OtherDebtors'] = gcc['OtherDebtors'].replace(other_debtors_mapping)


property_mapping = {
    1: "real estate",
    2: "building society savings agreement/ life insurance",
    3: "car or other, not in attribute Account",
    4: "unknown / no property"
}

# Replace the numeric values in the 'Property' column with descriptions
gcc['Property'] = gcc['Property'].replace(property_mapping)

install_plans_mapping = {
    1: "bank",
    2: "stores",
    3: "none"
}

# Replace the numeric values in the 'OtherInstallPlans' column with descriptions
gcc['OtherInstallPlans'] = gcc['OtherInstallPlans'].replace(install_plans_mapping)


housing_mapping = {
    1: "rent",
    2: "own",
    3: "for free"
}

# Replace the numeric values in the 'Housing' column with descriptions
gcc['Housing'] = gcc['Housing'].replace(housing_mapping)

job_mapping = {
    1: "unemployed/ unskilled - non-resident",
    2: "unskilled - resident",
    3: "skilled employee / official",
    4: "management/ self-employed/highly qualified employee/ officer"
}

# Replace the numeric values in the 'Job' column with descriptions
gcc['Job'] = gcc['Job'].replace(job_mapping)

telephone_mapping = {
    1: "no",
    2: "yes"
}

# Replace the numeric values in the 'Telephone' column with descriptions
gcc['Telephone'] = gcc['Telephone'].replace(telephone_mapping)


foreign_worker_mapping = {
    1: "yes",
    2: "no"
}

# Replace the numeric values in the 'ForeignWorker' column with descriptions
gcc['ForeignWorker'] = gcc['ForeignWorker'].replace(foreign_worker_mapping)

print(gcc.shape)
print(gcc.columns)

gcc.to_csv('gcc_data_processed.csv', index=False)
