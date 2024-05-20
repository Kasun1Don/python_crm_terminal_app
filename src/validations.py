import csv
import re

def selection_invalid():
    print("Invalid input, select from displayed options")

def company_url_validation(company_url):
    return company_url.startswith("http://") or company_url.startswith("https://")

#check if a given company url exists in the lead database CSV
def url_exists(company_url, lead_database="leads_appdatabase.csv"):
    with open (lead_database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row ["company_url"] == company_url:
                return True
    return False


