from collections import deque

ramens=list(map(int,input().split(", ")))
customers=deque(map(int,input().split(", ")))

while ramens and customers:
    ramen=ramens.pop()
    customer=customers.popleft()

    if ramen==customer:
        continue

    elif ramen>customer:
        ramen-=customer
        ramens.append(ramen)

    elif customer>ramen:
        customer-=ramen
        customers.appendleft(customer)

if len(customers)==0:
    print("Great job! You served all the customers.")
    if any(ramens):
        print(f'Bowls of ramen left: {", ".join(map(str, ramens))}')

else:
    print("Out of ramen! You didn't manage to serve all customers.")
    if any(customers):
        print(f'Customers left: {", ".join(map(str, customers))}')
