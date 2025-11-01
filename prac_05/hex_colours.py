"""
CP1404/CP5632 Practical
Colour codes in a dictionary
"""

NAME_TO_CODE = {"Bright Turquoise": "08e8de", "Cherry Blossom Pink": "ffb7c5", "Chocolate": "d2691e",
                "Deep Peach": "004b49", "Eggplant": "614051", "Dutch White": "efdfbb", "Ferrari Red": "ff2800",
                "Forest Green": "228b22", "Camel": "c19a6b", "Dandelion": "f0e130"}
print(NAME_TO_CODE)

name_width = max(len(code) for code in NAME_TO_CODE.keys())

for name, code in NAME_TO_CODE.items():
    print(f"{name:{name_width}} is #{code}")

colour_name = input("Enter colour name: ").title()
while colour_name != "":
    try:
        print(f"{colour_name} is #{NAME_TO_CODE[colour_name]}")
    except KeyError:
        print("Invalid colour name")
    colour_name = input("Enter colour name: ").title()