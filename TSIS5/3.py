import re

text = input()
pattern = r'[a-z]+_[a-z]+'
match = re.match(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")