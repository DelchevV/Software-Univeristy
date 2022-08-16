import math

area=int(input())
grape_per_sqm=float(input())
needed_wine=int(input())
needed_workers=int(input())

usable_area=area*0.4
total_grape= grape_per_sqm*usable_area
wine=total_grape/2.5
if needed_wine>wine:
    more=needed_wine-wine
    print(f"It will be a tough winter! More {math.floor(abs(more))} liters wine needed.")

else:
    lefts=wine-needed_wine
    per_worker=lefts/needed_workers
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    print(f"{math.floor(lefts)} liters left -> {math.floor(per_worker)} liters per person.")