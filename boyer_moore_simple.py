def bad_char_table(pattern):
    """Creates the bad character shift table."""
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0  # Empty pattern matches at index 0

    bad_char = bad_char_table(pattern)
    i = 0  # Index in text

    while i <= n - m:
        j = m - 1  # Start comparing from end of pattern

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            print(f"Pattern found at index {i}")
            return i  # Match found
        else:
            # Shift pattern using bad character rule
            shift = max(1, j - bad_char.get(text[i + j], -1))
            i += shift

    print("Pattern not found")
    return -1


def main():
    text = "ababcabcacbab"
    pattern = "abcac"
    boyer_moore(text, pattern)


if __name__ == "__main__":
    main()
