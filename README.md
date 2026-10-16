# Python Data Analysis Practice: Pandas & NumPy

## About This Repository

This repository documents my learning journey in Python for data analysis. I am currently practicing Pandas and NumPy using a German Credit dataset to develop practical data exploration, manipulation, and numerical analysis skills.

**Project status:** In Progress 🚧

## Tools and Libraries

* Python
* Pandas
* NumPy
* Pydroid 3

## Dataset

I am using a German Credit dataset containing information about loan applicants and their credit details.

The dataset includes fields such as:

* Age
* Credit amount
* Duration
* Housing
* Purpose
* Checking account
* Saving accounts

## Topics Practiced So Far

### 1. Data Loading and Exploration

* Importing Pandas and NumPy
* Reading CSV files
* Displaying the first and last rows
* Generating descriptive statistics
* Inspecting column names and data types
* Checking dataset dimensions and index

### 2. Data Quality Checks

* Identifying missing values
* Checking null values in columns

### 3. Data Selection and Filtering

* Selecting specific columns
* Filtering loans with credit amounts above 5,000
* Practicing conditions for filtering records

### 4. Sorting and Aggregation

* Sorting loan records by credit amount
* Calculating average credit amounts by loan purpose
* Counting records by loan purpose
* Calculating average loan amounts and durations by housing type

## Example Python Code

```python
import pandas as pd
import numpy as np

df = pd.read_csv("german_credit_data.csv")

# Explore the dataset
print(df.head())
print(df.describe())
print(df.shape)
print(df.dtypes)

# Check missing values
print(df.isnull().sum())

# Select specific columns
print(df[["Purpose", "Credit amount", "Age"]])

# Filter loans above 5,000
print(df[df["Credit amount"] > 5000])

# Average credit amount by purpose
print(
    round(
        df.groupby("Purpose")["Credit amount"].mean(),
        2
    )
)

# Summarize loan amount and duration by housing
print(
    df.groupby("Housing").agg(
        avg_amount=("Credit amount", "mean"),
        avg_duration=("Duration", "mean")
    )
)
```

*Note: The filename in the example may need to be changed to match the actual CSV file you use.*

## Learning Objectives

* Improve my Python programming skills.
* Learn to clean and manipulate datasets.
* Develop confidence in data exploration and analysis.
* Apply Pandas and NumPy to practical datasets.
* Build a portfolio to demonstrate my progress toward becoming a Data Analyst.

## Next Steps

* Practice handling missing values and duplicate records.
* Create calculated columns.
* Learn more NumPy functions and array operations.
* Perform deeper exploratory data analysis.
* Answer business questions using the dataset.
* Document findings and insights.

## Project Status

This repository is a work in progress. I will continue updating it as I learn new techniques and complete additional exercises.

Thank you for visiting my repository!

**Skills in progress:** Python | Pandas | NumPy | Data Analysis
