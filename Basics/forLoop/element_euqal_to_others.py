import sys

n=int(input())
max=-sys.maxsize
sum=0
for i in range(n):
    num=int(input())
    sum += num
    if num>max:
        max=num

sum-=max

diff=abs(sum-max)

if sum==max:
    print("Yes")
    print(f"Sum = {sum}")
else:
    print("No")
    print(f"Diff = {diff}")