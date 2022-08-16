zoo={}
areas={}


def add_func(zoo_d, animal, needed_food, area):
    if animal not in zoo_d:
        zoo_d[animal]=[needed_food,area]
    else:
        zoo_d[animal][0]+=needed_food
    return zoo_d


def feed_func(zoo_d,animal,food):
    if animal in zoo_d:
        zoo_d[animal][0]-=food
        if zoo_d[animal][0]<=0:
            print(f"{animal} was successfully fed")
            del zoo_d[animal]
    return zoo_d


while True:
    entry=input().split(": ")
    command=entry[0]

    if command=="EndDay":
        break

    if command=="Add":
        rest_of_entry=entry[1].split("-")
        animal_name=rest_of_entry[0]
        food_quantity=int(rest_of_entry[1])
        area=rest_of_entry[2]
        zoo=add_func(zoo,animal_name,food_quantity,area)

    elif command=="Feed":
        rest_of_entry = entry[1].split("-")
        animal_name = rest_of_entry[0]
        food_q=int(rest_of_entry[1])
        zoo=feed_func(zoo,animal_name,food_q)

for species in zoo:
    area=zoo[species][1]
    if area in areas:
        areas[area]+=1
    else: areas[area]=1

print("Animals:")
for key in zoo:
    print(f" {key} -> {zoo[key][0]}g")
print("Areas with hungry animals:")

for key in areas:
    print(f" {key}: {areas[key]}")
