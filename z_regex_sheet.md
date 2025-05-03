# ✅ Python Regex Cheatsheet

## 📌 Importing

```python
import re
```

---

## 🔤 Basic Patterns

| Pattern | Matches                             |
| ------- | ----------------------------------- |
| `.`     | Any character except newline (`\n`) |
| `^`     | Start of string                     |
| `$`     | End of string                       |
| `*`     | 0 or more repetitions               |
| `+`     | 1 or more repetitions               |
| `?`     | 0 or 1 repetition                   |
| `{n}`   | Exactly n repetitions               |
| `{n,}`  | n or more repetitions               |
| `{n,m}` | Between n and m repetitions         |

---

## 🧱 Character Classes

| Pattern        | Description                                  |
| -------------- | -------------------------------------------- |
| `[abc]`        | Matches 'a', 'b', or 'c'                     |
| `[^abc]`       | Matches any char **except** 'a', 'b', or 'c' |
| `[a-z]`        | Lowercase letters                            |
| `[A-Z]`        | Uppercase letters                            |
| `[0-9]`        | Digits                                       |
| `[a-zA-Z0-9_]` | Alphanumeric + underscore                    |

---

## 🔢 Predefined Character Sets (Shortcuts)

| Pattern | Description                      |
| ------- | -------------------------------- |
| `\d`    | Digit = `[0-9]`                  |
| `\D`    | Non-digit                        |
| `\w`    | Word character = `[a-zA-Z0-9_]`  |
| `\W`    | Non-word character               |
| `\s`    | Whitespace (space, tab, newline) |
| `\S`    | Non-whitespace                   |

---

## 🪄 Anchors & Boundaries

| Pattern    | Description         |
| ---------- | ------------------- |
| `^`        | Start of string     |
| `$`        | End of string       |
| `\b`       | Word boundary       |
| `\B`       | Not a word boundary |
| `(?=...)`  | Positive lookahead  |
| `(?!...)`  | Negative lookahead  |
| `(?<=...)` | Positive lookbehind |
| `(?<!...)` | Negative lookbehind |

---

## 🎭 Groups & Capturing

| Pattern         | Description         |
| --------------- | ------------------- |
| `(abc)`         | Capture group       |
| `(?:abc)`       | Non-capturing group |
| `(?P<name>...)` | Named group         |
| `\1`, `\2`      | Backreferences      |

---

## 🔁 Regex Functions in `re` module

```python
re.search(pattern, string)      # First match anywhere
re.match(pattern, string)       # Match only at beginning
re.fullmatch(pattern, string)   # Match whole string
re.findall(pattern, string)     # List of all matches
re.finditer(pattern, string)    # Iterator of Match objects
re.sub(pattern, repl, string)   # Replace pattern with repl
re.split(pattern, string)       # Split string by pattern
```

---

## 🧪 Match Object Methods

```python
match.group()       # Return matched string
match.group(n)      # Group by index
match.groups()      # All groups as tuple
match.groupdict()   # Named groups as dict
match.start(), match.end()  # Start/end index
```

---

## 🧩 Flags

| Flag                     | Description                          |
| ------------------------ | ------------------------------------ |
| `re.IGNORECASE` / `re.I` | Case-insensitive                     |
| `re.MULTILINE` / `re.M`  | `^` and `$` match start/end of lines |
| `re.DOTALL` / `re.S`     | `.` matches newline                  |
| `re.VERBOSE` / `re.X`    | Allow comments and whitespace        |

Example:

```python
re.search(r"(?i)^abc", "ABC")  # Case-insensitive match
```

---

## 🔍 Common Regex Patterns

| Task              | Regex                                 |
| ----------------- | ------------------------------------- |
| Email             | `[\w.-]+@[\w.-]+\.\w+`                |
| URL               | `https?://[\w./-]+`                   |
| Phone (US)        | `\(?\d{3}\)?[-.\s]?\d{3}[-.\s]?\d{4}` |
| Date (YYYY-MM-DD) | `\d{4}-\d{2}-\d{2}`                   |
| HTML Tag          | `<[^>]+>`                             |
| Integer           | `-?\d+`                               |
| Float             | `-?\d+\.\d+`                          |