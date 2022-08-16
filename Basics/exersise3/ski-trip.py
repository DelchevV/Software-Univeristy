days=int(input())
type_of_room=input()
rating=input()

room_for_one=18.00
apartment=25.00
president_apartment=35
sleepovers = days - 1
price=0

if sleepovers<10:
    if type_of_room=="room for one person":
        price=sleepovers*18
    if type_of_room=="apartment":
        price= sleepovers*25*0.70
    if type_of_room=="president apartment":
        price=sleepovers*35*0.90
elif  sleepovers>10 and sleepovers<15:
    if type_of_room=="room for one person":
        price=sleepovers*18
    if type_of_room=="apartment":
        price= sleepovers*25*0.65
    if type_of_room=="president apartment":
        price=sleepovers*35*0.85
elif sleepovers >15:
    if type_of_room=="room for one person":
        price=sleepovers*18
    if type_of_room=="apartment":
        price= sleepovers*25*0.50
    if type_of_room=="president apartment":
        price=sleepovers*35*0.80
if rating=="positive":
    price=price+price*0.25
else:
    price*=0.90
print(f"{price:.2f}")
