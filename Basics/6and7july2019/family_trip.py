budget=float(input())
sleepovers=int(input())
price_per_sleepover=float(input())
percent_extra_spending=float(input())
if sleepovers>7:
    price_per_sleepover*=0.95
needed_money=sleepovers*price_per_sleepover
needed_money+=budget*(percent_extra_spending/100)
diffrence=abs(needed_money-budget)
if needed_money>budget:
    print(f"{diffrence:.2f} leva needed.")
else:
    print(f"Ivanovi will be left with {diffrence:.2f} leva after vacation.")
