import csv
import pandas

#searches for a lead in the CSV file based on the company URL and prints the lead's details if found
def find_lead(company_url, lead_database="leads_appdatabase.csv"):
    with open(lead_database) as f:
        reader = csv.DictReader(f)
        for row in reader:
            if row["company_url"] == company_url:
                print(f"ID: {row['id']}")
                print(f"Name: {row['name']}")
                print(f"Company Name: {row['company_name']}")
                print(f"Company URL: {row['company_url']}")
                print(f"Email: {row['email']}")
                print(f"Role: {row['role']}")
                print(f"Assigned to: {row['assigned_to']}")
                print(f"Status: {row['status']}")
                print(f"Timestamp: {row['timestamp']}")
                return
    print("No lead found for this company URL.")


#appends a new lead record to the csv file
def insert_lead(new_lead, lead_database="leads_appdatabase.csv"):
    with open(lead_database, "a", newline='') as f:
        writer = csv.DictWriter(f, fieldnames=new_lead.keys())
        writer.writerow(new_lead)

#remove a lead record from the CSV file based on the company URL
def remove_record(company_url, lead_database="lead_appdatabase.csv"):
    lines = []
    with open(lead_database, "r") as readfile:
        reader = csv.reader(readfile)
        for row in reader:
            if row and row[3] != company_url:  # Updated to match column index for company_url
                lines.append(row)
    with open(lead_database, "w", newline='') as writefile:
        writer = csv.writer(writefile)
        #write filtered rows back to the CSV file, removing the rows with specified URLs
        writer.writerows(lines)


#prints all leads from the CSV file to the console
def display_leads(lead_database="leads_appdatabase.csv"):
    df = pd.read_csv(lead_database)
    print(df.to_string(index=False))


#reads the column titles
def get_columns()
    


