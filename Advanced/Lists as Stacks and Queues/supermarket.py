from collections import deque
queue=deque()
while True:
    line=input()
    if line=="End":
        break
    if line=="Paid":
        print('\n'.join(queue))
        queue.clear()
    else:
        queue.append(line)
print(f'{len(queue)} people remaining.')