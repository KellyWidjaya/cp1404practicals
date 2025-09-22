"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def main():
    score = float(input("Enter score: "))
    score_result = determine_result(score)
    random_score = random.randint(1, 100)
    random_result = determine_result(random_score)
    print(score_result)
    print(f"Random score: {random_score}")
    print(random_result)

def determine_result(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"

main()