type=input()
litres=int(input())

if type=="Gasoline" or type=="Gas" or type=="Diesel":
    if litres>=25:
        print(f"You have enough {type.lower()}.")
    else:
        print(f"Fill your tank with {type.lower()}!")
else:
    print("Invalid fuel!")