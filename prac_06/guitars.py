"""
CP1404/CP5632 Practical - Client code to use the Guitar class.
Estimate: 20 minutes
Actual:   18 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Code to store all the user's guitars using Guitar class."""
    guitars = []

    print("My guitars!")

    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitars.append(Guitar(name, year, cost))
        print(f"{Guitar(name, year, cost)} added.")
        print()

        name = input("Name: ")

    print()
    print("These are my guitars:")

    for i, guitar in enumerate(guitars, 1):
        vintage_string = "(vintage)" if guitar.is_vintage() else ""

        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f} {vintage_string}")

main()