from  collections import deque
chocolate_stack=list(map(int,input().split(", ")))
cups_queue=deque(map(int,input().split(", ")))

milkshakes=0
while chocolate_stack or cups_queue:
    flag=False
    if milkshakes>=5:
        break
    if chocolate_stack and cups_queue:
        current_chocolate=chocolate_stack.pop()
        current_cup=cups_queue.popleft()
        if current_chocolate<=0:
            if current_cup>0:
                cups_queue.insert(0,current_cup)
            flag=True
        if current_cup <=0:
            if current_chocolate>0:
                chocolate_stack.append(current_chocolate)
            flag=True
        if flag:
            continue
        if current_chocolate == current_cup:
            milkshakes+=1
        else:
            current_chocolate-=5
            chocolate_stack.append(current_chocolate)
            cups_queue.append(current_cup)
    else:
        break
if milkshakes>=5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")


print(f"Chocolate: {', '.join(map(str,chocolate_stack)) if chocolate_stack else 'empty'}")
print(f"Milk: {', '.join(map(str,cups_queue)) if cups_queue else 'empty'}")