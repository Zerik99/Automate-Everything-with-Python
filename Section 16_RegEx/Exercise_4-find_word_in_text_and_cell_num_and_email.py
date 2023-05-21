"""A simple app to find a word in a text file and return the line."""
import re

data = [
    "mr Jim Cloudy, Texas, 01091231, 1 dog 1 cat, jim.cloudy@example.com",
    "mrs Anna Cloudy, Delhi, 2dogs 1fish bathlover@example.com",
    "Mrs. Sarah Prost, Baghdad, +4327629101, 1 hamster, 2 crocodiles",
    "Ms Beta Palm Ontario 08234211 12 cats, beta@example.com",
    "mr. Dog Bells texas 09234211 3 honey badgers alta_bells.example.com",
    "ms. Claudia More, Gujarat, 012311, 3 dogs",
    "mrs Alma Stills Delhi 01231981 1 dog",
    "mr Sen Kumar Delhi 3456 ants",
]

pattern = re.compile(
    r"(.*)(delhi+)(.*)(0|\+[0-1]{4,10}.*|[^ ]+@[a-z]+\.[a-z]+)", re.IGNORECASE
)

matches = [
    line for line in data if pattern.findall(line)
]  # we love list comprehension!!

print(matches)
