"""
CP1404/CP5632 Practical
Code to test the UnreliableCar class methods.
"""

from prac_09.unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class with multiple drive attempts."""
    reliable_car = UnreliableCar("Reliable Car", 100, 90)
    unreliable_car = UnreliableCar("Unreliable Car", 100, 30)

    reliable_successes = 0
    unreliable_successes = 0

    for attempt in range(100):
        if reliable_car.drive(1) > 0:
            reliable_successes += 1

        if unreliable_car.drive(1) > 0:
            unreliable_successes += 1

    print(f"Reliable car succeeded {reliable_successes}/100 drives (expected: around 90)")
    print(f"Unreliable car succeeded {unreliable_successes}/100 drives (expected: around 30)")


main()