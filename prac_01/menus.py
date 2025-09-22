"""
Pseudocode:

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

get name
print MENU
get choice
while choice != Q
   if choice == H
       print "hello" name
   else if choice == G
       print "goodbye" name
   else
       print invalid message
   print MENU
   get choice
print finished message
"""

MENU = "(H)ello\n(G)oodbye\n(Q)uit"

name = input("Enter name: ")

print(MENU)
choice = input(">>> ").upper()

while choice != "Q":
    if choice == "H":
        print(f"Hello {name}")
    elif choice == "G":
        print(f"Goodbye {name}")
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished.")
