"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError occurs when the user enters something that cannot be converted to an integer using int(). For example: ten, 10.0.
2. When will a ZeroDivisionError occur?
A ZeroDivisionError occurs when the denominator entered is 0, because division by zero is mathematically undefined.
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
We can use a while loop to repeatedly ask for a non-zero denominator until the user enters a valid number that isn’t 0.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    while denominator == 0:
        print("Denominator cannot be zero!")
        denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:
    print("Numerator and denominator must be valid numbers!")
print("Finished.")