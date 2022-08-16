import re

total_cost = 0
furniture = []
pattern = r'>>(\w+)<<(\d+\.?\d+)!(\d+)'
line = input()
while line != "Purchase":
    matches = re.match(pattern, line)
    if matches:
        furniture.append(matches[1])
        total_cost+=int(matches[3])*float(matches[2])
    line=input()
print('Bought furniture:')
for piece in furniture:
    print(piece)
print(f'Total money spend: {total_cost:.2f}')
