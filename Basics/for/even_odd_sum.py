n=int(input())
even=0
odd=0
sum=0
diff=0

for i in range(n):
    num=int(input())
    if i%2==0:
        even+=num
    else:
        odd+=num

sum=even
diff=abs(even-odd)

if even==odd:
    print(f"Yes")
    print(f"Sum = {sum}")
else:
    print(f"No")
    print(f"Diff = {diff}")