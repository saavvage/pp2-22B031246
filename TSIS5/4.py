import re

text = input()
pattern = r'[A-Z][a-z]+'
match = re.match(pattern, text)

if match:
    print("Match found!")
else:
    print("Match not found.")