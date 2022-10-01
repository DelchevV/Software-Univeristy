stack=list()
result=[]
number_of_lines=int(input())
for line in range(number_of_lines):
    entry=input().split()
    number=int(entry[0])
    if number==1:
        stack.append(int(entry[1]))
    elif number==2:
        if len(stack)>0:
            stack.pop()
    elif number==3:
        if stack:
            print(max(stack))
    elif number==4:
        if stack:
            print(min(stack))
for _ in range(len(stack)):
    result.append(str(stack.pop()))
print(', '.join(result))
