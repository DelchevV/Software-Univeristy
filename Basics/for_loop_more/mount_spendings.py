months=int(input())
electricity=0
water=months*20
internet=months*15
others=0
average=0
total=0
electricity_now=0

others_el=0
others_water=0
others_interntet=0

for i in range(months):
    electricity_now=float(input())
    electricity+=electricity_now
    others+=electricity_now
    others+=water
    others+=internet
    others*=0.2

total+=electricity+water+internet+others
average=total/months
print(f"Electricity: {electricity:.2f} lv")
print(f"Water: {water:.2f} lv")
print(f"Internet: {internet:.2f} lv")
print(f"Other: {others:.2f} lv")
print(f"Average: {average:.2f} lv")