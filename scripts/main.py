# Imports
from extract import extract_data
from load import transform_and_load
from generate_report import generate_report_and_send
from report import *
import os
import time


# 1. Extract data from API and save to parquet file
print("Extracting data from API...")

# Extract data from API and save to parquet file
extract_data(days=[-30, -7, 0],
             n=300)

# 2. Transform data and save to parquet file
print("\n")
print("Preparing to transform and load data...")

# Read the current directory for parquet files
files = [f for f in os.listdir("./") if f.endswith(".parquet")]

# Transform data and save to parquet file
transform_and_load(files=files)

# 3. Generate report and send email
print("\n")
print("Data transformed and loaded...")
time.sleep(1)
print("Finding optimal prices for products...")
time.sleep(1)
print("Generating report and sending email...")


# Generate report
generate_report_and_send(recipient_email = os.environ.get("RECIPIENT_EMAIL"), 
                         sender_email = os.environ.get("SENDER_EMAIL"), 
                         password = os.environ.get("EMAIL_PASSWORD"))

# 4. Delete parquet files
print("\n")
print("Deleting parquet files...")

# delete parquet files
for f in os.listdir("./"):
    if f.endswith(".parquet"):
        os.remove(f)

print("\n")
print("All done...")


"""Main script for the data pipeline."""