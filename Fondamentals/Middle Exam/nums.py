def add_func(values, number_list):
    number_list.append(value)
    return number_list


def remove_func(values, number_list):
    if values in number_list:
        for item in number_list:
            if item == values:
                number_list.remove(values)
                break
    return number_list


def replace_func(values, replacements, number_list):
    if values in number_list:
        for item in number_list:
            if item==value:
                index=number_list.index(item)
                number_list[index]=replacements
                break
    return number_list


def collapse_func(values, number_list):
    new_list = []
    for item in number_list:
        if item >= values:
            new_list.append(item)
    return new_list


numbers = list(map(int, input().split()))
while True:
    data = input().split()
    command = data[0]
    if command == "Finish":
        break
    value = int(data[1])
    if command == "Add":
        numbers = add_func(value, numbers)
    elif command == "Remove":
        numbers = remove_func(value, numbers)
    elif command == "Replace":
        replacement = int(data[2])
        numbers = replace_func(value, replacement, numbers)
    elif command == "Collapse":
        numbers = collapse_func(value, numbers)
print(" ".join(str(st) for st in numbers))
