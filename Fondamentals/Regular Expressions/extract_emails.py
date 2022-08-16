import re
pattern=r'\s(([A-Za-z0-9]+)([\-\.\_][A-Za-z0-9]+)*@[\-a-z]+(\.[\-a-z]+)+)\b'
sentence=input()
matches=re.findall(pattern,sentence)
for match in matches:
    print(match[0])
