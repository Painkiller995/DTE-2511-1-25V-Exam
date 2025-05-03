def main():
    text = input("Enter a text: ")
    pattern = input("Enter a string pattern: ")

    index = find_pattern(text, pattern)
    if index >= 0:
        print(f"Matched at index {index}")
    else:
        print("Unmatched")


# Return the index of the first match, or -1 if not found.
def find_pattern(text, pattern):
    for i in range(len(text) - len(pattern) + 1):
        if is_matched(i, text, pattern):
            return i
    return -1


# Check if the pattern matches the text starting at index i
def is_matched(i, text, pattern):
    return text[i : i + len(pattern)] == pattern


if __name__ == "__main__":
    main()
