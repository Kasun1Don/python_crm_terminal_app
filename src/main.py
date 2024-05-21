from colorama import init, Fore, Style
from lead import Lead
import validations
import data_operations

init()

# visual separator for improved readability
def visual_seperator():
    print("\n")

# display main menu options
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

# prompt to select menu option
    while True:
        display_options()
        choice = input("Enter Menu Option Number: ")

# Option 1: Check if a lead is already assigned to a sales person
        if choice == "1":
            visual_seperator()
            # prompt user to enter the lead's company URL
            while True:
                company_url = input("Enter the URL (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")

                    # validate the URL format
                if not validations.company_url_validation(company_url):
                    print(Fore.RED + "Invalid - Enter company URL in either http:// or https:// format." + Style.RESET_ALL)
                    continue
                break
            
            # check if URL is already assigned to a sales person using validation function
            assigned_to = validations.get_assigned_to(company_url, lead_database)
            if assigned_to:
                visual_seperator()
                print(Fore.RED + f"Lead is already assigned to {assigned_to}." + Style.RESET_ALL)
            else:
                visual_seperator()
                print(Fore.GREEN + "This lead is available to be assigned." + Style.RESET_ALL)
                
# Option 2: Add a new lead
        elif choice == "2":
            visual_seperator()
            while True:
                # prompt user to enter the lead's company URL
                company_url = input("Company URL (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")

                if not validations.company_url_validation(company_url):
                    visual_seperator()
                    print(Fore.RED + "Invalid - Enter company URL in either http:// or https:// format." + Style.RESET_ALL)
                    continue
                # check if the URL already exists in the CRM database
                if validations.url_exists(company_url, lead_database):
                    visual_seperator()
                    print(Fore.RED + "Invalid - A lead with this URL already exists." + Style.RESET_ALL)
                    continue
                break
            
        # prompts user to enter new lead's details, validating each input
            while True:
                company_name = input("Company name: ")
                if validations.company_name_validation(company_name):
                    break
                else:
                    print(Fore.RED + "Invalid - Enter company name longer than 0 characters." + Style.RESET_ALL)

            while True:
                name = input("Lead's name (optional): ")
                if validations.name_validation(name):
                    break
                else:
                    print(Fore.RED + "Invalid - Name must only contain letters." + Style.RESET_ALL)

            while True:
                role = input("Lead's role (optional): ")
                if validations.role_validation(role):
                    break
                else:
                    print(Fore.RED + "Invalid - Role must only contain letters." + Style.RESET_ALL)

            while True:
                email = input("Lead's email (optional): ")
                if validations.email_validation(email):
                    break
                else:
                    print(Fore.RED + "Invalid - Enter a valid email address." + Style.RESET_ALL)

            while True:
                assigned_to = input("Lead owner's name: ")
                if validations.assigned_to_validation(assigned_to):
                    break
                else:
                    print(Fore.RED + "Invalid - Sales representative name must be only letters." + Style.RESET_ALL)

            while True:
                status = input("Lead status [qualified/unqualified] (optional): ")
                if validations.status_validation(status):
                    break
                else:
                    print(Fore.RED + "Invalid - Enter status 'qualified' or 'unqualified'." + Style.RESET_ALL)
            
            # confirm the user wants to add the lead to the CRM
            visual_seperator()
            validations.confirmation_validation(
                (Fore.BLUE + "Add lead to CRM? (Y/N): " + Style.RESET_ALL),
                (Fore.RED + "Lead not created" + Style.RESET_ALL)
            )

            # create new lead object
            new_lead = Lead(name, company_name, company_url, email, role, assigned_to, status)
            # add the lead to the CRM database
            data_operations.insert_lead(new_lead.__dict__, lead_database)
            visual_seperator()
            print(Fore.GREEN + "Lead added successfully." + Style.RESET_ALL)
        
