from project.player import Player
from project.supply.drink import Drink
from project.supply.food import Food
from project.supply.supply import Supply


class Controller:
    def __init__(self):
        self.players = []
        self.supplies = []

    def __find_player(self, name):
        for player in self.players:
            if player.name == name:
                return player

    def __find_last_supply(self, supply_type):
        for i in range(len(self.supplies) - 1, 0, -1):
            if type(self.supplies[i]).__name__ == supply_type:
                return self.supplies.pop(i)
        if supply_type == "Food":
            raise Exception("There are no food supplies left!")
        if supply_type == "Drink":
            raise Exception("There are no drink supplies left!")

    def add_player(self, *args: Player):
        new_players = []
        for player in args:
            if player not in self.players:
                new_players.append(player)
        self.players.extend(new_players)
        return f"Successfully added: {', '.join([p.name for p in new_players])}"

    def add_supply(self, *args: Supply):
        for supply in args:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustain_type: str):
        player = self.__find_player(player_name)
        if player.stamina == 100:
            return f"{player.name} have enough stamina."
        supply = self.__find_last_supply(sustain_type)
        if supply:
            player._sustain_player(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    @staticmethod
    def __attack(p1, p2):
        p2.stamina -= (p1.stamina / 2)
        if p1.stamina - (p2.stamina / 2) < 0:
            p1.stamina = 0
        else:
            p1.stamina -= (p2.stamina / 2)
        if p1.stamina < p2.stamina:
            return f"Winner: {p2.name}"
        else:
            return f"Winner: {p1.name}"

    def duel(self, first_player_name: str, second_player_name: str):
        first_player = self.__find_player(first_player_name)
        second_player = self.__find_player(second_player_name)
        if first_player.stamina == 0 or second_player.stamina == 0:
            result = []
            if first_player.stamina == 0:
                result.append(f"Player {first_player.name} does not have enough stamina.")
            if second_player.stamina == 0:
                result.append(f"Player {second_player.name} does not have enough stamina.")

            return "\n".join(result)

        if first_player.stamina < second_player.stamina:
            return self.__attack(first_player, second_player)
        else:
            return self.__attack(second_player, first_player)

    def next_day(self):
        for player in self.players:
            player.stamina -= player.age * 2

            if player.stamina < 0:
                player.stamina = 0

        for player in self.players:
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(str(player))
        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)


controller = Controller()
apple = Food("apple", 22)
cheese = Food("cheese")
juice = Drink("orange juice")
water = Drink("water")
first_player = Player('Peter', 15)
second_player = Player('Lilly', 12, 94)
print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
print(controller.add_player(first_player, second_player))
print(controller.duel("Peter", "Lilly"))
print(controller.add_player(first_player))
print(controller.sustain("Lilly", "Drink"))
first_player.stamina = 0
print(controller.duel("Peter", "Lilly"))
print(first_player)
print(second_player)
controller.next_day()
print(controller)
