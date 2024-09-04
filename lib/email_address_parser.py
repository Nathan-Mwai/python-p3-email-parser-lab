# your code goes here!
import re
class EmailAddressParser:
    email_pattern = re.compile(r"^[A-z][A-z0-9._%+-]+\@[A-z0-9.-]+\.[A-z]{2,}$")
    
    def __init__(self,email):
        self.email = email
    
    def parse(self):
        emails = re.split(r',|\s', self.email)
        parsing_emails = set()
        for email in emails:
            if self.email_pattern.fullmatch(email):
                parsing_emails.add(email)
        return sorted(list(parsing_emails))
        