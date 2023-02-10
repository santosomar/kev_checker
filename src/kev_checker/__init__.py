#!/usr/bin/env python3
# Author: Omar Santos @santosomar
# This script retrieves CISA's KEV data and processes the data using pandas

import argparse
import pandas as pd
import requests
from datetime import timedelta


def main():
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

    # Convert the dateAdded field to a datetime object
    df["dateAdded"] = pd.to_datetime(df["dateAdded"])

    # Make a copy of the original case of the columns
    df_original_case = df.copy()

    # Make the columns case-insensitive
    df["cveID"] = df["cveID"].str.lower()
    df["vendorProject"] = df["vendorProject"].str.lower()
    df["product"] = df["product"].str.lower()

    # Use argparse to parse the command line arguments
    parser = argparse.ArgumentParser(description='Retrieve and process CISA KEV data.')

    parser.add_argument('search', type=str, help='The search term to use. Can be a cveID, vendorProject, product, or a time range in the format "YYYY-MM-DD:YYYY-MM-DD".')

    args = parser.parse_args()

    # Get the search term from the arguments and make it case-insensitive
    search_input = args.search.lower()

    # Split the input into two parts, separated by a colon
    search_input_parts = search_input.split(":")

    # Check if the input is a time range
    if len(search_input_parts) == 2:
        # Get the start and end date from the input
        start_date = search_input_parts[0]
        end_date = search_input_parts[1]

        # Filter the DataFrame to only include rows where the dateAdded is within the time range
        filtered_df = df[(df["dateAdded"] >= start_date) & (df["dateAdded"] <= end_date)]

    else:
        # Filter the DataFrame to only include rows where the cveID, vendorProject, or product contains the input
        filtered_df = df[(df["cveID"] == search_input) | (df["vendorProject"] == search_input) | (df["product"].str.contains(search_input))]

    # Get the original case of the filtered records
    filtered_df_original_case = df_original_case.loc[filtered_df.index]

    # Set the display option to show all rows
    pd.options.display.max_rows = None

    # Print the filtered records with the original case
    print(filtered_df_original_case[["cveID", "vendorProject", "product"]])


if __name__ == '__main__':
    main()
