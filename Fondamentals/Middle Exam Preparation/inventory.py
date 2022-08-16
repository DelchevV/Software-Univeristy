# You will receive a journal with some collecting items, separated with a comma and a space (", "). After that, until receiving "Craft!" you will be receiving different commands split by " - ":
# •	"Collect - {item}" - you should add the given item to your inventory. If the item already exists, you should skip this line.
# •	"Drop - {item}" - you should remove the item from your inventory if it exists.
# •	"Combine Items - {old_item}:{new_item}" - you should check if the old item exists. If so, add the new item after the old one. Otherwise, ignore the command.
# •	"Renew – {item}" – if the given item exists, you should change its position and put it last in your inventory.
def collect_func(material, inventory):
    if material not in inventory:
        inventory.append(material)
    return inventory


def drop_func(material, inventory):
    if material in inventory:
        inventory.remove(material)
    return inventory


def combine_func(old, new , inventory):
    if old in inventory:
        where_is_old_item=inventory.index(old)
        inventory.insert(where_is_old_item+1, new)
    return inventory


def renew_func(material, inventory):
    if material in inventory:
        inventory.remove(material)
        inventory.append(material)
    return inventory


inventory_items=input().split(", ")

while True:
    data=input().split(" - ")
    command=data[0]
    if command=="Craft!":
        break
    item = data[1]
    if command=="Collect":
        inventory_items=collect_func(item,inventory_items)
    elif command=="Drop":
        inventory_items=drop_func(item,inventory_items)
    elif command=="Combine Items":
        split_by_new_old=item.split(":")
        old_item=split_by_new_old[0]
        new_item=split_by_new_old[1]
        inventory_items=combine_func(old_item,new_item,inventory_items)
    elif command=="Renew":
        inventory_items=renew_func(item, inventory_items)
print(", ".join(inventory_items))