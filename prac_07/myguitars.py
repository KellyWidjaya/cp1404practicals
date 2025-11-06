"""
CP1404/CP5632 Practical - Code to test the Guitar class methods.
"""

from prac_07.guitar import Guitar

FILENAME = 'guitars.csv'

def main():
    """Load and display guitars."""
    guitars = load_guitars()

    guitars.sort()
    for guitar in guitars:
        print(guitar)


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

main()