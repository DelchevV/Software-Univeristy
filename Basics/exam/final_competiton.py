dancers=int(input())
points=float(input())
season=input()
place=input()
expenses_percent=0
reward=0
charity=0
if season=="summer":
    if place=="Bulgaria":
        expenses_percent=0.95
    elif place=="Abroad":
        expenses_percent=0.9
elif season=="winter":
    if place=="Bulgaria":
        expenses_percent=0.92
    elif place=="Abroad":
        expenses_percent=0.85
if place=="Bulgaria":
    reward=points*dancers
elif place=="Abroad":
    reward=points*dancers
    reward+=reward/2
reward*=expenses_percent
charity=reward*0.75
money_per_dancer=(reward-charity)/dancers
print(f"Charity - {charity:.2f}")
print(f"Money per dancer - {money_per_dancer:.2f}")