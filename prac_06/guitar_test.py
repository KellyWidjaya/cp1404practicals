"""
CP1404/CP5632 Practical - Code to test the Guitar class methods.
Estimate: 15 minutes
Actual:   8 minutes
"""

from prac_06.guitar import Guitar

def main():
    """Test the Guitar class methods."""
    gibson = Guitar("Gibson L-5 CES", 1922, 16035.40)
    another = Guitar("Another Guitar", 2013, 760)

    print(f"{gibson.name} get_age() - Expected 100. Got {gibson.get_age()}")
    print(f"{another.name} get_age() - Expected 9. Got {another.get_age()}")
    print(f"{gibson.name} is_vintage() - Expected True. Got {gibson.is_vintage()}")
    print(f"{another.name} is_vintage() - Expected False. Got {another.is_vintage()}")

main()