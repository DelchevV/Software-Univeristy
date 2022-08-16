import re

regex = r'\b(?P<day>\d{2})([-.\/])(?P<month>[A-Z]{1}[a-z]{2})\2(?P<year>\d{4})\b'
text=input()
matches=re.findall(regex,text)
for match in matches:
    print(f"Day: {match[0]}, Month: {match[2]}, Year: {match[3]}")
