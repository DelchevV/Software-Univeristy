n=int(input())
left=0
right=0
sum=0
diff=0
for i in range(0,n):
    value=int(input())
    left+=value

for i in range(n):
    value = int(input())
    right += value

if left==right:
    sum=left
    print(f"Yes, sum = {sum}")
else:
    diff=abs(left-right)
    print(f"No, diff = {diff}")