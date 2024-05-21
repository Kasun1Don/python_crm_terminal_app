import csv
import pandas as pd
from tabulate import tabulate
from colorama import init, Fore, Style
from lead import Lead

init()

# searches for a lead in the CSV file based on the company URL and prints the lead's details if found using the __str__ method of Lead
def find_lead(company_url, lead_database="leads_appdatabase.csv"):
    with open(lead_database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["company_url"] == company_url:
                lead = Lead(
                    row['name'],
                    row['company_name'], 
                    row['company_url'], 
                    row['email'], 
                    row['role'], 
                    row['assigned_to'], 
                    row['status']
                )
                print(lead)
                return
    print(Fore.RED + "\nNo lead found for this company URL." + Style.RESET_ALL)

# prints all leads from the CSV file to the console using pandas
def display_leads(lead_database="leads_appdatabase.csv"):
    try:
        df = pd.read_csv(lead_database)
        
        # Select specific columns to display
        selected_columns = ['company_url', 'company_name', 'name', 'role', 'assigned_to', 'status']
        df_selected = df[selected_columns]
        
        # Fill NaN values with empty strings
        df_selected.fillna('', inplace=True)
        
        # Use tabulate to format table
        table_str = tabulate(df_selected, headers='keys', tablefmt='grid', showindex=False)
        print(table_str)

    except Exception:
        print(Fore.RED + "\nAn error occurred, please restart program" + Style.RESET_ALL)


# appends a new lead record to the csv file
def insert_lead(new_lead, lead_database="leads_appdatabase.csv"):
    with open(lead_database, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_lead.keys())
        writer.writerow(new_lead)

# remove a lead record from the CSV file based on the company URL
def remove_lead(company_url, lead_database="leads_appdatabase.csv"):
    lines = []
    with open(lead_database, "r") as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            if row and row[3] != company_url:  
                lines.append(row)
    with open(lead_database, "w", newline='') as writefile:
        writer = csv.writer(writefile)
        # write filtered rows back to the CSV file, removing the rows with specified URLs
        writer.writerows(lines)

# reads the column titles to retrieve
def get_columns(lead_database="leads_appdatabase.csv"):
    with open(lead_database) as f:
        data = f.readline()
        return data.strip("\n").split(",")
 
# edit existing lead details
def update_lead(company_url, field, new_value, lead_database="leads_appdatabase.csv"):
    updated = False
    lines = []
    columns = get_columns(lead_database)
    with open(lead_database, "r") as readfile:
        reader = csv.DictReader(readfile)
        # iterate over each row in the database to check for specified URL
        for row in reader:
            if row["company_url"] == company_url:
                row[field] = new_value
                updated = True
            lines.append(row)

    # if the lead was updated, write the updated rows back to the database
    if updated:
        with open(lead_database, "w", newline='') as writefile:
            writer = csv.DictWriter(writefile, fieldnames=columns)
            writer.writeheader()
            writer.writerows(lines)
        return True
    else:
        return False