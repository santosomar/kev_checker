![Python versions](https://img.shields.io/pypi/pyversions/danger-python)

# KEV Checker
his script retrieves and processes the Known Exploited Vulnerabilities (KEV) data from the CISA website. The data is stored in a CSV file and is processed using the pandas library.

## Requirements
- Python 3
- pandas
- requests
- argparse

## Usage
```
python3 kev_data_processing.py <search>
<search> can be either a cveID, vendorProject, product, or a time range in the format "YYYY-MM-DD:YYYY-MM-DD".
```     

## Output
The script outputs the filtered records that match the search term, including the "cveID", "vendorProject", "product", and "dateAdded" columns.

## Example
```
python3 kev_data_processing.py 2023-01-01:2023-12-31
```

This command will retrieve and process the KEV data, and output all records that have a "dateAdded" field within the range of January 1, 2023 to December 31, 2023.
