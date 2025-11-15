"""
CP1404/CP5632 Practical
Taxi simulator program that uses Taxi and SilverServiceTaxi classes.
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Taxi simulator menu program that uses Taxi and SilverServiceTaxi classes."""
    print("Let's drive!")
    print(MENU)
    choice = input(">>> ").lower()
    while choice != "q":
        if choice == "c":
            print("choose taxi")
        elif choice == "d":
            print("drive")
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").lower()
    print("quit")

main()