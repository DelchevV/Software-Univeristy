from collections import deque

wrapped_egs=0
eggs=deque(map(int, input().split(', ')))
paper=list(map(int,input().split(', ')))

while eggs and paper:
    current_egg=eggs.popleft()

    if current_egg<=0:
        continue

    if current_egg==13:
        first_paper=paper.pop(0)
        last_paper=paper.pop(-1)
        paper.insert(0,last_paper)
        paper.append(first_paper)
        continue

    current_paper=paper.pop()

    if current_paper+current_egg<=50:
        wrapped_egs+=1

if wrapped_egs>0:
    print(f'Great! You filled {wrapped_egs} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")
if eggs:
    print(f'Eggs left: {", ".join(map(str, eggs))}')
if paper:
    print(f'Pieces of paper left: {", ".join(map(str, paper))}')