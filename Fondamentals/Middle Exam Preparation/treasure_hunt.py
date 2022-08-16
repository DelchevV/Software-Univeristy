# The pirates need to carry a treasure chest safely back to the ship, looting along the way.
# Create a program that manages the state of the treasure chest along the way. On the first line, you will receive the initial loot of the treasure chest, which is a string of items separated by a "|".
# "{loot1}|{loot2}|{loot3} … {lootn}"
# The following lines represent commands until "Yohoho!" which ends the treasure hunt:
# •	"Loot {item1} {item2}…{itemn}":
# o	Pick up treasure loot along the way. Insert the items at the beginning of the chest.
# o	If an item is already contained, don't insert it.
# •	"Drop {index}":
# o	Remove the loot at the given position and add it at the end of the treasure chest.
# o	If the index is invalid, skip the command.
# •	"Steal {count}":
# o	Someone steals the last count loot items. If there are fewer items than the given count, remove as much as there are.
# o	Print the stolen items separated by ", ":
# "{item1}, {item2}, {item3} … {itemn}"
# In the end, output the average treasure gain, which is the sum of all treasure items length divided by the count of all items inside the chest formatted to the second decimal point:
# "Average treasure gain: {averageGain} pirate credits."
# If the chest is empty, print the following message:
# "Failed treasure hunt."


def drop_func(index_for_manipulation, treasure_loot):
    if 0 <= index_for_manipulation < len(treasure_loot):
        deleted_item = treasure_loot.pop(index_for_manipulation)
        treasure_loot.append(deleted_item)
    return treasure_loot


def steal_func(item, treasure_loot):
    stolen = []
    if item < len(treasure_loot):
        for item in range(item):
            stolen_stuff = treasure_loot.pop()
            stolen.append(stolen_stuff)
    else:
        for item in range(len(treasure_loot)):
            stolen_stuff = treasure_loot.pop()
            stolen.append(stolen_stuff)
    stolen.reverse()
    print(", ".join(stolen))
    return treasure_loot


def loot_func(items_for_add, loots):
    for item in range(len(items_for_add)):
        if items_for_add[item] not in loots:
            added_item = items_for_add[item]
            loots.insert(0, added_item)
    return loots


loot = input().split("|")
while True:
    data = input().split()
    command = data[0]
    if command == "Yohoho!":
        break
    if command == "Loot":
        data.pop(0)
        loot = loot_func(data, loot)
    elif command == "Drop":
        index = int(data[1])
        loot = drop_func(index, loot)
    elif command == "Steal":
        items = int(data[1])
        loot = steal_func(items, loot)

loot_ch_lengtt = []
for word in loot:
    word_len = 0
    for ch in word:
        word_len += 1
    loot_ch_lengtt.append(word_len)
if len(loot) > 0:
    print(f'Average treasure gain: {sum(loot_ch_lengtt) / len(loot):.2f} pirate credits.')
else:
    print('Failed treasure hunt.')
