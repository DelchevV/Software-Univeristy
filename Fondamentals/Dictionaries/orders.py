orders={}
while True:
    data=input().split()
    command=data[0]

    if command=="buy":
        break

    product=data[0]
    price=float(data[1])
    quantity=int(data[2])

    if product not in orders:
        orders[product]=[price,quantity]
    elif product in orders and orders[product][0]!=price:
        orders[product][0]=price
        orders[product][1] += quantity
    else:
        orders[product][1]+=quantity

for key in orders:
    price_of_item=orders[key][0]
    quantity_of_itme=orders[key][1]
    orders[key]=price_of_item*quantity_of_itme

for key,value in orders.items():
    print(f"{key} -> {value:.2f}")
