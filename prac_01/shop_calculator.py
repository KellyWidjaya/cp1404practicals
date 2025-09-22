"""
Pseudocode:

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9
total = 0

get number_of_items
while number_of_items < 0
    print invalid message
    get number_of_items

repeat number_of_items times
    get price
    while price < 0
        print invalid message
        get price
    total = total + price

if total > DISCOUNT_THRESHOLD
    total = total * DISCOUNT_RATE

print number_of_items, total
"""

DISCOUNT_THRESHOLD = 100
DISCOUNT_RATE = 0.9
total = 0

number_of_items = int(input("Number of items: "))
while number_of_items < 0:
    print("Invalid input")
    number_of_items = int(input("Number of items: "))

for i in range(number_of_items):
    price = float(input("Price of item: "))
    while price < 0:
        print("Invalid input")
        price = float(input("Price of item: "))
    total += price

if total > DISCOUNT_THRESHOLD:
    total *= DISCOUNT_RATE

print(f"Total price for {number_of_items} items is ${total:.2f}")
