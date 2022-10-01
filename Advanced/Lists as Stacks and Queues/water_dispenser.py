from collections import deque

queue = deque()
total_water=int(input())

while True:
    line=input()
    if line=="Start":
        break
    queue.append(line)

while True:
    line=input()
    if line=="End":
        break
    command=line.split(" ")

    if len(command)>1:
        total_water+=int(command[1])
    if len(command)==1:
        person=queue.popleft()
        liters=int(command[0])
        if liters<=total_water:
            total_water-=liters
            print(f'{person} got water')
        else:
            print(f'{person} must wait')
print(f'{total_water} liters left')
