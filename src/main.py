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


#string representation of the lead instance for printing lead information in terminal