def compute_lps(pattern):
    """Computes the Longest Prefix Suffix (LPS) array."""
    lps = [0] * len(pattern)
    length = 0  # length of the previous longest prefix suffix

    i = 1
    while i < len(pattern):
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length - 1]
            else:
                lps[i] = 0
                i += 1
    return lps


def kmp_search(text, pattern):
    """KMP string matching algorithm."""
    n = len(text)
    m = len(pattern)
    lps = compute_lps(pattern)

    i = 0  # index for text
    j = 0  # index for pattern

    while i < n:
        if text[i] == pattern[j]:
            i += 1
            j += 1

        if j == m:
            print(f"Pattern found at index {i - j}")
            return i - j
        elif i < n and text[i] != pattern[j]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1

    print("Pattern not found")
    return -1


def main():
    text = "ababcabcacbab"
    pattern = "abcac"
    kmp_search(text, pattern)


if __name__ == "__main__":
    main()
