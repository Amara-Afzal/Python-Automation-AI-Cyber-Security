import re

def validate_username(username):
    if not username:
        return "Username cannot be empty"
    if len(username) < 4:
        return "Username too short"
    if not username.isalnum():
        return "Username must contain only letters and numbers"
    return "Valid"

def validate_email(email):
    if not email:
        return "Email cannot be empty"
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return "Valid"
    return "Invalid email format"

def validate_password(password):
    if not password:
        return "Password cannot be empty"
    if len(password) < 8:
        return "Password too short"
    if not re.search(r"[A-Z]", password):
        return "Must contain uppercase letter"
    if not re.search(r"[a-z]", password):
        return "Must contain lowercase letter"
    if not re.search(r"[0-9]", password):
        return "Must contain a digit"
    if not re.search(r"[!@#$%^&*()_+]", password):
        return "Must contain special character"
    return "Strong"
while True:
    username = input("Enter username: ").strip()
    result = validate_username(username)
    print(result)
    if result == "Valid":
        break
while True:
    email = input("Enter email: ").strip()
    result = validate_email(email)
    print(result)
    if result == "Valid":
        break
while True:
    password = input("Enter password: ").strip()
    result = validate_password(password)
    print(result)
    if result == "Strong":
        break

print("\n All inputs validated successfully!")
