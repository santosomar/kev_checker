#!/usr/bin/env python3
# Author: Omar Santos @santosomar
# This script retrieves CISA's KEV data and processes the data using pandas

import pandas as pd
import requests
from datetime import timedelta


# CISAs Known Exploited Vulnerabilities (KEV) CSV file URL
url = "https://www.cisa.gov/sites/default/files/csv/known_exploited_vulnerabilities.csv"

# Download the CSV file
response = requests.get(url)

# Write the contents of the response to a local file
with open("known_exploited_vulnerabilities.csv", "wb") as f:
    f.write(response.content)

# Read the local CSV file into a DataFrame
# I can process the data directly from the URL, but I prefer to download the file
# and process it locally because in the future it may grow significantly in size
df = pd.read_csv("known_exploited_vulnerabilities.csv")

# Perform some processing on the data
# Get the column names
column_names = df.columns

# print("Field names:", column_names)

# Convert the dateAdded field to a datetime object
df["dateAdded"] = pd.to_datetime(df["dateAdded"])

# Get the current date
current_date = pd.Timestamp.now().date()

# Calculate the date 15 days ago
fifteen_days_ago = current_date - timedelta(days=15)

# Select the rows where dateAdded is greater than or equal to 15 days ago
new_records = df[df["dateAdded"].dt.date >= fifteen_days_ago]

# Print the new records
print(new_records[["cveID", "vendorProject", "product"]])




