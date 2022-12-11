class Player:
    def __init__(self, name: str, sprint: int, dribble: int, passing: int, shooting: int):
        self.__name = name
        self.__sprint = sprint
        self.__dribble = dribble
        self.__passing = passing
        self.__shooting = shooting

    def __str__(self):
        output = [
            f"Player: {self.name}",
            f"Sprint: {self.__sprint}",
            f"Dribble: {self.__dribble}",
            f"Passing: {self.__passing}",
            f"Shooting: {self.__shooting}"
        ]
        return "\n".join(output)

    @property
    def name(self):
        return self.__name
