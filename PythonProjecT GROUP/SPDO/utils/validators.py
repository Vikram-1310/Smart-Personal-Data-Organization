import re

def validate_email(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return re.match(pattern, email)

def validate_phone(phone):
    return phone.isdigit() and len(phone) == 10

def validate_age(age):
    return age.isdigit() and 0 < int(age) < 120