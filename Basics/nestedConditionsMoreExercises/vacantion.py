budget=float(input())
seasson=input()
location=" "
house_type=" "
price=0

if budget<=1000:
    house_type="Camp"
    if seasson=="Summer":
        location="Alaska"
        price=budget*0.65
    elif seasson=="Winter":
        location="Morocco"
        price=budget*0.45
elif budget<=3000:
    house_type = "Hut"
    if seasson == "Summer":
        location="Alaska"
        price = budget * 0.80
    elif seasson == "Winter":
        location="Morocco"
        price = budget * 0.60
elif budget>3000:
    house_type = "Hotel"
    if seasson == "Summer":
        location = "Alaska"
        price = budget * 0.90
    elif seasson == "Winter":
        location = "Morocco"
        price = budget * 0.90

print(f"{location} - {house_type} - {price:.2f}")