import re

#program to try out regular expressions

pattern = "is [0-9][0-9][0-9][0-9][0-9]"
text = "Hello my name is 080808"

if re.search(pattern, text):
    print("found a match")