entry=input()
open_brackets_stack=[]
for index in range(len(entry)):
    ch= entry[index]
    if ch =="(":
        open_brackets_stack.append(index)
    elif ch==')':
        start_index=open_brackets_stack.pop()
        print(entry[start_index:index+1])
