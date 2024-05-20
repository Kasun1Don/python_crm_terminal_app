from colorama import init, Fore, Style
from lead import Lead
import validations
import data_operations

init()

# def visual_seperator():
#     print("\n\n")

#menu options
def display_options():
    print("\n Lightning CRM for Sales [Menu]")
    print("1 > Check lead ownership")
    print("2 > Add new lead")
    print("3 > Remove lead")
    print("4 > Modify lead details")
    print("5 > Display all leads")
    print("6 > Search for a lead")
    print("7 > Exit")

def main():
    lead_database = "leads_appdatabase.csv"

#select menu option
    while True:
        display_options()
        choice = input("Enter Menu Option Number: ")

#Option 1: Check if a lead is already assigned to sales person
        if choice == "1":
            company_url = input("Enter the URL (in http:// or https:// format): ")
            if validations.url_exists(company_url, lead_database):
                print(Fore.RED + "Lead is already assigned." + Style.RESET_ALL)
            else:
                print("Lead is available to be assigned.")
                
#Option 2: Add a new lead
        elif choice == "2":
            company_url = input("Company URL: ")
            company_name = input("Company name: ")
            name = input("Lead's name (optional): ")
            role = input("Lead's role (optional): ")
            email = input("Lead's email (optional): ")
            assigned_to = input("Lead owner's name: ")
            status = input("Lead status [qualified/unqualified] (optional): ")
            

            if not validations.name_validation(name):
                print("Invalid - Name must only contain letters.")
                continue
            
            if not validations.company_name_validation(company_name):
                print("Invalid - Enter company name longer than 0 characters.")
                continue
            
            if not validations.company_url_validation(company_url):
                print("Invalid - Enter company url in either http:// or https:// format.")
                continue
            
            if not validations.email_validation(email):
                print("Invalid - Enter a valid email address.")
                continue
            
            if validations.url_exists(company_url, lead_database):
                print("Invalid - A lead this URL already exists.")
                continue
            
            if not validations.role_validation(role):
                print("Invalid - Role must only contain letters.")
                continue
            
            if not validations.status_validation(status):
                print("Invalid - Enter status 'qualified' or 'unqualified'")
                continue
            
            validations.confirmation_validation(
                "Add lead to database? (Y/N): ",
                "Lead not created"
            )

            new_lead = Lead(name, company_name, company_url, email, role, assigned_to, status)
            data_operations.insert_lead(new_lead.__dict__, lead_database)
            print("Lead added successfully.")
        
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
                print("Lead with this URL does not exist.")
        
#Option 4: Modify existing lead details
        elif choice == "4":
            company_url = input("Enter URL of the lead to update: ")
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

            if field == "company_url" and not validations.company_url_validation(new_value):
                print("Invalid - Enter company url in either http:// or https:// format.")
                continue

            if field == "email" and not validations.email_validation(new_value):
                print("Invalid - Enter a valid email address.")
                continue

            if field == "role" and not validations.role_validation(new_value):
                print("Invalid - Role must only contain letters.")
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
            company_url = input("Enter company URL: ")
            data_operations.find_lead(company_url, lead_database)

#Option 7: Exit
        elif choice == "7":
            print("Exiting Sales CRM.")
            break
        else:
            validations.selection_invalid()


main()