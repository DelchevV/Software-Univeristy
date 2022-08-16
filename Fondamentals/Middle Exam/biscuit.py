import math

number_of_biscuits = int(input())
workers = int(input())
other_factory_production = int(input())
total_biscuits = 0
for day in range(1, 30 + 1):
    daily_production = number_of_biscuits * workers
    if day % 3 == 0:
        daily_production *= 0.75
    total_biscuits += daily_production

result=0
a=total_biscuits
b=other_factory_production
if a>b or b>a:
    result=100*abs(a-b)/((a+b)/2)

print(f"You have produced {math.floor(total_biscuits)} biscuits for the past month.")
if total_biscuits > other_factory_production:
    print(f"You produce {result:.2f} percent more biscuits.")
else:

    print(f"You produce {result:.2f} percent less biscuits.")
