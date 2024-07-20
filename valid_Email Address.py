import re
def is_valid_email(email):
    pattern = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    return bool(pattern.match(email))

email = input("Enter an email address: ")
print("Valid Email Address" if is_valid_email(email) else "Invalid Email Address")
