import math

expression=input().split()
numbers=[]
for ch in expression:
    if ch.lstrip("-").isdigit() :
        numbers.append(int(ch))
    elif ch=="-":
        first_num=numbers.pop(0)
        while numbers:
            first_num-=numbers.pop(0)
        numbers.append(first_num)
    elif ch=="+":
        first_num=numbers.pop(0)
        while numbers:
            first_num+=numbers.pop()
        numbers.append(first_num)
    elif ch=="*":
        first_num = numbers.pop(0)
        while numbers:
            first_num *= numbers.pop()
        numbers.append(first_num)
    elif ch=='/':
        first_num = numbers.pop(0)
        while numbers:
            first_num /= numbers.pop()
        numbers.append(math.floor(first_num))

print(*numbers)