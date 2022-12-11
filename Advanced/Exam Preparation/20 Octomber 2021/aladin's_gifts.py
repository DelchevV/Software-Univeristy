from collections import deque

materials = list(map(int, input().split()))
magic_lvl = deque(map(int, input().split()))

gifts = {
    "Gemstone": 0,
    "Porcelain Sculpture": 0,
    "Gold": 0,
    "Diamond Jewellery": 0
}

while magic_lvl and materials:

    material = materials.pop()
    magic = magic_lvl.popleft()
    sum = material + magic

    if sum < 100:
        if sum % 2 == 0:
            sum = magic * 3 + material * 2
        else:
            sum *= 2
    elif sum > 499:
        sum /= 2

    if 100 <= sum <= 199:
        gifts["Gemstone"] += 1
    elif 200 <= sum <= 299:
        gifts["Porcelain Sculpture"] += 1
    elif 300 <= sum <= 399:
        gifts['Gold'] += 1
    elif 400 <= sum <= 499:
        gifts["Diamond Jewellery"] += 1

if (gifts["Gemstone"] >= 1 and gifts["Porcelain Sculpture"] >= 1) or (gifts["Gold"] >= 1 and gifts["Diamond Jewellery"] >= 1):
    print("The wedding presents are made!")
else:
    print("Aladdin does not have enough wedding presents.")
if materials:
    print(f'Materials left: {", ".join(map(str,materials))}')
if magic_lvl:
    print(f'Magic left: {", ".join(map(str,magic_lvl))}')

for key, value in sorted(gifts.items(),key=lambda x: x[0]):
    if value>=1:
        print(f'{key}: {value}')


