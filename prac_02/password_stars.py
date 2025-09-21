MINIMUM_PASSWORD_LENGTH = 8

password = input("Password: ")
while len(password) < MINIMUM_PASSWORD_LENGTH:
    print(f"Password must be at least {MINIMUM_PASSWORD_LENGTH} characters long")
    password = input("Password: ")
for letter in password:
    print('*', end='')