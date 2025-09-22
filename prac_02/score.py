"""
CP1404/CP5632 - Practical
Program to determine score status
"""

import random

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

def main():
    """Program to determine score result."""
    score = float(input("Enter score: "))
    score_result = determine_result(score)
    random_score = random.randint(MINIMUM_SCORE, MAXIMUM_SCORE)
    random_result = determine_result(random_score)
    print(score_result)
    print(f"Random score: {random_score}")
    print(random_result)

def determine_result(score):
    """Return result based on score."""
    if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        return "Invalid score"
    elif score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()