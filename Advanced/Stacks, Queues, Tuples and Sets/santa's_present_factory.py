from collections import deque
materials_stack=list(map(int,input().split()))
magic_que=deque(map(int,input().split()))
crafted_toys={'Doll':0,'Wooden train':0,'Teddy bear':0,'Bicycle':0}
while materials_stack and magic_que:
    multiplication=materials_stack[-1]*magic_que[0]
    if multiplication==150:
        materials_stack.pop()
        magic_que.popleft()
        if "Doll" not in crafted_toys:
            crafted_toys["Doll"]=0
        crafted_toys['Doll']+=1
    elif multiplication==250:
        materials_stack.pop()
        magic_que.popleft()
        if "Wooden train" not in crafted_toys:
            crafted_toys["Wooden train"]=0
        crafted_toys['Wooden train']+=1
    elif multiplication==300:
        materials_stack.pop()
        magic_que.popleft()
        if "Teddy bear" not in crafted_toys:
            crafted_toys["Teddy bear"] = 0
        crafted_toys['Teddy bear'] += 1
    elif multiplication==400:
        materials_stack.pop()
        magic_que.popleft()
        if "Bicycle" not in crafted_toys:
            crafted_toys["Bicycle"] = 0
        crafted_toys['Bicycle'] += 1
    elif multiplication<0:
        material=materials_stack.pop()
        magic=magic_que.popleft()
        materials_stack.append(material+magic)
    elif multiplication>0:
        magic_que.popleft()
        materials_stack[-1]+=15
    elif materials_stack[-1]==0 or magic_que[0]==0:
        if materials_stack[-1]==0:
            materials_stack.pop()
        if magic_que[0]==0:
            magic_que.popleft()

flag=False
if crafted_toys['Doll']>=1 and crafted_toys["Wooden train"]>=1:
    flag=True
elif crafted_toys["Teddy bear"]>=1 and crafted_toys["Bicycle"]>=1:
    flag=True
if flag:
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if materials_stack:
    result=[]
    while materials_stack:
        result.append(materials_stack.pop())
    print(f'Materials left: {", ".join(map(str,result))}')
if magic_que:
    print(f'Magic left: {", ".join(map(str,magic_que))}')
for key in sorted(crafted_toys):
    if crafted_toys[key]>0:

        print(f'{key}: {crafted_toys[key]}')


