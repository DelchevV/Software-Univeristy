lugage=int(input())
price=0
bus=0
truck=0
train=0
tons=0
for i in range(lugage):
    weight=int(input())
    if weight<=3:
        price+=weight*200
        bus+=weight
    elif weight<=11:
        price += weight * 175
        truck+=weight
    elif weight>=12:
        price += weight * 120
        train+=weight
    tons+=weight
average_price_per_ton=price/tons
print(f"{average_price_per_ton:.2f}")
print(f"{bus/tons*100:.2f}%")
print(f"{truck/tons*100:.2f}%")
print(f"{train/tons*100:.2f}%")
