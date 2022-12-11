from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    def __init__(self):
        self.cars = []
        self.drivers = []
        self.races = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        if car_type in ["MuscleCar", "SportsCar"]:
            for car in self.cars:
                if car.model == model:
                    raise Exception(f"Car {model} is already created!")

            if car_type == "MuscleCar":
                car = MuscleCar(model, speed_limit)
            else:
                car = SportsCar(model, speed_limit)

            self.cars.append(car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        for driver in self.drivers:
            if driver.name == driver_name:
                raise Exception(f"Driver {driver_name} is already created!")

        driver = Driver(driver_name)
        self.drivers.append(driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        for race in self.races:
            if race.name == race_name:
                raise Exception(f"Race {race_name} is already created!")

        race = Race(race_name)
        self.races.append(race)
        return f"Race {race_name} is created."

    def __find_driver(self, name):
        for driver in self.drivers:
            if driver.name == name:
                return driver

    def __find_car(self, car_type):
        for car in reversed(self.cars):
            if type(car).__name__ == car_type and not car.is_taken:
                return car

    def __find_race(self, name):
        for race in self.races:
            if race.name == name:
                return race

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.__find_driver(driver_name)
        car = self.__find_car(car_type)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if not car:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car is not None:
            driver.car.is_taken = False
            old_model = driver.car.model
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} changed his car from {old_model} to {car.model}."
        else:
            driver.car = car
            car.is_taken = True

            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.__find_race(race_name)
        driver = self.__find_driver(driver_name)

        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")
        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")
        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.__find_race(race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")
        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        drivers = [d for d in race.drivers]
        participants = sorted(drivers, key=lambda x: -x.car.speed_limit)
        result = []
        for winner in reversed(participants[:3]):
            winner.number_of_wins+=1
            result.append(f"Driver {winner.name} wins the {race_name} race with a speed of {winner.car.speed_limit}.")

        return "\n".join(reversed(result))


controller = Controller()
print(controller.create_driver("Peter"))
print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("SportsCar", "Porsche 911", 580))
print(controller.add_car_to_driver("Peter", "SportsCar"))
print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
print(controller.create_driver("John"))
print(controller.create_driver("Jack"))
print(controller.create_driver("Kelly"))
print(controller.add_car_to_driver("Kelly", "MuscleCar"))
print(controller.add_car_to_driver("Jack", "MuscleCar"))
print(controller.add_car_to_driver("John", "SportsCar"))
print(controller.create_race("Christmas Top Racers"))
print(controller.add_driver_to_race("Christmas Top Racers", "John"))
print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
print(controller.start_race("Christmas Top Racers"))
[print(d.name, d.number_of_wins) for d in controller.drivers]
