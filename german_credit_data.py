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
amount_capped=german_credit_data["Credit amount"].quantile(0.)
print (amount_capped)

#Find the average Credit amount for each Purpose, rounded to 2 decimals, largest first.
print (german_credit_data.groupby("Purpose")["Credit amount"].mean(). round (2).sort_values(ascending=False))

#For each Housing type, find the count, mean, minimum and maximum Credit amount using agg().
print(german_credit_data.groupby("Housing")["Credit amount"].agg(["mean","min","max"]). round(1)
)
# For each Purpose, find the number of loans, average Duration and average Credit amount, using named outputs.
print(german_credit_data.groupby("Purpose").agg(

 loans=("Credit amount", "count"),
 avg_duration=("Duration", "mean"),
 avg_amount=("Credit amount", "mean")).round(1))


             # numpy

#Convert the Credit amount column into a numpy array called amounts. Print its type, shape and first 5 values.

amounts = german_credit_data["Credit amount"].to_numpy()
print(type(amounts), amounts.shape)
print(amounts[:5])

#Using numpy functions, find the mean, median, standard deviation, minimum and maximum of amounts.
print(np.mean(amounts), np.median(amounts), np.std(amounts))

print(np.min(amounts), np.max(amounts))


#Find the 25th, 50th, 75th and 90th percentiles of amounts
print(np.percentile(amounts, [25, 50, 75, 90]))

#How many loans are above the mean amount? What percentage of all loans is that?
above= amounts>amounts.mean()
print(above.sum())
print(round(above.mean()*100, 2))

#Create a new array with every amount increased by 10% and rounded to the nearest whole number

with_interest = np.round(amounts * 1.10, 0)
print(with_interest[:5])


#Create amount_per_month = Credit amount divided by Duration, and show the first 5 rows of the three columns.
german_credit_data["amount_per_month"]=german_credit_data["Credit amount"] / german_credit_data["Duration"]
print(german_credit_data[["amount_per_month","Credit amount","Duration"]].head())

#Q34. Create risk_tier: High if Credit amount is above 5000, Medium if it is 2000 to 5000, otherwise Low.
import numpy as np
german_credit_data["risk_tier"] = np.where(german_credit_data["Credit amount"] > 5000, "High",
 np.where(german_credit_data["Credit amount"] >= 2000, "Medium", "Low"))
conditions = [german_credit_data["Credit amount"] > 5000, german_credit_data["Credit amount"] >= 2000]
german_credit_data["risk_tier2"] = np.select(conditions, ["High", "Medium"], default="Low")
print(german_credit_data["risk_tier"].value_counts())

#Build a pivot table of the average Credit amount with Housing as rows and Sex as columns.
pt=german_credit_data.pivot_table(index="Housing",columns = "Sex",values="Credit amount", aggfunc="mean")
print(pt)

#Create age_group with pd.cut using the groups 18-25, 26-35, 36-50 and 51+, and count the loans in each.
german_credit_data["age_group"] = pd.cut(german_credit_data["Age"], bins=[17, 25, 35, 50, 120],
 labels=["18-25", "26-35", "36-50", "51+"])
print(german_credit_data["age_group"].value_counts().sort_index())

#Split loans into four equal-sized groups by Credit amount (Q1 to Q4) with pd.qcut, and find the average amount in each.
german_credit_data["amount_quartile"] = pd.qcut(german_credit_data["Credit amount"], 4, labels=["Q1", "Q2", "Q3", "Q4"])
print(german_credit_data.groupby("amount_quartile", observed=True)["Credit amount"].mean().round(0))

#Rank every loan inside its own Purpose by Credit amount (1 = largest)
german_credit_data["rank_in_purpose"] = (german_credit_data.groupby("Purpose")["Credit amount"]
 .rank(ascending=False, method="min"))
show = ["Purpose", "Credit amount", "rank_in_purpose"]
print(german_credit_data.sort_values(["Purpose", "rank_in_purpose"])[show].head(10))


