"""
CP1404/CP5632 Practical
Wikipedia title search program
"""

import wikipedia


title = input("Enter page title: ")
while title != "":
    try:
        page = wikipedia.page(title, auto_suggest=False)

        print(page.title)
        print(page.summary.strip())
        print(page.url)

    except wikipedia.exceptions.DisambiguationError as e:
        print("We need a more specific title. Try one of the following, or a new search:")
        print(e.options)

    except wikipedia.exceptions.PageError:
        print(f'Page id "{title}" does not match any pages. Try another id!')

    print()
    title = input("Enter page title: ")
print("Thank you.")