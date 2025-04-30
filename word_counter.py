import os
import re
from collections import Counter

FILE_PATH = "z_lorem_ipsum.txt"


def count_words(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, encoding="utf-8") as file:
        text = file.read().lower()
        words = re.findall(r"\b\w+\b", text)
        return Counter(words)


def print_counts(counter):
    for word, count in sorted(counter.items()):
        print(f"{word!r}: {count}")


def main():
    word_counts = count_words(FILE_PATH)
    print_counts(word_counts)


if __name__ == "__main__":
    main()
