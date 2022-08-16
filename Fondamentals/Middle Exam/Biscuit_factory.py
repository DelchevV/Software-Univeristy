import math

number_of_biscuits=int(input())
workers=int(input())
other_factory_production=int(input())
total_biscuits=0
for day in range(1,30+1):
    daily_production = number_of_biscuits * workers
    if day%3==0:
        daily_production*=0.75
    total_biscuits+=daily_production



other_factory_one_percent=other_factory_production/100
total_biscuits_one_percent=total_biscuits/100
result=(other_factory_one_percent-total_biscuits_one_percent)*100
print(result)
diff=total_biscuits-other_factory_production

# percent=diff/other_factory_production * 100
# print(f"You have produced {math.floor(total_biscuits)} biscuits for the past month.")
# if other_factory_production<total_biscuits:
#     print(f'You produce {percent:.2f} percent more biscuits.')
# elif other_factory_production>total_biscuits:
#     print(f"You produce {abs(percent):.2f} percent less biscuits.")

