# 1.
name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

# 2.
in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")

# 3.
with open("numbers.txt", "r") as in_file:
    first_number = int(in_file.readline())   # Read the first line and convert to int
    second_number = int(in_file.readline())  # Read the second line and convert to int

result = first_number + second_number
print(f"Result: {result}")

# 4.
with open("numbers.txt", "r") as in_file:
    total = 0
    for line in in_file:
        number = int(line)
        total += number
print(f"Total: {total}")