hrizantemi=int(input())
rozi=int(input())
laleta=int(input())
season=input()
is_holiday=input()

all_flowers=hrizantemi+rozi+laleta
price=0

if season=="Spring" or season=="Summer":
    if laleta>7:
        price= (hrizantemi*2+rozi*4.10+laleta*2.50)*0.95
    else:
        price = (hrizantemi * 2 + rozi * 4.10 + laleta * 2.50)
elif season=="Autumn" or season=="Winter":
    if rozi>=10:
        price= (hrizantemi*3.75+rozi*4.50+laleta*4.15)*0.90
    else:
        price = (hrizantemi * 3.75 + rozi * 4.50 + laleta * 4.15)
if is_holiday=="Y":
    price=price+price*0.15
if all_flowers>20:
    price=price-price*0.20
else:
    pass
price+=2
print(f"{price:.2f}")