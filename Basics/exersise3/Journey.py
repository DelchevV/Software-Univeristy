budget=float(input())
seasson=input()
price=0
destination=" "
type_of_destination=" "
if budget <=100:
    if seasson=="summer":
        price=budget*0.30
        destination="Bulgaria"
        type_of_destination="Camp"
    elif seasson=="winter":
        price=budget*0.7
        destination = "Bulgaria"
        type_of_destination = "Hotel"
elif budget <=1000:
    if seasson=="summer":
        price=budget*0.40
        destination = "Balkans"
        type_of_destination = "Camp"
    elif seasson=="winter":
        price=budget*0.80
        destination = "Balkans"
        type_of_destination = "Hotel"
elif budget>1000:
    price=budget*0.9
    destination = "Europe"
    type_of_destination = "Hotel"

print(f"Somewhere in {destination}" )
print(f"{type_of_destination} - {price:.2f}")

