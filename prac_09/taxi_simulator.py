"""
CP1404/CP5632 Practical
Taxi simulator program that uses Taxi and SilverServiceTaxi classes.
"""

from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import SilverServiceTaxi

MENU = "q)uit, c)hoose taxi, d)rive"

def main():
    """Taxi simulator menu program that uses Taxi and SilverServiceTaxi classes."""
    total_bill = 0.0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]
    current_taxi = None

    print("Let's drive!")
    print(MENU)
    menu_choice = input(">>> ").lower()
    while menu_choice != "q":
        if menu_choice == "c":
            print("Taxis available: ")
            display_taxis(taxis)

            try:
                taxi_choice = int(input("Choose taxi: "))
                current_taxi = taxis[taxi_choice]
            except (ValueError, IndexError):
                print("Invalid taxi choice")
        elif menu_choice == "d":
            if current_taxi:
                distance = float(input("Drive how far? "))

                current_taxi.start_fare()
                current_taxi.drive(distance)

                trip_cost = current_taxi.get_fare()
                total_bill += trip_cost

                print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
            else:
                print("You need to choose a taxi before you can drive")
        else:
            print("Invalid option")

        print(f"Bill to date: ${total_bill:.2f}")
        print(MENU)
        menu_choice = input(">>> ").lower()
    print("quit")

def display_taxis(taxis):
    """Print list of taxis."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

main()