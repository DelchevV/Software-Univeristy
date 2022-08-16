product=input()
town=input()
quantity=float(input())
amount=0
if town=="Sofia":
    if product=="coffee":
        amount=0.50
    elif product=="water":
        amount=0.80
    elif product=="beer":
        amount=1.20
    elif product=="sweets":
        amount=1.45
    elif product=="peanuts":
        amount=1.60
elif town=="Plovdiv":
    if product=="coffee":
        amount=0.40
    elif product=="water":
        amount=0.70
    elif product=="beer":
        amount=1.15
    elif product=="sweets":
        amount=1.30
    elif product=="peanuts":
        amount=1.50
elif town == "Varna":
    if product=="coffee":
        amount=0.45
    elif product=="water":
        amount=0.70
    elif product=="beer":
        amount=1.10
    elif product=="sweets":
        amount=1.35
    elif product=="peanuts":
        amount=1.55
price=amount*quantity
print(f"{price}")