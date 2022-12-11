class PizzaDelivery:

    def __init__(self, name: str, price: float, ingredients: dict):
        self.ordered = False
        self.name = name
        self.price = price
        self.ingredients = ingredients

    def add_extra(self, ingredients: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredients in self.ingredients:
                self.ingredients[ingredients] += quantity
                self.price += price_per_quantity * quantity
            else:
                self.ingredients[ingredients] = quantity
                self.price += price_per_quantity * quantity
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredients: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredients not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredients} in {self.name}!"
            else:
                if quantity > self.ingredients[ingredients]:
                    return f"Please check again the desired quantity of {ingredients}!"
                self.ingredients[ingredients] -= quantity
                self.price -= quantity * price_per_quantity
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            ingredients_print = []
            for key, value in self.ingredients.items():
                ingredients_print.append(f'{key}: {value}')
            return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients_print)} and the price will be {self.price}lv."
        else:
            return f"Pizza {self.name} already prepared, and we can't make any changes!"


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))
