import re

def is_valid_phone_number(phone):
    pattern = re.compile(r'^(\+?\d{1,4}[\s-])?(?:\(\d{3}\)|\d{3})[\s-]\d{3}[\s-]\d{4}$')
    return bool(pattern.match(phone))

phone = input("Enter a phone number: ")
print("Valid Phone Number" if is_valid_phone_number(phone) else "Invalid Phone Number")
