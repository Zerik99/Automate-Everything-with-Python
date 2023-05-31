import json

file = open("Section 28_miscellaneous/files/data.json")
data = json.load(file)


def define(_word):
    if word in data:
        return data[_word]
    else:
        return "The word doesn't exist. Please double check it."


word = input("Enter a word: ")
output = define(word)
print(output)
