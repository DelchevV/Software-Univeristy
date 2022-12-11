from project.aquarium.base_aquarium import BaseAquarium


class SaltwaterAquarium(BaseAquarium):
    VALID_FISH_TYPE = ["SaltwaterFish"]
    CAPACITY = 25

    def __init__(self, name):
        super(SaltwaterAquarium, self).__init__(name, self.CAPACITY)
