import pandas as pd
import os

# Locate the CSV file from Task 1
csv_path = os.path.join(
    os.path.dirname(__file__),
    "..",
    "Task1_WebScraping",
    "books.csv"
)

# Load dataset
df = pd.read_csv(csv_path)

print("First 5 Rows:")
print(df.head())

print("\nDataset Information:")
df.info()

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns)

# Clean Price column
df["Price"] = df["Price"].str.replace("£", "", regex=False)
df["Price"] = df["Price"].astype(float)

print("\nAfter Cleaning:")
df.info()

# Statistical Summary
print("\nPrice Statistics:")
print(df["Price"].describe())

print("\nAverage Price:")
print(df["Price"].mean())

print("\nHighest Price:")
print(df["Price"].max())

print("\nLowest Price:")
print(df["Price"].min())

# Rating Analysis
print("\nRating Counts:")
print(df["Rating"].value_counts())

# Availability Analysis
print("\nAvailability Counts:")
print(df["Availability"].value_counts())

# Most Expensive Book
print("\nMost Expensive Book:")
print(df.loc[df["Price"].idxmax()])

# Cheapest Book
print("\nCheapest Book:")
print(df.loc[df["Price"].idxmin()])

# Save cleaned dataset
output_file = os.path.join(
    os.path.dirname(__file__),
    "cleaned_books.csv"
)

df.to_csv(output_file, index=False)

print("\nCleaned dataset saved successfully!")