# Option 3: Remove a lead
        elif choice == "3":
            visual_seperator
            # prompt user to enter the lead's company URL
            company_url = input("Enter company URL to remove lead (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            if validations.url_exists(company_url, lead_database):
                visual_seperator()
                # prompt for confirmation before permanently deleting the lead
                validations.confirmation_validation(
                    (Fore.RED + "\nDo you want to permanently delete this lead? (Y/N): " + Style.RESET_ALL),
                    "Removal cancelled."
                )

                # remove the lead from the CRM database
                data_operations.remove_lead(company_url, lead_database)
                visual_seperator()
                print(Fore.GREEN + "Lead deleted successfully." + Style.RESET_ALL)
            else:
                visual_seperator()
                print(Fore.RED + "Lead with this URL does not exist. " + Style.RESET_ALL)
        
# Option 4: Modify existing lead details
        elif choice == "4":
            visual_seperator()
            # prompt user to enter the lead's company URL
            company_url = input("Enter URL of the lead to update (in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            if not validations.url_exists(company_url, lead_database):
                print(Fore.RED + "Lead with this URL does not exist." + Style.RESET_ALL)
                continue
            
            # loop until a valid field is entered
            while True:
                field = input("Select ONE field to update \n(name, company_name, email, role, assigned_to, status): ").strip().lower()

                if field in ["name", "company_name", "email", "role", "assigned_to", "status"]:
                    break
                else:
                    print(Fore.RED + "Invalid field. Choose from: name, company_name, email, role, assigned_to, status" + Style.RESET_ALL)

            # prompts user to enter the new value for the selected field and validates input
            new_value = input(f"Updated {field}: ")

            if field == "name" and not validations.name_validation(new_value):
                print(Fore.RED + "Invalid - Name must only contain letters." + Style.RESET_ALL)
                continue

            if field == "company_name" and not validations.company_name_validation(new_value):
                print(Fore.RED + "Invalid - Enter company name longer than 0 characters." + Style.RESET_ALL)
                continue

            if field == "email" and not validations.email_validation(new_value):
                print(Fore.RED + "Invalid - Enter a valid email address." + Style.RESET_ALL)
                continue

            if field == "role" and not validations.role_validation(new_value):
                print(Fore.RED + "Invalid - Role must only contain letters." + Style.RESET_ALL)
                continue

            if field == "assigned_to" and not validations.assigned_to_validation(new_value):
                print(Fore.RED + "Invalid - Sales representative name must be only letters" + Style.RESET_ALL)
                continue

            if field == "status" and not validations.status_validation(new_value):
                print(Fore.RED + "Invalid - Enter status 'qualified' or 'unqualified'" + Style.RESET_ALL)
                continue

            # confirm the user wants to update CRM field
            visual_seperator()
            validations.confirmation_validation(
                (Fore.RED + f"\nDo you want to update the {field} to '{new_value}'? (Y/N): " + Style.RESET_ALL),
                "Update cancelled."
            )

            # update the CRM database and provide feedback
            if data_operations.update_lead(company_url, field, new_value, lead_database):
                visual_seperator()
                print(Fore.GREEN + f"Lead {field} updated successfully." + Style.RESET_ALL)
            else:
                visual_seperator()
                print(Fore.RED + "Failed to update lead." + Style.RESET_ALL)

# Option 5: Display all the leads
        elif choice == "5":
            visual_seperator()
            #display all leads in formatted table using database functions
            data_operations.display_leads(lead_database)

# Option 6: Search the lead list for specific lead details
        elif choice == "6":
            visual_seperator()
            # prompt user for lead's company URL
            company_url = input("Enter company URL(in http:// or https:// format e.g." + Fore.GREEN + "\nhttps://www.salesforce.com" + Style.RESET_ALL + "): ")
            #search for specific lead detail fields in the database
            data_operations.find_lead(company_url, lead_database)

# Option 7: Exit terminal application
        elif choice == "7":
            visual_seperator()
            print(Fore.GREEN + "Exiting LITESPEED Sales CRM." + Style.RESET_ALL)
            break
        else:
            validations.selection_invalid()


main()