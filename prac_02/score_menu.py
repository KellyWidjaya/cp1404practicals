"""
CP1404/CP5632 - Practical
Score menu program to determine score status
"""

MENU = "(G)et a valid score (must be 0-100 inclusive)\n(P)rint result\n(S)how stars\n(Q)uit"
MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50


def main():
    """Menu program to get score, determine the result and print stars."""
    score = validate_score()

    print(MENU)
    choice = input(">>> ").upper()

    while choice != "Q":
        if choice == "G":
            score = validate_score()
        elif choice == "P":
            result = determine_result(score)
            print(result)
        elif choice == "S":
            print("*" * score)
        else:
            print("Invalid choice")
        print(MENU)
        choice = input(">>> ").upper()

    print("Farewell")

def validate_score():
    """Get valid score within the minimum and maximum range."""
    score = int(input("Enter score: "))
    while score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
        print("Invalid score")
        score = int(input("Enter score: "))
    return score

def determine_result(score):
    """Return result based on score."""
    if score >= EXCELLENT_THRESHOLD:
        return "Excellent"
    elif score >= PASS_THRESHOLD:
        return "Passable"
    else:
        return "Bad"

main()