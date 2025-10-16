"""
CP1404/CP5632 Practical
Wimbledon Champions
Estimate: 30 minutes
Actual:    minutes
"""

import csv

FILENAME = "wimbledon.csv"

def main():
    print("Wimbledon Champions: ")

    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)

        for record in reader:
            records.append(record)

    champion_to_count = {}
    countries = set()
    for record in records:
        champion_to_count[record[2]] = champion_to_count.get(record[2], 0) + 1
        countries.add(record[1])

    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")

    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

main()