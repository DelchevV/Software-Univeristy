def total_price_func(product, quantity):
    price=0
    if product=="coffee":
       price=1.50
    elif product=="coke":
        price=1.40
    elif product=="water":
        price=1.00
    elif product=="snacks":
        price=2.00
    result=quantity*price
    return f"{result:.2f}"

input_product=input()
input_quantity=int(input())
print(total_price_func(input_product,input_quantity))