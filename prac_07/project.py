"""
CP1404/CP5632 Practical - The Project class.
Estimate: 30 minutes
Actual:   35 minutes
"""

class Project:
    """Represent a Project object."""

    def __init__(self, name, date, priority, cost, completion):
        """Initialise a Project instance.

        name: string, the project name.
        date: date, the project start date.
        priority: int, the priority number.
        cost: float, the estimated cost.
        completion: int, the completion percentage.
        """
        self.name = name
        self.date = date
        self.priority = priority
        self.cost = cost
        self.completion = completion

    def is_complete(self):
        """Return True if the project is 100% complete."""
        return self.completion >= 100

    def __lt__(self, other):
        """Compare two projects by priority for sorting."""
        return self.priority < other.priority

    def __str__(self):
        """Return a formatted string representation of the project."""
        return f"{self.name}, start: {self.date.strftime("%d/%m/%Y")}, priority {self.priority}, estimate: ${self.cost:.2f}, completion: {self.completion}%"