name = input("Enter your name: ")
out_file = open("name.txt", "w")
out_file.write(name)
out_file.close()