"""
CP1404 - Practical
Program to convert password into asterisks
"""

MINIMUM_PASSWORD_LENGTH = 8

def main():
    """Hidden password program."""
    password = get_password()
    print_asterisk(password)

def print_asterisk(password):
    """Print asterisks equal to the length of the password."""
    print('*' * len(password))

def get_password():
    """Get valid password of minimum length."""
    password = input("Password: ")
    while len(password) < MINIMUM_PASSWORD_LENGTH:
        print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long")
        password = input("Password: ")
    return password

main()