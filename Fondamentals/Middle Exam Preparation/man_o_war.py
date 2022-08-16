def fire_func(target, damaging, enemy):
    if 0 <= target < len(enemy):
        enemy[target] -= damaging
        if enemy[target] <= 0:
            print("You won! The enemy ship has sunken.")
            exit()
    return enemy


def defend_func(start, end, damages, pirate):
    if 0 <= start < len(pirate) and 0 <= end < len(pirate):
        for section in range(start, end + 1):
            pirate[section] -= damages
            if pirate[section] <= 0:
                print("You lost! The pirate ship has sunken.")
                exit()
    return pirate


def repair_func(indexes, healths, pirate):
    if 0 <= indexes < len(pirate):
        pirate[indexes]+=healths
        if pirate[indexes] > maximum_health:
            pirate[indexes] = maximum_health
    return pirate


def status_func(max_health, pirate):
    need_repair_below = max_health * 0.2
    sections_need_repair = 0
    for item in pirate:
        if item < need_repair_below:
            sections_need_repair += 1
    if sections_need_repair>0:
        print(f"{sections_need_repair} sections need repair.")


pirate_ship = list(map(int, input().split(">")))
warship = list(map(int, input().split(">")))
maximum_health = int(input())

while True:
    data = input().split()
    command = data[0]
    if command == "Retire":
        break

    if command == "Fire":
        index = int(data[1])
        damage = int(data[2])
        warship = fire_func(index, damage, warship)

    elif command == "Defend":
        start_index = int(data[1])
        end_index = int(data[2])
        damage = int(data[3])
        pirate_ship = defend_func(start_index, end_index, damage, pirate_ship)

    elif command == "Repair":
        index = int(data[1])
        health = int(data[2])
        repair_func(index, health, pirate_ship)

    elif command == "Status":
        status_func(maximum_health, pirate_ship)
if len(pirate_ship) and len(warship)>0:
    print(f'Pirate ship status: {sum(pirate_ship)}')
    print(f'Warship status: {sum(warship)}')