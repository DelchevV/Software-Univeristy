chicken_price=10.35
fish_price=12.40
veg_price=8.15
delivery=2.50

chicken=int(input())
fish=int(input())
veg=int(input())

main_meal_cost=chicken*chicken_price + fish*fish_price + veg*veg_price
desert=main_meal_cost*0.2
total=desert+main_meal_cost+delivery

print(total)
