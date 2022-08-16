class Zoo:
    __animals = 0

    def __init__(self, zoo_name):
        self.name = zoo_name
        self.mammals = []
        self.fishes = []
        self.birds = []

    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1

    def get_info(self, species):
        result = ""
        if species == "mammal":
            result += f"Mammals in {self.name}: {', '.join(self.mammals)}"
        elif species == "fish":
            result += f"Fishes in {self.name}: {', '.join(self.fishes)}"
        elif species == "bird":
            result += f"Birds in {self.name}: {', '.join(self.birds)}"
        return print(result)


zoo_name = input()
zoo = Zoo(zoo_name)
lines = int(input())
for line in range(lines):
    data = input().split(" ")
    species = data[0]
    name = data[1]
    zoo.add_animal(species, name)
searched_animal_species = input()
zoo.get_info(searched_animal_species)
print(f"Total animals: {lines}")
