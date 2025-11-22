"""
CP1404/CP5632 Practical - Code to test the Guitar class methods.
"""

from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'

def main():
    """Load and display guitars."""
    guitars = load_guitars()
    add_guitars(guitars)
    save_guitars(guitars)
    display_guitars(guitars)

def load_guitars():
    """Read guitars from file into a list of Guitar objects."""
    guitars = []

    in_file = open(FILENAME, 'r', encoding='utf-8')
    for line in in_file:
        parts = line.strip().split(',')
        guitar = Guitar(parts[0], int(parts[1]), float(parts[2]))
        guitars.append(guitar)
    in_file.close()

    return guitars

def add_guitars(guitars):
    """Get new guitars and add them to the list."""
    name = input("Name: ")
    while name != "":
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)

        print(f"{guitar} added.")
        print()

        name = input("Name: ")

def save_guitars(guitars):
    """Save all guitars to the CSV file."""
    out_file = open(FILENAME, 'w', encoding='utf-8')
    for guitar in guitars:
        print(f"{guitar.name},{guitar.year},{guitar.cost}", file=out_file)
    out_file.close()

def display_guitars(guitars):
    """Print list of guitars neatly."""
    guitars.sort()
    for guitar in guitars:
        print(guitar)

main()