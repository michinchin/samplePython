import re

#program to try out regular expressions

pattern = "my name is"
text = "Hello my name is 080808"

if re.search(pattern, text):
    print("found a match")

patt2 = ["ch1829","chE8934","ch8234"]
