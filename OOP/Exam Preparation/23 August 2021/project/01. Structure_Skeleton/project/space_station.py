from project.astronaut.astronaut import Astronaut
from project.astronaut.astronaut_repository import AstronautRepository
from project.astronaut.biologist import Biologist
from project.astronaut.geodesist import Geodesist
from project.astronaut.meteorologist import Meteorologist
from project.planet.planet import Planet
from project.planet.planet_repository import PlanetRepository


class SpaceStation:
    COMPLETED_MISSIONS = 0
    FAILED_MISSIONS = 0

    def __init__(self):
        self.planet_repository = PlanetRepository()
        self.astronaut_repository = AstronautRepository()

    def __find_planed(self, planet_name):
        for p in self.planet_repository.planets:
            if p.name == planet_name:
                return p
        raise Exception("Invalid planet name!")

    def add_astronaut(self, astronaut_type: str, name: str):
        if astronaut_type not in ["Biologist", "Geodesist", "Meteorologist"]:
            raise Exception("Astronaut type is not valid!")

        astronaut = object
        if astronaut_type == "Biologist":
            astronaut = Biologist(name)
        elif astronaut_type == "Geodesist":
            astronaut = Geodesist(name)
        else:
            astronaut = Meteorologist(name)

        for a in self.astronaut_repository.astronauts:
            if a.name == astronaut.name:
                return f"{astronaut.name} is already added."

        self.astronaut_repository.add(astronaut)
        return f"Successfully added {type(astronaut).__name__}: {name}."

    def add_planet(self, name: str, items: str):
        for p in self.planet_repository.planets:
            if p.name == name:
                return f"{name} is already added."

        planet = Planet(name)
        planet.items.extend([x for x in items.split(", ")])
        self.planet_repository.add(planet)

        return f"Successfully added Planet: {planet.name}."

    def retire_astronaut(self, name: str):
        for a in self.astronaut_repository.astronauts:
            if a.name == name:
                self.astronaut_repository.astronauts.remove(a)
                return f"Astronaut {name} was retired!"

        raise Exception(f"Astronaut {name} doesn't exist!")

    def recharge_oxygen(self):
        for astronaut in self.astronaut_repository.astronauts:
            astronaut.oxygen += 10

    def send_on_mission(self, planet_name: str):
        planet = self.__find_planed(planet_name)

        suitable_astronauts = []
        for astronaut in self.astronaut_repository.astronauts:
            if astronaut.oxygen > 30:
                suitable_astronauts.append(astronaut)
        if len(suitable_astronauts) < 1:
            raise Exception("You need at least one astronaut to explore the planet!")
        suitable_astronauts = sorted(suitable_astronauts, key=lambda x: -x.oxygen)

        astronauts_in_space = []
        for astronaut in suitable_astronauts:

            if planet.items:
                astronauts_in_space.append(astronaut.name)

            while True:
                if astronaut.oxygen <= 0:
                    break

                if planet.items:
                    astronaut.backpack.append(planet.items.pop())
                    astronaut.breathe()
                else:
                    self.COMPLETED_MISSIONS += 1
                    return f"Planet: {planet_name} was explored. {len(astronauts_in_space)} astronauts participated in collecting items."

        if planet.items:
            self.FAILED_MISSIONS += 1
            return f"Mission is not completed."

    def report(self):
        result = [
            f"{self.COMPLETED_MISSIONS} successful missions!",
            f"{self.FAILED_MISSIONS} missions were not completed!",
            "Astronauts' info:",
        ]
        for a in self.astronaut_repository.astronauts:
            a_result = [
                f"Name: {a.name}",
                f"Oxygen: {a.oxygen}",
                f"Backpack items: {', '.join(a.backpack) if a.backpack else 'none'}"
            ]
            result.extend(a_result)

        return "\n".join(result)

# station = SpaceStation()
# print(station.add_planet("Earth", "iron, gold, coal"))
# print(station.add_astronaut("Geodesist", "Gosho"))
# print(station.add_astronaut("Biologist", "Ivan"))
# print(station.add_astronaut("Meteorologist", "Peter"))
# print(station.send_on_mission("Earth"))
# print(station.report())
