"""
CP1404/CP5632 Practical - Client code to use the Project class.
Estimate: 50 minutes
Actual:   minutes
"""

MENU = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""

def main():
    """Project management menu program."""
    print("Welcome to Pythonic Project Management")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "l":
            print("load projects")
        elif choice == "s":
            print("save projects")
        elif choice == "d":
            print("display projects")
        elif choice == "f":
            print("filter projects by date")
        elif choice == "a":
            print("add new project")
        elif choice == "u":
            print("update project")
        else:
            print("invalid choice")

        print(MENU)
        choice = input(">>> ").lower()
    print("Thank you for using custom-built project management software.")

main()