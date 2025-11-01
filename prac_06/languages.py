"""
CP1404/CP5632 Practical - Client code to use the ProgrammingLanguage class.
Estimate: 20 minutes
Actual:   10 minutes
"""

from prac_06.programming_language import ProgrammingLanguage


def main():
    """Code to show dynamic languages using ProgrammingLanguage class."""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    print(python)
    print("The dynamically typed languages are:")

    programming_languages = [python, ruby, visual_basic]
    for language in programming_languages:
        if language.is_dynamic():
            print(language.name)


main()