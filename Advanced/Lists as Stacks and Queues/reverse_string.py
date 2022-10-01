line=input()
stack=[]
for index in range(len(line)):
    stack.append(line[index])

while len(stack)>0:
    print(stack.pop(),end='')