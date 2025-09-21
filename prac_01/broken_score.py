"""
CP1404/CP5632 - Practical
Broken program to determine score status
Pseudocode:

VALID_THRESHOLD = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

get score
if score < 0 or score > VALID_THRESHOLD
    result = "Invalid score"
else if score >= EXCELLENT_THRESHOLD
    result = "Excellent"
else if score >= PASSABLE_THRESHOLD
    result = "Passable"
else
    result = "Bad"
print result
"""

# TODO: Fix this!

VALID_THRESHOLD = 100
EXCELLENT_THRESHOLD = 90
PASSABLE_THRESHOLD = 50

score = float(input("Enter score: "))
if score < 0 or score > VALID_THRESHOLD:
    result = "Invalid score"
elif score >= EXCELLENT_THRESHOLD:
    result = "Excellent"
elif score >= PASSABLE_THRESHOLD:
    result = "Passable"
else:
    result = "Bad"
print(result)