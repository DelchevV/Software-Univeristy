numbers=tuple(map(float,input().split()))

unique_nums=[]
for num in numbers:
    if num not in unique_nums:
        unique_nums.append(num)

for num in unique_nums:
    print(f'{num:.1f} - {numbers.count(num)} times')