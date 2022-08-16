def shoot_fun(index, power, targets):
    if 0 <= index < len(targets):
        if targets[index]-power <=0:
            targets.pop(index)
        else:
            targets[index] -= power
    return targets


def add_func(index, value, targets):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike_func(index, radius, targets):
    validator_index = index - radius >= 0 and index + radius<= len(targets)
    if validator_index:
        start_index = index - radius
        end_index = index + radius
        targets = [targets[i] for i in range(len(targets)) if i < start_index or i > end_index]
    else:
        print("Strike missed!")
    return targets


targets = list(map(int, input().split()))
while True:
    data = input().split()
    command = data[0]
    if command == "End":
        print("|".join(str(st) for st in targets))
        break
    first_input = int(data[1])
    second_input = int(data[2])

    if command == "Shoot":
        targets = shoot_fun(first_input, second_input, targets)
    elif command == "Add":
        targets = add_func(first_input, second_input, targets)
    elif command == "Strike":
        targets = strike_func(first_input, second_input, targets)
