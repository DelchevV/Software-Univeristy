import math

visitors=int(input())
tax=float(input())
price_sun_chair=float(input())
price_per_umbrella=float(input())
needed_sun_chairs=math.ceil(visitors*0.75)
needed_umbrellas=math.ceil(visitors/2)
total=(visitors*tax)+(price_per_umbrella*needed_umbrellas)+(price_sun_chair*needed_sun_chairs)
print(f"{total:.2f} lv.")