import re

text = input()
result = re.findall(r"\b[A-Z][a-z]+ [A-Z][a-z]+\b", text)
print(" ".join(result))
