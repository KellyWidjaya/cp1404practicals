"""
CP1404/CP5632 Practical
"Quick Pick" Lottery Ticket Generator
"""

import random

NUMBERS_PER_LINE = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_picks = int(input("How many quick picks? "))

number_width = len(str(MAXIMUM_NUMBER))
for i in range(number_of_picks):
    numbers = []
    for j in range(NUMBERS_PER_LINE):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        numbers.append(number)
    print(" ".join(f"{number:{number_width}}" for number in numbers))