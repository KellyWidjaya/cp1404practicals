name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()

in_file = open("name.txt", "r")
name = in_file.read()
in_file.close()
print(f"Hi {name}!")