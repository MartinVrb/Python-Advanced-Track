def valid_password(password: str):
    is_valid = True
    count_digits = [char for char in password if char.isdigit()]

    if not 6 <= len(password) <= 10:
        is_valid = False
        print("Password must be between 6 and 10 characters")

    if not password.isalnum():
        is_valid = False
        print("Password must consist only of letters and digits")

    if len(count_digits) < 2:
        is_valid = False
        print("Password must have at least 2 digits")

    if is_valid:
        print("Password is valid")

valid_password(input())
