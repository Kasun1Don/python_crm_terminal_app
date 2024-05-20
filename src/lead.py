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
  self.timestamp = datetime.datetime.now()

def __str__(self):
  return (f"ID: {self.id}, Name: {self.name}, Company Name: {self.company_name}, "
                f"Company URL: {self.company_url}, Email: {self.email}, Role: {self.role}, "
                f"Assigned to: {self.assigned_to}, Status: {self.status}, Timestamp: {self.timestamp}")

#string representation of the lead instance for printing lead information in terminal


lead = Lead("Emily Davis", "https://example.net", "emily.davis@example.net", "Analyst", "Carol White", "qualified")
print(f"Lead Information:\n{lead}")