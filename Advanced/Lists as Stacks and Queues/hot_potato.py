from collections import deque

queue= deque(input().split())
toss=int(input())
counter=1

while len(queue)>1:
    kid=queue.popleft()
    if counter==toss:
        counter=1
        print(f'Removed {kid}')
    else:
        counter+=1
        queue.append(kid)
print(f'Last is {queue[0]}')