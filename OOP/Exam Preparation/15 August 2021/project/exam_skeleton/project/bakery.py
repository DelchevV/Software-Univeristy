from project.baked_food.bread import Bread
from project.baked_food.cake import Cake
from project.drink.tea import Tea
from project.drink.water import Water
from project.table.inside_table import InsideTable
from project.table.outside_table import OutsideTable


class Bakery:
    def __init__(self, name):
        self.name = name
        self.food_menu = []
        self.drinks_menu = []
        self.tables_repository = []
        self.total_income = 0

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value.strip() == "":
            raise ValueError("Name cannot be empty string or white space!")
        self.__name = value

    def add_food(self, food_type: str, name: str, price: float):
        if food_type not in ["Bread", "Cake"]:
            for food in self.food_menu:
                if food.name == name:
                    raise Exception(f"{food_type} {name} is already in the menu!")

            if food_type == "Bread":
                food = Bread(name, price)
            else:
                food = Cake(name, price)

            self.food_menu.append(food)
            return f"Added {food.name} ({type(food).__name__}) to the food menu"

    def add_drink(self, drink_type: str, name: str, portion: float, brand: str):
        if drink_type in ["Tea", "Water"]:
            for d in self.drinks_menu:
                if d.name == name:
                    raise Exception(f"{drink_type} {name} is already in the menu!")

            if drink_type == "Tea":
                drink = Tea(name, portion, brand)
            else:
                drink = Water(name, portion, brand)

            self.drinks_menu.append(drink)
            return f"Added {drink.name} ({drink.brand}) to the drink menu"

    def add_table(self, table_type: str, table_number: int, capacity: int):
        if table_type in ["InsideTable", "OutsideTable"]:
            for table in self.tables_repository:
                if table.table_number == table_number:
                    raise Exception(f"Table {table_number} is already in the bakery!")

            if table_type == "InsideTable":
                table = InsideTable(table_number, capacity)
            else:
                table = OutsideTable(table_number, capacity)

            self.tables_repository.append(table)

            return f"Added table number {table_number} in the bakery"

    def reserve_table(self, number_of_people: int):
        for table in self.tables_repository:
            if not table.is_reserved:
                if table.capacity >= number_of_people:
                    table.is_reserved = True
                    table.number_of_people += number_of_people
                    return f"Table {table.table_number} has been reserved for {number_of_people} people"

        return f"No available table for {number_of_people} people"

    def order_food(self, table_number: int, *args):
        table = self.__find_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        food_in_menu = []
        food_not_in_menu = []

        for food in args:
            for f in self.food_menu:
                if food == f.name:
                    table.food_orders.append(f)
                    food_in_menu.append(f)
                else:
                    food_not_in_menu.append(food)

        result = [
            f"Table {table_number} ordered:"
        ]

        for f_name in food_in_menu:
            result.append(f" - {f_name.name}: {f_name.portion}g - {f_name.price}lv")

        result.append(f"{self.name} does not have in the menu:")

        for f_name in food_not_in_menu:
            result.append(f"{f_name}")

        return "\n".join(result)

    def order_drink(self, table_number: int, *args):
        table = self.__find_table(table_number)

        if not table:
            return f"Could not find table {table_number}"

        drink_in_menu = []
        drink_not_in_menu = []

        for d in args:
            for drink in self.drinks_menu:
                if d == drink.name:
                    drink_in_menu.append(drink)
                    table.drink_orders.apend(drink)
                else:
                    drink_not_in_menu.append(d)

        result = [
            f"Table {table_number} ordered:"
        ]

        for f_name in drink_in_menu:
            result.append(f"- {f_name.name} {f_name.brand} - {f_name.portion}ml - {f_name.price}lv")

        result.append(f"{self.name} does not have in the menu:")

        for f_name in drink_not_in_menu:
            result.append(f"{f_name}")

        return "\n".join(result)

    def leave_table(self, table_number: int):
        table = self.__find_table(table_number)
        bill = table.get_bill()
        self.total_income += bill

        result = [
            f"Table: {table_number}",
            f"Bill: {bill:.2f}"
        ]

        table.clear()
        return "\n".join(result)

    def get_free_tables_info(self):
        result = []
        for table in self.tables_repository:
            result.append(table.free_table_info())

        return "\n".join(result)

    def get_total_income(self):
        return f"Total income: {self.total_income:.2f}lv"

    def __find_table(self, table_number):
        for table in self.tables_repository:
            if table.table_number == table_number:
                return table

