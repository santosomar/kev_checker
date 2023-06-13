![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Python versions](https://img.shields.io/pypi/pyversions/danger-python) ![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)

# KEV Checker
The KEV Checker is a tool created by Omar Santos designed to retrieve and efficiently process the most up-to-date [CISA's Known Exploited Vulnerabilities (KEV)](https://www.cisa.gov/known-exploited-vulnerabilities-catalog) data. The data is processed using the `pandas` library.

By leveraging the KEV Checker, users can effortlessly access critical information regarding known vulnerabilities that have been exploited. The tool fetches the latest KEV data from CISA, and it can beused to streamline the data processing workflow with other vulnerability management tools. 

## Main Requirements
- Python 3
- pandas
- requests
- argparse

## Installation

```
pip3 install kev-checker
```

### Make an editable install if you want to make changes/enhancements to the code

```
git clone https://github.com/santosomar/kev_checker
cd kev_checker
pip3 install --upgrade -e .
```

## Usage
```
kev-checker <search>
```
`<search>` can be either:
- a CVE ID in the format "CVE-YYYY-NNNNN"
- a vendor or open source project
- a product name (keyword search)
- or a date range in the format "YYYY-MM-DD:YYYY-MM-DD".

All input is case insensitive.    


## Examples

### CVE ID
This command will retrieve and process the KEV data, and output all records that have a "cveID" field that matches "CVE-2023-21674".

```
kev-checker CVE-2023-21674
```

Output:
```
              cveID vendorProject  product  dateAdded
869  CVE-2023-21674     Microsoft  Windows 2023-01-10
```

### Vendor or Open Source Project
This command will retrieve and process the KEV data, and output all records that have a "vendorProject" field that matches "Microsoft".

```
kev-checker openssl
```

Output:
```
             cveID vendorProject  product  dateAdded
658  cve-2014-0160       openssl  openssl 2022-05-04
```

### Product
This command will retrieve and process the KEV data, and output all records that have a "product" field that matches "Cisco IOS XR products".

```
kev-checker "IOS XR"
```

Output:
```
              cveID vendorProject product
59    CVE-2020-3118         Cisco  IOS XR
60    CVE-2020-3566         Cisco  IOS XR
61    CVE-2020-3569         Cisco  IOS XR
564   CVE-2010-3035         Cisco  IOS XR
566   CVE-2009-2055         Cisco  IOS XR
662  CVE-2022-20821         Cisco  IOS XR
```

### Time Range
This command will retrieve and process the KEV data, and output all records that have a "dateAdded" field within the range of January 1, 2023 to December 31, 2023.
```
kev-checker 2023-01-01:2023-12-31
```

Output:
```
              cveID vendorProject                               product  dateAdded
868  CVE-2022-41080     Microsoft                       Exchange Server 2023-01-10
869  CVE-2023-21674     Microsoft                               Windows 2023-01-10
870  CVE-2022-44877           CWP                     Control Web Panel 2023-01-17
871  CVE-2022-47966          Zoho                          ManageEngine 2023-01-23
872  CVE-2017-11357       Telerik  User Interface (UI) for ASP.NET AJAX 2023-01-26
873  CVE-2022-21587        Oracle                      E-Business Suite 2023-02-02
874  CVE-2023-22952      SugarCRM                     Multiple Products 2023-02-02
```


