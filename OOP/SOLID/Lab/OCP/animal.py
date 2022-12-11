from abc import ABC, abstractmethod


class Animal(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass


class Cat(Animal):
    def make_sound(self):
        return "meow!"


class Dog(Animal):
    def make_sound(self):
        return "woof-woof!"


class Chicken(Animal):
    def make_sound(self):
        return "Cluck"


animals = [Cat(), Dog()]
for animal in animals:
    print(animal.make_sound())

## добавете ново животно и рефакторирайте кода да работи без да се налага да се правят промени по него
## при добавяне на нови животни
# animals = [Animal('cat'), Animal('dog'), Animal('chicken')]
