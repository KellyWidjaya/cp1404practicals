"""
CP1404/CP5632 Practical
UnreliableCar class
"""

from prac_09.car import Car
import random


class UnreliableCar(Car):
    """Specialised version of a Car that drives based on reliability."""

    def __init__(self, name, fuel, reliability):
        """Initialise a UnreliableCar instance, based on parent class Car."""
        super().__init__(name, fuel)
        self.reliability = reliability

    def drive(self, distance):
        """Drive the car if it passes the reliability check."""
        distance_driven = 0
        if random.uniform(0, 100) < self.reliability:
            distance_driven = super().drive(distance)
        return distance_driven
