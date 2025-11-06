"""
CP1404/CP5632 Practical - The Guitar class.
"""

CURRENT_YEAR = 2022
VINTAGE_AGE = 50

class Guitar:
    """Represent a Guitar object."""

    def __init__(self, name="", year=0, cost=0):
        """Initialise a Guitar instance."""
        self.name = name
        self.year = year
        self.cost = cost

    def get_age(self):
        """Return the age of the Guitar."""
        return CURRENT_YEAR - self.year

    def is_vintage(self):
        """Determine if the Guitar is vintage."""
        return self.get_age() >= VINTAGE_AGE

    def __lt__(self, other):
        """Compare guitars by year for sorting."""
        return self.year < other.year

    def __str__(self):
        """Display a string output of the guitar details."""
        return "{} ({}) : ${:,.2f}".format(self.name, self.year, self.cost)