import os
from collections import Counter

FILE_PATH = "z_lorem_ipsum.txt"

if not os.path.exists(FILE_PATH):
    raise FileNotFoundError("The file 'z_lorem_ipsum.txt' does not exist.")

with open(FILE_PATH, encoding="utf-8") as file:
    letter_counts = Counter(char for line in file for char in line)

for char, count in sorted(letter_counts.items()):
    print(f"{char!r}: {count}")
