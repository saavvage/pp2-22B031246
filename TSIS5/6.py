import re

text = "Hello, professor. How are you?"
pattern = r'[ ,\.]+'
new_text = re.sub(pattern, ':', text)
print(new_text)