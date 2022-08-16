# You are playing a game, and your goal is to win a legendary item - any legendary item will be good enough. However, it's a tedious process, and it requires quite a bit of farming. The possible items are:
# •	"Shadowmourne" - requires 250 Shards
# •	"Valanyr" - requires 250 Fragments
# •	"Dragonwrath" - requires 250 Motes
# "Shards", "Fragments", and "Motes" are the key materials 	(case-insensitive), and everything else is junk.
# You will be given lines of input in the format:
# "{quantity1} {material1} {quantity2} {material2} … {quantityN} {materialN}"
# Keep track of the key materials - the first one that reaches 250, wins the race. At that point, you have to print that the corresponding legendary item is obtained.
# In the end, print the remaining shards, fragments, motes in the format:
# "shards: {number_of_shards}
# fragments: {number_of_fragments}
# motes: {number_of_motes}"
# Finally, print the collected junk items in the order of appearance.


valuable_items = {"shards": 0, "fragments": 0, "motes": 0}
junk_items = {}


def print_func(valuable, junk):
    for key, value in valuable.items():
        print(f"{key}: {value}")

    for key, value in junk.items():
        print(f"{key}: {value}")


def is_leg_item_obtained(valuable, junk):
    for key, value in valuable.items():

        if key == "shards" and value >= 250:
            print("Shadowmourne obtained!")
            valuable[key] -= 250
            print_func(valuable, junk)
            exit()

        elif key == "fragments" and value >= 250:
            print("Valanyr obtained!")
            valuable[key] -= 250
            print_func(valuable, junk)
            exit()

        elif key == "motes" and value >= 250:
            print("Dragonwrath obtained!")
            valuable[key] -= 250
            print_func(valuable, junk)
            exit()


while True:

    data = input().split()
    for i in range(0, len(data), 2):
        item = data[i + 1].lower()
        quantity = int(data[i])
        if item == "shards" or item == "fragments" or item == "motes":
            if item in valuable_items:
                valuable_items[item] += quantity
                is_leg_item_obtained(valuable_items, junk_items)
            else:
                valuable_items[item] = quantity
                is_leg_item_obtained(valuable_items, junk_items)
        else:
            if item in junk_items:
                junk_items[item] += quantity
            else:
                junk_items[item] = quantity
