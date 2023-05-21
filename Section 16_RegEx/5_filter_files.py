"""a simple app to demonstrate regex and filtering files by name."""
import re
from pathlib import Path
from typing import Any

files_dir = Path("Section 16_RegEx/files/lecture_5")

files = files_dir.iterdir()

pattern = re.compile(r"(nov[a-z]*)-(?:[1-9]|1[0-9]|20)\.([a-z])", re.IGNORECASE)

filenames_str: list[Any] = [file.name for file in files]
print(filenames_str)

matches = [filename for filename in filenames_str if pattern.findall(filename)]

print(matches)
