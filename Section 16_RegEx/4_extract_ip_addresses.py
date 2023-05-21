"""a simple app to demonstrate regex and extracting IP addresses"""
import re
from pathlib import Path

pattern = re.compile(r"(\d{1,3})\.(\d{1,3})\.(\d{1,3})\.(\d{1,3})")

# Here is the explanation for the code above:
# 1. The \d{1,3} regex matches one to three digits.
# 2. Since \d matches only one digit, \d{1,3} matches one to three digits.
# 3. The periods need to be escaped with a backslash, so they need to be
#    surrounded with escape characters: \.
# 4. The regex doesn’t match to strings like 4444.11.11.11, because the
#    regex requires that the IP address has exactly three digits and not four digits.

files_dir = Path("Section 16_RegEx\\files\\lecture4")

for file in files_dir.glob("*.txt"):
    with open(file, "r", encoding="utf-8") as f:
        contents = f.read()
        matches = pattern.finditer(contents)
        for match in matches:
            print(match.group(0))
