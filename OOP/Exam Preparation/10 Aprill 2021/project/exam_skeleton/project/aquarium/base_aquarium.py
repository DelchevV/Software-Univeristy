from abc import ABC, abstractmethod


class BaseAquarium(ABC):
    VALID_FISH_TYPE = []

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.decorations = []
        self.fish = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Aquarium name cannot be an empty string.")
        self.__name = value

    def calculate_comfort(self):
        comfort = 0
        for dec in self.decorations:
            comfort += dec.comfort

        return comfort

    def add_fish(self, fish: object):
        if len(self.fish) == self.capacity:
            return "Not enough capacity."
        if type(fish).__name__ in self.VALID_FISH_TYPE:
            self.fish.append(fish)
            return f"Successfully added {type(fish).__name__} to {self.name}."

    def remove_fish(self, fish):
        if fish in self.fish:
            self.fish.remove(fish)

    def add_decoration(self, decoration):
        self.decorations.append(decoration)

    def feed(self):
        for fish in self.fish:
            fish.eat()

    def __str__(self):
        result = [
            f"{self.name}:"
        ]

        if self.fish:
            fishes = [fish.name for fish in self.fish]
            result.append(f"Fish: {' '.join(fishes)}")
        else:
            result.append("Fish: none")

        result.append(f"Decorations: {len(self.decorations)}")
        result.append(f"Comfort: {self.calculate_comfort()}")

        return "\n".join(result)
