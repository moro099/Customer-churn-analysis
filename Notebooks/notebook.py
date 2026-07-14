import pandas as pd
import numpy as np
df = pd.read_excel("C:\\Users\\ketan\\Desktop\\DA Project2.0\\Telco_customer_churn.xlsx")
df.head()
df.info()   
df.shape

# basic data checks
print(df.isnull().sum())
print(df.duplicated().sum())
df["Churn Reason"] = df["Churn Reason"].fillna("Not Churned")
print(df.head())
print(df.iloc[2000:2050])

print(df.describe())
df['Total Charges'] = pd.to_numeric(df['Total Charges'], errors='coerce')
print(df.isnull().sum())

df["Total Charges"] = df["Total Charges"].fillna(0)
print(df.isnull().sum())


# creating churn flag
df["Churn Flag"] = df["Churn Value"].map({"Yes": 1, "No": 0})

# creating tenure groups
def tenure_group(Tenure):
    if Tenure <= 12:
        return '0-12 Months'
    elif Tenure <= 24:
        return '13-24 Months'
    elif Tenure <= 48:
        return '25-48 Months'
    else:
        return '49+ Months'

df['TenureGroup'] = df['Tenure Months'].apply(tenure_group)

#Create Monthly Charges Band
def monthly_charge_band(charge):
    if charge < 35:
        return 'Low'
    elif charge < 70:
        return 'Medium'
    else:
        return 'High'

df['MonthlyChargeBand'] = df['Monthly Charges'].apply(monthly_charge_band)

#Create Customer Value Segment
def customer_value_segment(total):
    if total < 1000:
        return 'Low Value'
    elif total < 3000:
        return 'Medium Value'
    else:
        return 'High Value'

df['CustomerValueSegment'] = df['Total Charges'].apply(customer_value_segment)
# Revenue at Risk

df['RevenueAtRisk'] = np.where(df['Churn Label'] == 'Yes', df['Monthly Charges'], 0)

#Create Risk Score

df['RiskScore'] = 0

df.loc[df['Contract'] == 'Month-to-month', 'RiskScore'] += 30
df.loc[df['Tenure Months'] <= 12, 'RiskScore'] += 20
df.loc[df['Payment Method'] == 'Electronic check', 'RiskScore'] += 15
df.loc[df['Internet Service'] == 'Fiber optic', 'RiskScore'] += 15
df.loc[df['Tech Support'] == 'No', 'RiskScore'] += 10
df.loc[df['Online Security'] == 'No', 'RiskScore'] += 10

#Risk Category
def risk_category(score):
    if score >= 70:
        return 'High Risk'
    elif score >= 40:
        return 'Medium Risk'
    else:
        return 'Low Risk'

df['RiskCategory'] = df['RiskScore'].apply(risk_category)

print(df.head())

df.to_csv("cleaned_customer_churn.csv", index=False)
df.info()
 
