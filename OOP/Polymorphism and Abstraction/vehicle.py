from abc import ABC, abstractmethod


class Vehicle(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def drive(self, km):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    INCREASE = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + self.INCREASE)
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption


class Truck(Vehicle):
    INCREASE = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        super().__init__()
        self.fuel_consumption = fuel_consumption
        self.fuel_quantity = fuel_quantity

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95

    def drive(self, distance):
        consumption = distance * (self.fuel_consumption + self.INCREASE)
        if self.fuel_quantity - consumption >= 0:
            self.fuel_quantity -= consumption


truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)
