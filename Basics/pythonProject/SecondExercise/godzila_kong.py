budget=float(input())
statists=int(input())
price_per_unit=float(input())

decor=budget*0.1
dress_price=price_per_unit*statists
if statists>150:
    dress_price=dress_price*0.9
total=dress_price+decor
if total>budget:
    missing=total-budget
    print("Not enough money!")
    print(f"Wingard needs {missing:.2f} leva more.")
else:
    spare=abs(total-budget)
    print("Action!")
    print(f"Wingard starts filming with {spare:.2f} leva left.")


