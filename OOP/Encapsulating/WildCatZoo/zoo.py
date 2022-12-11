from WildCatZoo.animal import Animal
from WildCatZoo.caretaker import Caretaker
from WildCatZoo.cheetah import Cheetah
from WildCatZoo.keeper import Keeper
from WildCatZoo.lion import Lion
from WildCatZoo.tiger import Tiger
from WildCatZoo.vet import Vet


class Zoo:
    def __init__(self, name, budget, animal_capacity, workers_capacity):
        self.name = name
        self.__budget = budget
        self.__animal_capacity = animal_capacity
        self.__workers_capacity = workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal, price):
        price = int(price)
        if self.__animal_capacity > len(self.animals) and price > self.__budget:
            return "Not enough budget"

        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        return "Not enough space for animal"

    def hire_worker(self, worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                self.__workers_capacity += 1
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        total_salaries_cost = 0
        for worker in self.workers:
            total_salaries_cost += worker.salary
        if self.__budget >= total_salaries_cost:
            self.__budget -= total_salaries_cost
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        total_animal_care_cost = 0
        for animal in self.animals:
            total_animal_care_cost += animal.money_for_care
        if self.__budget >= total_animal_care_cost:
            self.__budget -= total_animal_care_cost
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        output = [f"You have {len(self.animals)} animals"]
        lions = 0
        tigers = 0
        cheetahs = 0
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                lions += 1
            elif animal.__class__.__name__ == "Tiger":
                tigers += 1
            elif animal.__class__.__name__ == "Cheetah":
                cheetahs += 1

        output.append(f"----- {lions} Lions:")
        for animal in self.animals:
            if animal.__class__.__name__ == "Lion":
                output.append(animal.__repr__())

        output.append(f"----- {tigers} Tigers:")
        for animal in self.animals:
            if animal.__class__.__name__ == "Tiger":
                output.append(animal.__repr__())

        output.append(f"----- {cheetahs} Cheetahs:")
        for animal in self.animals:
            if animal.__class__.__name__ == "Cheetah":
                output.append(animal.__repr__())

        return "\n".join(output)

    def workers_status(self):
        vets = 0
        keepers = 0
        caretakers = 0
        output = [f"You have {len(self.workers)} workers"]

        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                vets += 1
            elif worker.__class__.__name__ == "Caretaker":
                caretakers += 1
            elif worker.__class__.__name__ == "Keeper":
                keepers += 1

        output.append(f"----- {keepers} Keepers:")
        for worker in self.workers:
            if worker.__class__.__name__ == "Keeper":
                output.append(worker.__repr__())

        output.append(f'----- {caretakers} Caretakers:')
        for worker in self.workers:
            if worker.__class__.__name__ == "Caretaker":
                output.append(worker.__repr__())

        output.append(f"----- {vets} Vets:")
        for worker in self.workers:
            if worker.__class__.__name__ == "Vet":
                output.append(worker.__repr__())

        return "\n".join(output)

# zoo = Zoo("Zootopia", 3000, 5, 8)
#
# # Animals creation
# animals = [Cheetah("Cheeto", "Male", 2), Cheetah("Cheetia", "Female", 1), Lion("Simba", "Male", 4), Tiger("Zuba", "Male", 3), Tiger("Tigeria", "Female", 1), Lion("Nala", "Female", 4)]
#
# # Animal prices
# prices = [200, 190, 204, 156, 211, 140]
#
# # Workers creation
# workers = [Keeper("John", 26, 100), Keeper("Adam", 29, 80), Keeper("Anna", 31, 95), Caretaker("Bill", 21, 68), Caretaker("Marie", 32, 105), Caretaker("Stacy", 35, 140), Vet("Peter", 40, 300), Vet("Kasey", 37, 280), Vet("Sam", 29, 220)]
#
# # Adding all animals
# for i in range(len(animals)):
#     animal = animals[i]
#     price = prices[i]
#     print(zoo.add_animal(animal, price))
#
# # Adding all workers
# for worker in workers:
#     print(zoo.hire_worker(worker))
#
# # Tending animals
# print(zoo.tend_animals())
#
# # Paying keepers
# print(zoo.pay_workers())
#
# # Fireing worker
# print(zoo.fire_worker("Adam"))
#
# # Printing statuses
# print(zoo.animals_status())
# print(zoo.workers_status())




