from colorama import init, Fore
import csv
from lead import Lead
import validations
import data_operations

init()

def visual_seperator():
    print("\n\n")

#menu options
def display_options():
    print("\n Lightning CRM for Sales [Menu]")
    print("1 > Check lead ownership")
    print("2 > Add new lead")
    print("3 > Remove lead")
    print("4 > Modify lead details")
    print("5 > Display all leads")
    print("6 > Search lead list")
    print("7 > Exit")

def main():
    lead_database = "leads_appdatabase.py"

#select menu option
    while True:
        display_options()
        choice = input("Enter Menu Option Number: ")

#Option 1: Check if a lead is already assigned to sales person

        if choice == "1":
            company_url = input("Enter the URL (in http:// or https:// format): ")
            if validations.url_exists(company_url, lead_database):
                print("Lead is already assigned")
            else:
                print("Lead is available to be assigned")
                
#Option 2: Add a new lead
        elif choice == "2":
            company_url = input("Enter company URL: ")
            company_name = input("Enter company name: ")
            name = input("Enter lead's name (optional): ")
            role = input("Enter lead's role (optional): ")
            email = input("Enter lead's email (optional): ")
            assigned_to = input("Enter lead owner's name: ")
            status = input("Enter lead status (qualified/unqualified) (optional): ")
            
        







#Option 3: Remove a lead

#Option 4: Modify existing lead details

#Option 5: Display all the leads

#Option 6: Search the lead list

#Option 7: Exit

