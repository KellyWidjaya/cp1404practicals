"""
CP1404/CP5632 Practical
Word Occurrences
Estimate: 20 minutes
Actual:   11 minutes
"""

text = input("Text: ").lower()
words = text.split()
word_to_count = {}

for word in words:
    word_to_count[word] = word_to_count.get(word, 0) + 1

word_width = max(len(word) for word in word_to_count)

for word, count in sorted(word_to_count.items()):
    print(f"{word:{word_width}} : {count}")