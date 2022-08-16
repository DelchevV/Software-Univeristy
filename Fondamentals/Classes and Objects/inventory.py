class Inventory:
    def __init__(self, _capacity: int):
        self.capacity = _capacity
        self.items = []

    def add_item(self, item: str):
        if len(self.items) < self.capacity:
            self.items.append(item)
            return self.items
        else:
            return "not enough room in the inventory"

    def get_capacity(self):
        return self.capacity

    def __repr__(self):
        result=f"Items: {', '.join(self.items)}." \
               f"\nCapacity left: {Inventory.get_capacity(self)-len(self.items)}"
        return result


inventory = Inventory(2)
inventory.add_item("potion")
inventory.add_item("sword")
print(inventory.add_item("bottle"))
print(inventory.get_capacity())
print(inventory)


