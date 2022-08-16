n_lines=int(input())
plants={}
plants_rating={}
for line in range(n_lines):
    entry=input().split("<->")
    plant=entry[0]
    rarity=int(entry[1])
    plants[plant]=rarity
    plants_rating[plant]=[]


def rate_func(plants_dict, plant, rating):
    if plant in plants_dict:
        plants_dict[plant].append(rating)
    else:
        print("error")

    return plants_dict


def update_func(plants_dict,plant,new_rar):
    if plant in plants_dict:
        plants_dict[plant]=new_rar
    else:
        print('error')
    return plants_dict


def reset_func(plants_rar, plant):
    if plant in plants_rar:
        plants_rar[plant]=[]
    else:
        print('error')
    return plants_rar


while True:
    entry=input().split(": ")
    command=entry[0]
    if command=="Exhibition":
        break
    elif command=="Rate":
        rest_info=entry[1].split(" - ")
        plant=rest_info[0]
        rating=int(rest_info[1])
        plants_rating=rate_func(plants_rating,plant,rating)

    elif command=="Update":
        rest_info = entry[1].split(" - ")
        plant = rest_info[0]
        new_rarity = int(rest_info[1])
        plants=update_func(plants,plant,new_rarity)
    elif command=="Reset":
        rest_info = entry[1].split(" - ")
        plant = rest_info[0]
        plants_rating=reset_func(plants_rating,plant)
# print(plants)
# print(plants_rating)
for current_rarity in plants_rating:
    if sum(plants_rating[current_rarity])>0:
        plants_sum_rating=f'{sum(plants_rating[current_rarity])/len(plants_rating[current_rarity]):.2f}'
    else:
        plants_sum_rating=f'{0:.2f}'
    plants_rating[current_rarity]=plants_sum_rating
print("Plants for the exhibition:")
for current_plant in plants:
    print(f'- {current_plant}; Rarity: {plants[current_plant]}; Rating: {plants_rating[current_plant]}')