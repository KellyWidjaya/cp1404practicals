"""
CP1404/CP5632 Practical
Code to test the SilverServiceTaxi class methods.
"""

from prac_09.silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class methods."""
    my_taxi = SilverServiceTaxi("my taxi", 100, 2)
    my_taxi.drive(18)
    print(my_taxi)
    print(f"fare: ${my_taxi.get_fare()}")
    assert abs(my_taxi.get_fare() - 48.78) < 0.01, "Fare calculation is incorrect"

main()