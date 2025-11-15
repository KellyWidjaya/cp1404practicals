"""
CP1404/CP5632 Practical
Band class
"""

class Band:
    """Represent a Band object."""

    def __init__(self, level=""):
        """Initialise a Band."""
        self.level = level
        self.musicians = []

    def __str__(self):
        """Return a string representation of a Band."""
        return f"{self.level} ({', '.join(str(musician) for musician in self.musicians)})"

    def add(self, musician):
        """Add a musician to the band."""
        self.musicians.append(musician)

    def play(self):
        """Return a string showing each musician playing their first instrument."""
        result = []
        for musician in self.musicians:
            result.append(musician.play())
        return "\n".join(result)