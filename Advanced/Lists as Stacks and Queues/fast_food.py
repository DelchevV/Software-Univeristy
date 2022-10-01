from collections import deque

quantity=int(input())
entry=input().split()
entry=[int(i) for i in entry]
entry=deque(entry)

print(max(entry))

for _ in range(len(entry)):
    if entry[0] <=quantity:
        current_order=entry.popleft()
        quantity-=current_order
    else:
        break


    # if entry[0]<quantity:
    #     current_quantity=int(entry.popleft())
    #     if quantity - current_quantity<=0:
    #         break
    #
    #     else:
    #         quantity-=current_quantity
if len(entry)>0:
    entry=[str(i) for i in entry]
    print(f"Orders left: {' '.join(entry)}")
elif len(entry)==0:
    print('Orders complete')


