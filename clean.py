
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
print("Shape:", df.shape)

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

print("--- Exercise 5 ---")

print("Duplicate rows:", df.duplicated().sum())

df = df.drop_duplicates()

print("Shape:", df.shape)

print("--- Exercise 6 ---")

print(df.describe())

# The maximum quantity_sold of 9999 is suspiciously high compared to the median of 3.
# This may have beeen a placeholder or data-entry error, not a realistic sale quantity.

# The minimum unit_price is -1634, which is not a sale price.
# It is likely a data-entry error, and should be removed from the dataset.


print("Rows with quantity_sold == 9999:", (df["quantity_sold"] == 9999).sum())

df = df[df["quantity_sold"] != 9999]

print("Shape:", df.shape)

print("--- Exercise 7 ---")

df.to_csv("data/clean_sales.csv", index=False)

clean_df = pd.read_csv("data/clean_sales.csv")
print(clean_df.info())


clean_df = pd.read_csv("data/clean_sales.csv", parse_dates=["order_date"])
print(clean_df.info())
