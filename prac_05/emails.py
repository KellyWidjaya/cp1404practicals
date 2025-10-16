"""
CP1404/CP5632 Practical
Emails
Estimate: 20 minutes
Actual:   24 minutes
"""

email_to_name = {}

email = input("Email: ")
while email != "":
    # extract name part before '@', replace dots with spaces, and capitalize each word
    email_to_name[email] = " ".join(email.split("@")[0].split(".")).title()
    choice = input(f"Is your name {email_to_name[email]}? (Y/n) ").upper()
    if choice != "" and choice != "Y":
        email_to_name[email] = input("Name: ").title()
    email = input("Email: ")

print()

for email, name in email_to_name.items():
    print(f"{name} ({email})")