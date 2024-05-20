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

#check if input name contains only alphabetical characters
def name_validation(name):
    return name.isalpha() if name else True

def company_name_validation(company_name):
    return len(company_name) > 0 if company_name else True

#check if the email address is in the correct format
def email_validation(email):
    return re.match(r"[^@]+@[^@]+\.[^@]+", email) if email else True


def role_validation(role):
    return role.isalpha() if role else True

#check if status is one of the accepted values
def status_validation(status):
    return status in ["qualified", "unqualified", ""] #allows empty status for incomplete rows


#prompt for confirmation before adding the lead
def confirmation_validation(prompt:str, feedback:str):
    while True:
        confirmation = input(prompt).upper()
        if confirmation == "Y":
            break
        if confirmation == "N":
            print(feedback)
            exit()
        print("Invalid input, enter Y or N")