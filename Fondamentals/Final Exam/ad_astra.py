import re


total_cal=0
pattern=r"([\#\|])([A-Za-z\s]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d+)\1"
text=input()
matches=re.findall(pattern,text)
for match in matches:
    total_cal+=int(match[3])
print(f"You have food to last you for: {int(total_cal/2000)} days!")
for match in matches:
    print(f"Item: {match[1]}, Best before: {match[2]}, Nutrition: {match[3]}")