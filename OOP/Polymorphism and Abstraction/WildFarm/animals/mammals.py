from abc import ABC

from WildFarm.animals.animal import Animal
from WildFarm.animals.birds import Hen
from WildFarm.food import Meat, Vegetable


class Mammal(Animal, ABC):
    def __init__(self, name, weight, living_region, food_eaten=0):
        super(Mammal, self).__init__(name, weight, food_eaten)
        self.living_region = living_region

    def __repr__(self):
        return f'{self.__class__.__name__} [{self.name}, {self.weight}, {self.living_region}, {self.food_eaten}]'


class Mouse(Mammal):
    weight_increase = 0.10
    food_type = ["Vegetable", 'Fruit']

    def make_sound(self):
        return 'Squeak'

    def feed(self, food):
        if food.__class__.__name__ not in self.food_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity




class Dog(Mammal):
    weight_increase = 0.40
    food_type = ['Meat']

    def make_sound(self):
        return "Woof!"

    def feed(self, food):
        if food.__class__.__name__ not in self.food_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Cat(Mammal):
    weight_increase = 0.30
    food_type = ['Vegetable', 'Meat']

    def make_sound(self):
        return 'Meow'

    def feed(self, food):
        if food.__class__.__name__ not in self.food_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


class Tiger(Mammal):
    weight_increase = 1.00
    food_type = ['Meat']

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food):
        if food.__class__.__name__ not in self.food_type:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"

        self.weight += food.quantity * self.weight_increase
        self.food_eaten += food.quantity


