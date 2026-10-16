import pandas as pd
import numpy as np

german_credit_data=pd.read_csv("/storage/emulated/0/Download/german_credit_data (2).csv")
# remove the old index column if present
german_credit_data= german_credit_data.drop(columns="Unnamed: 0", errors="ignore") 
print(german_credit_data.columns.tolist())
#   How many rows and columns does the dataset have? Store them in two variables, rows and cols.
print(german_credit_data.shape)
#Print the column names and the data type of each column.
print(german_credit_data.columns.tolist())
print(german_credit_data.dtypes)
#Show the first 5 and last 5 rows of only Age, Credit amount and Purpose.
print (german_credit_data[["Age","Credit amount","Purpose"]].head())
print(german_credit_data[["Age","Credit amount","Purpose"]].tail())
#Which columns are numeric and which are text?
print(german_credit_data.info())
#Count the missing values in each column, then show them as a percentage of all rows.
print (german_credit_data.isna().sum())
print((german_credit_data.isna().mean() * 100).round(1))
#List the unique values of Purpose and Housing, and say how many unique Purpose values there are
print(german_credit_data["Purpose"].unique())
print(german_credit_data["Housing"].unique())
print(german_credit_data["Purpose"].nunique())
#Show all loans with a Credit amount above 5000.
print(german_credit_data[german_credit_data["Credit amount"]> 5000])
#Show customers aged 25 to 40 who own their house. Check the Housing values first.
print(german_credit_data["Housing"].nunique())
mask = (german_credit_data["Housing"] == "own") & (german_credit_data["Age"] >= 25) & (german_credit_data["Age"] <= 40)

print(german_credit_data[mask])
#Show loans whose Purpose is car or education, using isin()
print (german_credit_data[german_credit_data["Purpose"].isin(["car","education"])])

#Show customers who do not rent (Housing is not rent)
print(german_credit_data["Housing"]!= "rent")
#Show the 10 largest loans, biggest first
print (german_credit_data.sort_values("Credit amount", ascending=False).head())

#Sort by Duration ascending, and by Credit amount descending inside each Duration.
print (german_credit_data.sort_values(["Duration","Credit amount"], ascending=[True,False]).head(10))

#Use loc to show Age and Purpose for customers older than 60. Use iloc to show the first 5 rows and first 3columns.

print(german_credit_data.loc[german_credit_data["Age"] > 60, ["Age", "Purpose"]])
print (german_credit_data.iloc[:5,:3])
#Fill the missing values in Saving accounts and Checking account with the text unknown, and save the change. Confirm no missing values remain.

german_credit_data["Saving accounts"]= print (german_credit_data["Saving accounts"].fillna("unknown"))
german_credit_data["Checking account"]=print(german_credit_data["Checking account"].fillna("unknown"))
print (german_credit_data.isna().sum())
#Count duplicate rows and remove them

print (german_credit_data.duplicated().sum())
print(german_credit_data.drop_duplicates())
print (german_credit_data.shape)

#Create df_clean, a copy of df with column names in lowercase snake_case (credit_amount,saving_accounts, and so on).

german_credit_data_clean = german_credit_data.copy()

german_credit_data_clean.columns = german_credit_data_clean.columns.str.lower().str.replace(" ", "_")

print(german_credit_data_clean.columns.tolist())
# Convert Purpose, Housing and Sex to the category type and compare memory use before and after(without changing df).
cat_cols=["Purpose","Housing","Sex"]
before =german_credit_data[cat_cols].memory_usage(deep=True).sum()
after = german_credit_data[cat_cols].astype("category").memory_usage(deep=True).sum()

print(before, after)

#Create amount_capped: Credit amount with values above the 99th percentile capped at that value, using clip().


