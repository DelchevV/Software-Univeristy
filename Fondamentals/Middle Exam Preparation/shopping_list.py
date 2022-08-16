# You will receive an initial list with groceries separated by an exclamation mark "!".
# After that, you will be receiving 4 types of commands until you receive "Go Shopping!".
# •	"Urgent {item}" - add the item at the start of the list.  If the item already exists, skip this command.
# •	"Unnecessary {item}" - remove the item with the given name, only if it exists in the list. Otherwise, skip this command.
# •	"Correct {oldItem} {newItem}" - if the item with the given old name exists, change its name with the new one. Otherwise, skip this command.
# •	"Rearrange {item}" - if the grocery exists in the list, remove it from its current position and add it at the end of the list. Otherwise, skip this command


def urgent_func(items, foods):
    if items not in foods:
        foods.insert(0, items)
    return foods


def unnecessary_func(items, foods):
    if items in foods:
        foods.remove(items)
    return foods


def correct_func(old, new, foods):
    if old in foods:
        index = foods.index(old)
        foods[index] = new
    return foods


def rearrange_func(items, foods):
    if items in foods:
        index = foods.index(items)
        poped_item=foods.pop(index)
        foods.append(poped_item)
    return foods


food_list = input().split("!")

while True:
    data = input().split()
    command = data[0]

    if command == "Go":
        break
    item = data[1]
    if command == "Urgent":
        food_list = urgent_func(item, food_list)
    elif command == "Unnecessary":
        food_list = unnecessary_func(item, food_list)
    elif command == "Correct":
        old_item = data[1]
        new_item = data[2]
        food_list = correct_func(old_item, new_item, food_list)
    elif command == "Rearrange":
        food_list=rearrange_func(item,food_list)
print(", ".join(food_list))
