import uuid
import datetime

#new lead instance with lead details
class Lead:
    def __init__(self, name, company_name, company_url, email, role, assigned_to, status):
        self.id = str(uuid.uuid4())
        self.name = name
        self.company_name = company_name
        self.company_url = company_url
        self.email = email
        self.role = role
        self.assigned_to = assigned_to
        self.status = status
        self.timestamp = datetime.datetime.now() #record the current date and time 

#provide a string representation of the lead instance to display lead details in terminal app
    def __str__(self):
            return (
                f"ID: {self.id}\n"
                f"Name: {self.name}\n"
                f"Company Name: {self.company_name}\n"
                f"Company URL: {self.company_url}\n"
                f"Email: {self.email}\n"
                f"Role: {self.role}\n"
                f"Assigned to: {self.assigned_to}\n"
                f"Status: {self.status}\n"
                f"Timestamp: {self.timestamp}")

#test if code works
# lead = Lead(
#     name="John Doe",
#     company_name="Example",
#     company_url="https://example.com",
#     email="john.doe@example.com",
#     role="Manager",
#     assigned_to="KD",
#     status="qualified")

# print(lead)