"""
CP1404/CP5632 - Practical
Broken program to determine score status
Pseudocode:

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

get score
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE
    message = "Invalid score"
else
    if score >= EXCELLENT_THRESHOLD
        message = "Excellent"
    else if score >= PASS_THRESHOLD
        message = "Passable"
    else
        message = "Bad"

print message
"""

# TODO: Fix this!

MINIMUM_SCORE = 0
MAXIMUM_SCORE = 100
EXCELLENT_THRESHOLD = 90
PASS_THRESHOLD = 50

score = float(input("Enter score: "))
if score < MINIMUM_SCORE or score > MAXIMUM_SCORE:
    message = "Invalid score"
else:
    if score >= EXCELLENT_THRESHOLD:
        message = "Excellent"
    elif score >= PASS_THRESHOLD:
        message = "Passable"
    else:
        message = "Bad"

print(message)