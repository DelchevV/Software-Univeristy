destination=input()
packet=input()
is_vip=input()
sleepovers=int(input())
price_per_day=0
if (destination=="Bansko" or destination=="Borovets" or destination=="Varna" or destination=="Burgas") and (packet=="noEquipment" or packet=="withEquipment" or packet=="noBreakfast" or packet=="withBreakfast"):
    if sleepovers<1:
        print("Days must be positive number!")
        exit()
    if destination=="Bansko" or destination=="Borovets":
        if packet=="withEquipment":
            price_per_day=100
        elif packet=="noEquipment":
            price_per_day=80
    elif destination=="Varna" or destination=="Burgas":
        if packet=="withBreakfast":
            price_per_day=130
        elif packet=="noBreakfast":
            price_per_day=100
    if sleepovers>7:
        sleepovers-=1
    total=sleepovers*price_per_day
    if is_vip=="yes" and destination=="Bansko":
        total*=0.9
    elif is_vip=="yes" and destination=="Borovets":
        total*=0.95
    elif is_vip=="yes" and destination=="Varna":
        total*=0.88
    elif is_vip=="yes" and destination=="Burgas":
        total*=0.93
    print(f"The price is {total:.2f}lv! Have a nice time!")
else:
    print("Invalid input!")
