bakery={}
while True:
    data=input().split(": ")
    command=data[0]
    if command=="statistics":
        break

    product=data[0]
    quantity=data[1]
    if product in bakery:
        bakery[product]+=int(quantity)
    else:
        bakery[product] = int(quantity)

print("Products in stock:")
for prod in bakery:
    print(f"- {prod}: {bakery[prod]}")

total_products=len(bakery)
total_quantity=sum(bakery.values())
print(f"Total Products: {total_products}")
print(f"Total Quantity: {total_quantity}")