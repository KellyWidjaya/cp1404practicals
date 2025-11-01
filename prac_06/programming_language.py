"""
CP1404/CP5632 Practical - The ProgrammingLanguage class.
Estimate: 20 minutes
Actual:   15 minutes
"""

class ProgrammingLanguage:
    """Represent a ProgrammingLanguage object."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Determine typing state."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Display a string output of the language details."""
        return f"{self.name}, {self.typing}, Reflection={self.reflection}, First appeared in {self.year}"