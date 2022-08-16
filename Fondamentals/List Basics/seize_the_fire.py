list_of_fires=input().split("#")
water=int(input())
effort=0
total_fire=0

print("Cells:")
for element in list_of_fires:
    if water<0:
        break
    is_valid_fire=False
    current_fire=element.split(" = ")
    type_of_fire=current_fire[0]
    range_of_fire=int(current_fire[-1])
    if water<int(range_of_fire):
        continue
    if type_of_fire== "Low" and 1 <= range_of_fire <= 50:
        is_valid_fire=True
    elif type_of_fire=="Medium" and 51<=range_of_fire<=80:
        is_valid_fire=True
    elif type_of_fire=="High" and 81<=range_of_fire<=125:
        is_valid_fire=True
    if is_valid_fire:
        current_water=range_of_fire
        water-=range_of_fire
        effort+=current_water*0.25
        total_fire+=range_of_fire
        print(f" - {range_of_fire}")
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")
