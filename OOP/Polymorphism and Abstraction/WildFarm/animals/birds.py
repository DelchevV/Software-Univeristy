from abc import ABC

from WildFarm.animals.animal import Animal
from WildFarm.food import Meat, Vegetable


class Bird(Animal, ABC):
    def __init__(self, name, weight, wing_size, food_eaten=0):
        super(Bird, self).__init__(name, weight, food_eaten)
        self.wing_size = wing_size

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]'


class Owl(Bird):
    food_type = 'Meat'
    weight_increase = 0.25

    def make_sound(self):
        return f"Hoot Hoot"

    def feed(self, food):
        if food.__class__.__name__ != self.food_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Hen(Bird):
    weight_increase = 0.35

    def make_sound(self):
        return "Cluck"

    def feed(self, food):
        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity
