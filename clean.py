
print("--- Exercise 1 ---")

import pandas as pd

df = pd.read_csv("data/messy_sales.csv")

print(df.info())

print(df.isnull().sum())

#1.) The customer ID has 362 missing values.
#2.) The Order ID has 31 missing values.
#3.) The unit price is being stored as a string instead of a numeric data type.

print("--- Exercise 2 ---")

df.columns = df.columns.str.lower().str.replace(" ", "_")

print(df.columns.tolist())

print("--- Exercise 3 ---")

print("Shape before:", df.shape)
#save original shape to compare later.
df = df.dropna(subset=["customer_id", "order_id"])
#drop the rows with missing values in the customer_id and order_id columns.
print("Shape after:", df.shape)

df["quantity_sold"] = df["quantity_sold"].fillna(df["quantity_sold"].mean())
#Filling the missing quantity_sold values with the column mean because
# quantity_sold is numeric and has relatively few missing values.

print("--- Exercise 4 ---")

df["order_date"] = pd.to_datetime(df["order_date"], errors="coerce")

print("Dates converted to NaT:", df["order_date"].isna().sum())

df["unit_price"] = df["unit_price"].str.replace("$", "", regex=False)

df["unit_price"] = df["unit_price"].str.replace(",", "", regex=False)

df["unit_price"] = df["unit_price"].astype(float)

df["quantity_sold"] = df["quantity_sold"].astype(int)

df["revenue"] = (df["unit_price"] * df["quantity_sold"]).round(2)

print(df.dtypes)