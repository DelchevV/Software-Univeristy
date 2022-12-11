from project.aquarium.freshwater_aquarium import FreshwaterAquarium
from project.aquarium.saltwater_aquarium import SaltwaterAquarium
from project.decoration.decoration_repository import DecorationRepository
from project.decoration.ornament import Ornament
from project.decoration.plant import Plant
from project.fish.freshwater_fish import FreshwaterFish
from project.fish.saltwater_fish import SaltwaterFish


class Controller:
    def __init__(self):
        self.decorations_repository = DecorationRepository()
        self.aquariums = []

    def __find_aquarium(self, name):
        for aquarium in self.aquariums:
            if aquarium.name == name:
                return aquarium

    def __find_decoration(self, decoration_type):
        for decoration in self.decorations_repository.decorations:
            if type(decoration).__name__ == decoration_type:
                return decoration

    def add_aquarium(self, aquarium_type: str, aquarium_name: str):
        current_aquarium = object
        valid_aquariums = ["FreshwaterAquarium", "SaltwaterAquarium"]
        if aquarium_type not in valid_aquariums:
            return "Invalid aquarium type."

        if aquarium_type == valid_aquariums[0]:
            current_aquarium = FreshwaterAquarium(aquarium_name)
        else:
            current_aquarium = SaltwaterAquarium(aquarium_name)

        self.aquariums.append(current_aquarium)
        return f"Successfully added {aquarium_type}."

    def add_decoration(self, decoration_type: str):
        decoration = object
        valid_decorations = ["Ornament", "Plant"]
        if decoration_type not in valid_decorations:
            return "Invalid decoration type."
        if decoration_type == valid_decorations[0]:
            decoration = Ornament()
        else:
            decoration = Plant()

        self.decorations_repository.add(decoration)
        return f"Successfully added {decoration_type}."

    def insert_decoration(self, aquarium_name: str, decoration_type: str):

        decoration = self.__find_decoration(decoration_type)
        if not decoration:
            return f"There isn't a decoration of type {decoration_type}."

        aquarium = self.__find_aquarium(aquarium_name)

        if aquarium:
            aquarium.add_decoration(decoration)
            self.decorations_repository.remove(decoration)
            return f"Successfully added {decoration_type} to {aquarium_name}."

    def add_fish(self, aquarium_name: str, fish_type: str, fish_name: str, fish_species: str, price: float):
        if fish_type not in ["FreshwaterFish", "SaltwaterFish"]:
            return f"There isn't a fish of type {fish_type}."
        aquarium = self.__find_aquarium(aquarium_name)

        if not aquarium:
            return

        if fish_type[:-4] not in aquarium.__class__.__name__:
            return "Water not suitable."

        if fish_type == "FreshwaterFish":
            fish = FreshwaterFish(fish_name, fish_species, price)
        else:
            fish = SaltwaterFish(fish_name, fish_species, price)

        return aquarium.add_fish(fish)

    def feed_fish(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        for fish in aquarium.fish:
            fish.eat()

        return f"Fish fed: {len(aquarium.fish)}"

    def calculate_value(self, aquarium_name: str):
        aquarium = self.__find_aquarium(aquarium_name)
        if aquarium:
            total_value = 0
            for fish in aquarium.fish:
                total_value += fish.price
            for decoration in aquarium.decorations:
                total_value += decoration.price

            return f"The value of Aquarium {aquarium_name} is {total_value:.2f}."

    def report(self):
        return "\n".join(str(a) for a in self.aquariums)

