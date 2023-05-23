"""a simple app to demonstrate metacharacters in regular expressions"""
import re

# examples and description of all RegEx meta Characters:
#   .       - Any Character Except New Line
#   \       - Escape Character, use to escape special characters
#   \d      - Digit (0-9)
#   \D      - Not a Digit (0-9)
#   \w      - Word Character (a-z, A-Z, 0-9, _)
#   \W      - Not a Word Character
#   \s      - Whitespace (space, tab, newline)
#   \S      - Not Whitespace (space, tab, newline)

#   \b      - Word Boundary
#   \B      - Not a Word Boundary
#   ^       - Beginning of a String
#   $       - End of a String

#   []      - Matches Characters in brackets
#   [^ ]    - Matches Characters NOT in brackets
#   |       - Either Or
#   ( )     - Group

# Quantifiers:
#   *       - 0 or More
#   +       - 1 or More
#   ?       - 0 or One
#   {3}     - Exact Number
#   {3,4}   - Range of Numbers (Minimum, Maximum)

# create a string containing emails to search
search_string = """This is a string to search for a regular expression like

    1. here is an email Erikzndr@gmail.com
    2. here is an email rand_om@gmail.com
    3. here is an email fak1eemail@gmail.com
    4. here is an email fake mail @gmail.com"""

pattern = re.compile(r"[^ ]+@[^ ]+\.[a-z]+")
matches = pattern.findall(search_string)
print(matches)
