budget=float(input())
seasson=input()
price=0
car=" "
bundle=" "

if budget <=100:
    bundle="Economy class"
    if seasson=="Summer":
        car="Cabrio"
        price=budget*0.35
    elif seasson=="Winter":
        car="Jeep"
        price=budget*0.65
elif budget<=500:
    bundle = "Compact class"
    if seasson == "Summer":
        car = "Cabrio"
        price = budget * 0.45
    elif seasson == "Winter":
        car = "Jeep"
        price = budget * 0.80
elif budget>500:
    bundle = "Luxury class"
    car = "Jeep"
    price = budget * 0.90
print(bundle)
print(f"{car} - {price:.2f}")
