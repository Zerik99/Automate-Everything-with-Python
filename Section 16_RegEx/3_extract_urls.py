"""a simple app to extract urls from a file"""
import re
from pathlib import Path

files_dir = Path("Section 16_RegEx/files/lecture_3")

for file in files_dir.glob("*.txt"):
    with open(file, "r", encoding="utf-8") as f:
        contents = f.read()
        pattern = re.compile(r"https?://(?:www\.)?(\w+)(\.com|\.org)")

        # Here is the explanation for the code above:
        # 1. re.compile(r"") is a function that creates a regex object. It is useful if you
        #     want to use the same regex expression several times.

        # 2. r"" is the raw string notation. It means that backslashes are not treated as
        #     escape characters. It is useful when you have a lot of backslashes in your
        #     regex expression.

        # 3. https?:// matches http:// or https://

        # 4. (www\.)? matches www. or nothing

        # 5. (\w+) matches any word character (a-z, A-Z, 0-9, _)

        # 6. (\.\w+) matches a dot and any word character (a-z, A-Z, 0-9, _)

        matches = pattern.finditer(contents)
        for match in matches:
            print(match.group(0))

        # Here is the explanation for the code above:
        # 1. re.compile(pattern, flags=0) --> Compile a regular expression pattern
        #     into a regular expression object, which can be used for matching
        #     using its match() and search() methods, described below.

        # 2. re.finditer(pattern, string, flags=0) --> Return an iterator yielding
        #     match objects over all non-overlapping matches for the RE pattern in
        #     string. The string is scanned left-to-right, and matches are returned
        #     in the order found. Empty matches are included in the result.

        # 3. match.group(0) --> Return the string matched by the RE
