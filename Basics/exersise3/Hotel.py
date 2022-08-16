mounth=input()
sleepovers=int(input())
studio=0
apartment=0
price_apartment=0
price_studio=0

if mounth=="May" or mounth=="October":
    studio=50
    apartment=65
    if sleepovers > 7 and sleepovers < 14:
        price_studio = (studio * sleepovers) * 0.95
    elif  sleepovers > 14:
        price_studio = studio * sleepovers * 0.70
    else:
        price_studio = studio * sleepovers
    if sleepovers>14:
        price_apartment=apartment*sleepovers*0.90
    else:
        price_apartment = apartment * sleepovers
elif mounth=="June" or mounth=="September":
    studio=75.20
    apartment=68.70
    if sleepovers > 14:
        price_studio = studio * sleepovers * 0.80
    else:
        price_studio = studio * sleepovers
    if sleepovers > 14:
        price_apartment = apartment * sleepovers * 0.90
    else:
        price_apartment = apartment * sleepovers
elif mounth=="July" or mounth=="August":
    studio = 76
    apartment = 77
    price_studio = studio * sleepovers
    if sleepovers > 14:
        price_apartment = apartment * sleepovers * 0.90
    else:
        price_apartment = apartment * sleepovers

print(f"Apartment: {price_apartment:.2f} lv.")
print(f"Studio: {price_studio:.2f} lv.")