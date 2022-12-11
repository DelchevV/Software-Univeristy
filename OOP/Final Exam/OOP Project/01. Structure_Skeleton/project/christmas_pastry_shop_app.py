from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    def __init__(self):
        self.booths = []
        self.delicacies = []
        self.income = 0.0

    def __first_booth(self, number_of_people):
        for booth in self.booths:
            if booth.capacity >= number_of_people and not booth.is_reserved:
                return booth

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        for delicacy in self.delicacies:
            if delicacy.name == name:
                raise Exception(f"{name} already exists!")

            if type_delicacy not in ["Gingerbread", "Stolen"]:
                raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = object
        if type_delicacy == "Gingerbread":
            new_delicacy = Gingerbread(name, price)
        elif type_delicacy == "Stolen":
            new_delicacy = Stolen(name, price)

        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in ["Open Booth", "Private Booth"]:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = object
        if type_booth == "Open Booth":
            new_booth = OpenBooth(booth_number, capacity)
        elif type_booth == "Private Booth":
            new_booth = PrivateBooth(booth_number, capacity)

        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        booth = self.__first_booth(number_of_people)

        if not booth:
            raise Exception(f"No available booth for {number_of_people} people!")

        booth.reserve(number_of_people)
        return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."

    def __find_booth_by_num(self, booth_number):
        for booth in self.booths:
            if booth.booth_number == booth_number:
                return booth
        else:
            raise Exception(f"Could not find booth {booth_number}!")

    def __find_delicacy(self, del_name):
        for delicacy in self.delicacies:
            if delicacy.name == del_name:
                return delicacy
        else:
            raise Exception(f"No {del_name} in the pastry shop!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self.__find_booth_by_num(booth_number)
        delicacy = self.__find_delicacy(delicacy_name)
        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        current_bill = 0
        booth = self.__find_booth_by_num(booth_number)
        current_bill += booth.price_for_reservation
        for delicacy in booth.delicacy_orders:
            current_bill += delicacy.price

        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0

        result = [
            f"Booth {booth_number}:",
            f"Bill: {current_bill:.2f}lv."
        ]
        self.income += current_bill
        return "\n".join(result)

    def get_income(self):
        return f"Income: {self.income:.2f}lv."


shop = ChristmasPastryShopApp()
print(shop.add_delicacy("Gingerbread", "Gingy", 5.20))
print(shop.delicacies[0].details())
print(shop.add_booth("Open Booth", 1, 30))
print(shop.add_booth("Private Booth", 10, 5))
print(shop.reserve_booth(30))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.reserve_booth(5))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.order_delicacy(1, "Gingy"))
print(shop.leave_booth(1))
print(shop.get_income())
