import re

text = "SplitThisSentencesAtUpperCaseLetters"
pattern = r'[A-Z]'
result = re.split(pattern, text)
print(result)
