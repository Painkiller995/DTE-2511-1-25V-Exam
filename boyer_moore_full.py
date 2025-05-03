def bad_char_table(pattern):
    """Creates the bad character shift table."""
    table = {}
    for i, char in enumerate(pattern):
        table[char] = i
    return table


def good_suffix_table(pattern):
    """Creates the good suffix shift table."""
    m = len(pattern)
    shift = [0] * (m + 1)
    border_pos = [0] * (m + 1)

    i = m
    j = m + 1
    border_pos[i] = j

    while i > 0:
        while j <= m and pattern[i - 1] != pattern[j - 1]:
            if shift[j] == 0:
                shift[j] = j - i
            j = border_pos[j]
        i -= 1
        j -= 1
        border_pos[i] = j

    # Set shift values for suffixes with no border
    j = border_pos[0]
    for i in range(m + 1):
        if shift[i] == 0:
            shift[i] = j
        if i == j:
            j = border_pos[j]

    return shift


def boyer_moore(text, pattern):
    m = len(pattern)
    n = len(text)
    if m == 0:
        return 0  # Empty pattern matches at index 0

    bad_char = bad_char_table(pattern)
    good_suffix = good_suffix_table(pattern)

    i = 0  # Index in text

    while i <= n - m:
        j = m - 1

        while j >= 0 and pattern[j] == text[i + j]:
            j -= 1

        if j < 0:
            print(f"Pattern found at index {i}")
            return i
        else:
            bc_shift = j - bad_char.get(text[i + j], -1)
            gs_shift = good_suffix[j + 1]
            i += max(bc_shift, gs_shift)

    print("Pattern not found")
    return -1


def main():
    text = "ababcabcacbab"
    pattern = "abcac"
    boyer_moore(text, pattern)


if __name__ == "__main__":
    main()
