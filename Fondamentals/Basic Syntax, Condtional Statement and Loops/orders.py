number_of_orders=int(input())
total=0
for current_order in range(1,number_of_orders+1):
    price_per_capsule = float(input())
    days = int(input())
    needed_capsules = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif needed_capsules < 1 or needed_capsules > 2000:
        continue
    current_order_price=(price_per_capsule*needed_capsules)*days
    total+=current_order_price
    print(f"The price for the coffee is: ${current_order_price:.2f}")
print(f"Total: ${total:.2f}")
