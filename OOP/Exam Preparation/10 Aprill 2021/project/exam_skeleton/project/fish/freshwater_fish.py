from project.fish.base_fish import BaseFish


class FreshwaterFish(BaseFish):
    INCREASE_FISH_SIZE = 3
    INITIAL_SIZE = 3

    def __init__(self, name, species, price):
        super().__init__(name, species, self.INITIAL_SIZE, price)

    def eat(self):
        self.size += self.INCREASE_FISH_SIZE
