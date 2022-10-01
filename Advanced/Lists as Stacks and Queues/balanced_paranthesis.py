entry=input()
stack=[]
bool=True
for index in range(len(entry)):
    ch=entry[index]
    if ch == "(" or ch == "[" or ch=="{":
       stack.append(ch)
    elif ch==')':
        if stack:
            if stack[-1]!="(":
                bool=False
                break
            else:
                stack.pop()
        else:
            bool = False
            break
    elif ch == "]":
        if stack:
            if stack[-1] != "[":
                bool = False
                break
            else:
                stack.pop()
        else:
            bool = False
            break
    elif ch == '}':
        if stack:
            if stack[-1]!="{":
                bool=False
                break
            else:
                stack.pop()
        else:
            bool = False
            break

print("YES" if bool else  "NO")