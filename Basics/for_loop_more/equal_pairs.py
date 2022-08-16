import sys

count=int(input())
max=-sys.maxsize
min=sys.maxsize
sum=0
for i in range(count):
    first_pair=int(input())
    second_pair=int(input())
    sum=first_pair+second_pair
    if sum>max:
        max=sum
    elif sum<min:
        min=sum

print(f"Yes, value = {sum}")
