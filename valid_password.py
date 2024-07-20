import re
def is_valid_password(password):
    pattern = re.compile(r'^(?=.*[A-Z])(?=.*[a-z])(?=.*\d)(?=.*[@$!%*?&])[A-Za-z\d@$!%*?&]{8,}$')
    return bool(pattern.match(password))

password = input("Enter a password: ")
print("Valid Password" if is_valid_password(password) else "Invalid Password")
