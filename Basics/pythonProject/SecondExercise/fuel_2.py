gasoline_liter=2.22
diesel_liter=2.33
gas_liter=0.93

discount_for_gasoline=0.18
discount_for_diesel=0.12
discount_for_gas=0.08

type_of_fuel=input()
liters=int(input())
club_card=input()



if club_card.lower()=="yes" and type_of_fuel.lower()=="gasoline":
    bill = (gasoline_liter - discount_for_gasoline) * liters
    if liters>=20 and liters <=25:
        bill = bill - bill * 0.08
        print(f"{bill:.2f} lv.")
    elif liters > 25:
        bill = bill - bill * 0.1
        print(f"{bill:.2f} lv.")
    else:
        print(f"{bill:.2f} lv.")
elif club_card.lower()=="yes" and type_of_fuel.lower()=="gas":
    bill = (gas_liter-discount_for_gas)*liters
    if liters >= 20 and liters<= 25:
        bill = bill - bill * 0.08
        print(f"{bill:.2f} lv.")
    elif liters > 25:
        bill = bill - bill * 0.1
        print(f"{bill:.2f} lv.")
    else:
        print(f"{bill:.2f} lv.")
elif club_card.lower()=="yes" and type_of_fuel.lower()=="diesel":
    bill = (diesel_liter - discount_for_diesel) * liters
    if liters >= 20 and liters <= 25:
        bill = bill - bill * 0.08
        print(f"{bill:.2f} lv.")
    elif liters > 25:
        bill = bill - bill * 0.1
        print(f"{bill:.2f} lv.")
    else:
        print(f"{bill:.2f} lv.")
#въвеждане за без карта за отстъпка
elif club_card.lower()=="no" and type_of_fuel.lower()=="gasoline":
    bill=liters*gasoline_liter
    if liters >= 20 and liters <= 25:
        bill = bill - bill * 0.08
        print(f"{bill:.2f} lv.")
    elif liters > 25:
        bill = bill - bill * 0.1
        print(f"{bill:.2f} lv.")
    else:
        print(f"{bill:.2f} lv.")

elif club_card.lower()=="no" and type_of_fuel.lower()=="gas":
    bill = liters * gas_liter
    if liters >= 20 and liters <= 25:
        bill = bill - bill * 0.08
        print(f"{bill:.2f} lv.")
    elif liters > 25:
        bill = bill - bill * 0.1
        print(f"{bill:.2f} lv.")
    else:
        print(f"{bill:.2f} lv.")

else:
    bill = liters * diesel_liter
    if liters>=20 and liters <=25:
        bill=bill-bill*0.08
        print(f"{bill:.2f} lv.")
    elif liters > 25:
        bill = bill - bill * 0.1
        print(f"{bill:.2f} lv.")
    else:
        print(f"{bill:.2f} lv.")



