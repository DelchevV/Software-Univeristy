movie_budget=float(input())
statists=int(input())
price_per_cloth=float(input())

decor=movie_budget*0.1
if statists>150:
    price_per_cloth*=0.9
total=statists*price_per_cloth+decor
diffrence=abs(total-movie_budget)
if total>movie_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {diffrence:.2f} leva more.")
else:
    print("Action!")
    print(f"Wingard starts filming with {diffrence:.2f} leva left.")
