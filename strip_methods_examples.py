"""
# Whitespace Characters and Escape Sequences:
#
# | Character       | Description            | Escape Character | Is it an escape sequence? |
# |-----------------|------------------------|------------------|----------------------------|
# | Space           | ' ' (space)            | No               | No                         |
# | Tab             | Horizontal tab         | \t               | Yes                        |
# | Newline         | Line break             | \n               | Yes                        |
# | Carriage return | Older line break       | \r               | Yes                        |
# | Form feed       | Page break             | \f               | Yes                        |
# | Vertical tab    | Vertical spacing       | \v               | Yes                        |

repr() is used to show the string with escape characters
"""

text = " \t\n  Hello, World!  \n\t "  # Whitespace on both ends

# strip() - removes all leading and trailing whitespace
print("Original text:", repr(text))
print("Using strip():", repr(text.strip()))  # "Hello, World!"

# lstrip() - removes leading (left) whitespace only
print("Using lstrip():", repr(text.lstrip()))  # "Hello, World!  \n\t "

# rstrip() - removes trailing (right) whitespace only
print("Using rstrip():", repr(text.rstrip()))  # " \t\n  Hello, World!"

# --- Strip specific characters instead of whitespace ---

custom_text = "---Hello, World!---"

# strip('-') removes '-' from both ends
print("Strip '-' from both ends:", repr(custom_text.strip("-")))  # "Hello, World!"

# lstrip('-') removes '-' only from the left
print("lstrip('-'):", repr(custom_text.lstrip("-")))  # "Hello, World!---"

# rstrip('-') removes '-' only from the right
print("rstrip('-'):", repr(custom_text.rstrip("-")))  # "---Hello, World!"

# Strip multiple characters (e.g., x, *, y, space)
messy = "x*y Hello Python y*x"
# Removes any of 'x', '*', 'y', or ' ' from both ends
print("Strip multiple characters:", repr(messy.strip("x*y ")))  # "Hello Python"
