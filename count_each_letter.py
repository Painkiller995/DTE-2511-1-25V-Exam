import os
from collections import Counter

FILE_PATH = "z_lorem_ipsum.txt"


def count_characters(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file '{file_path}' does not exist.")

    with open(file_path, encoding="utf-8") as file:
        return Counter(char for line in file for char in line)


def print_counts(counter):
    for char, count in sorted(counter.items()):
        print(f"{char!r}: {count}")


def main():
    letter_counts = count_characters(FILE_PATH)
    print_counts(letter_counts)


if __name__ == "__main__":
    main()
