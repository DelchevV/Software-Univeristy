puzzle_price=2.60
doll_price=3
bear_price=4.10
minion_price=8.20
truck_price=2

trip_price=float(input())
puzzles=int(input())
dolls=int(input())
bears=int(input())
minions=int(input())
trucks=int(input())

total_puzzle=puzzle_price*puzzles
total_dolls=dolls*doll_price
total_bears=bears*bear_price
total_minions=minions*minion_price
total_trucks=trucks*truck_price
total_price=total_trucks+total_bears+total_dolls+total_puzzle+total_minions
total_pieces=puzzles+dolls+bears+minions+trucks
if total_pieces>=50:
    total_price=total_price*0.75
naem=total_price*0.1
profit=total_price-naem

diffrence = abs(profit - trip_price)

if profit>=trip_price:
    print(f"Yes! {diffrence:.2f} lv left.")
else:
    print(f"Not enough money! {diffrence:.2f} lv needed.")







