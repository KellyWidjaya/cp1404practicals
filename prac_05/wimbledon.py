"""
CP1404/CP5632 Practical
Wimbledon Champions
Estimate: 30 minutes
Actual:   40 minutes
"""

import csv

FILENAME = "wimbledon.csv"

def main():
    """Run the Wimbledon champions program"""
    print("Wimbledon Champions: ")

    records = load_data()
    champion_to_count, countries = process_data(records)
    display_results(champion_to_count, countries)

def display_results(champion_to_count, countries):
    """Print the champions with counts and list of countries that have won."""
    for champion, count in champion_to_count.items():
        print(f"{champion} {count}")
    print()
    print(f"These {len(countries)} countries have won Wimbledon: ")
    print(", ".join(sorted(countries)))

def process_data(records):
    """Returns a dictionary of champion_to_count and a set of countries."""
    champion_to_count = {}
    countries = set()
    for record in records:
        champion_to_count[record[2]] = champion_to_count.get(record[2], 0) + 1
        countries.add(record[1])
    return champion_to_count, countries

def load_data():
    """Read Wimbledon CSV data and return a list of records."""
    records = []
    with open(FILENAME, "r", encoding="utf-8-sig") as in_file:
        reader = csv.reader(in_file)
        next(reader)

        for record in reader:
            records.append(record)
    return records

main()