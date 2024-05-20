from colorama import init, Fore, Style
from lead import Lead
import validations
import data_operations

init()

def visual_seperator():
    print("\n")

#menu options
def display_options():
    print(Fore.BLUE + Style.BRIGHT + "\n LITESPEED CRM for Sales" + Style.RESET_ALL)
    visual_seperator()
    print("[Main Menu]")
    visual_seperator()
    print("1 > Check lead ownership")
    print("2 > Add new lead")
    print("3 > Remove lead")
    print("4 > Modify lead details")
    print("5 > Display all leads")
    print("6 > Search a lead's details")
    print("7 > Exit")
    visual_seperator()

def main():
    lead_database = "leads_appdatabase.csv"

#select menu option
    while True:
        display_options()
        choice = input("Enter Menu Option Number: ")

#Option 1: Check if a lead is already assigned to sales person
        if choice == "1":
            visual_seperator()
            company_url = input("Enter the URL (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            assigned_to = validations.get_assigned_to(company_url, lead_database)
            if assigned_to:
                print(Fore.RED + f"Lead is already assigned to {assigned_to}." + Style.RESET_ALL)
            else:
                visual_seperator()
                print(Fore.GREEN + "This lead is available to be assigned." + Style.RESET_ALL)
                
#Option 2: Add a new lead
        elif choice == "2":
            visual_seperator()
            company_url = input("Company URL (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            company_name = input("Company name: ")
            name = input("Lead's name (optional): ")
            role = input("Lead's role (optional): ")
            email = input("Lead's email (optional): ")
            assigned_to = input("Lead owner's name: ")
            status = input("Lead status [qualified/unqualified] (optional): ")
            

            if not validations.name_validation(name):
                print(Fore.RED + "Invalid - Name must only contain letters." + Style.RESET_ALL)
                continue
            
            if not validations.company_name_validation(company_name):
                print(Fore.RED + "Invalid - Enter company name longer than 0 characters." + Style.RESET_ALL)
                continue
            
            if not validations.company_url_validation(company_url):
                print(Fore.RED + "Invalid - Enter company url in either http:// or https:// format."  + Style.RESET_ALL)
                continue
            
            if not validations.email_validation(email):
                print(Fore.RED + "Invalid - Enter a valid email address." + Style.RESET_ALL)
                continue
            
            if validations.url_exists(company_url, lead_database):
                print(Fore.RED + "Invalid - A lead this URL already exists." + Style.RESET_ALL)
                continue
            
            if not validations.role_validation(role):
                print(Fore.RED + "Invalid - Role must only contain letters." + Style.RESET_ALL)
                continue
            
            if not validations.assigned_to_validation(assigned_to):
                print(Fore.RED + "Invalid - Sales representative name must be only letters" + Style.RESET_ALL)
                continue
            
            if not validations.status_validation(status):
                print(Fore.RED + "Invalid - Enter status 'qualified' or 'unqualified'" + Style.RESET_ALL)
                continue
            
            validations.confirmation_validation(
                "Add lead to database? (Y/N): ",
                "Lead not created"
            )

            new_lead = Lead(name, company_name, company_url, email, role, assigned_to, status)
            data_operations.insert_lead(new_lead.__dict__, lead_database)
            print(Fore.GREEN + "Lead added successfully." + Style.RESET_ALL)
        
#Option 3: Remove a lead
        elif choice == "3":
            company_url = input("Enter company URL to remove lead: ")
            if validations.url_exists(company_url, lead_database):
                validations.confirmation_validation(
                    "Do you want to permanently delete this lead? (Y/N): ",
                    "Removal cancelled."
                )
                data_operations.remove_lead(company_url, lead_database)
                print("Lead deleted successfully.")
            else:
                visual_seperator()
                print(Fore.RED + "Lead with this URL does not exist. " + Style.RESET_ALL)
        
#Option 4: Modify existing lead details
        elif choice == "4":
            company_url = input("Enter URL of the lead to update (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            if not validations.url_exists(company_url, lead_database):
                print("Lead with this URL does not exist.")
                continue

            field = input("Select ONE field to update \n(name, company_name, email, role, assigned_to, status): ")
            new_value = input(f"Updated {field}: ")

            if field == "name" and not validations.name_validation(new_value):
                print("Invalid - Name must only contain letters.")
                continue

            if field == "company_name" and not validations.company_name_validation(new_value):
                print("Invalid - Enter company name longer than 0 characters.")
                continue

            if field == "email" and not validations.email_validation(new_value):
                print("Invalid - Enter a valid email address.")
                continue

            if field == "role" and not validations.role_validation(new_value):
                print("Invalid - Role must only contain letters.")
                continue

            if field == "assigned_to" and not validations.assigned_to_validation(new_value):
                print("Invalid - Sales representative name must be only letters")
                continue

            if field == "status" and not validations.status_validation(new_value):
                print("Invalid - Enter status 'qualified' or 'unqualified'")
                continue

            validations.confirmation_validation(
                f"Do you want to update the {field} to '{new_value}'? (Y/N): ",
                "Update cancelled."
            )

            if data_operations.update_lead(company_url, field, new_value, lead_database):
                print(f"Lead {field} updated successfully.")
            else:
                print("Failed to update lead.")

#Option 5: Display all the leads
        elif choice == "5":
            data_operations.display_leads(lead_database)

#Option 6: Search the lead list for specific lead details
        elif choice == "6":
            visual_seperator()
            company_url = input("Enter company URL(in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            data_operations.find_lead(company_url, lead_database)

#Option 7: Exit
        elif choice == "7":
            print("Exiting Sales CRM.")
            break
        else:
            validations.selection_invalid()


main()