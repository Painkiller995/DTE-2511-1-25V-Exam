from collections import Counter

with open("z_lorem_ipsum.txt", encoding="utf-8") as file:
    letter_counts = Counter(char for line in file for char in line)

for char, count in sorted(letter_counts.items()):
    print(f"{char!r}: {count}")
