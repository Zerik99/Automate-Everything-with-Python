from pathlib import Path

p1 = Path("Section 4_Working with Computer Files and Folders/files/abc.txt")

p2 = Path("Section 4_Working with Computer Files and Folders/files/def.txt")

print(type(p1))

if p1.exists():
    with open(p1, "r") as f:
        print(f.read())

# this code is supposed to generate a file if it doesn't exist. But it doesn't work.
# not sure why at the moment.
# answer: It works now, I needed to adjust the relative path to the file.
if not p2.exists():
    with open(p2, "w") as f:
        f.write("This is a test.")

if p2.exists():
    with open(p2, "r") as f:
        print(f.read())

print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path("Section 4_Working with Computer Files and Folders/files")
print(list(p2.iterdir()))
