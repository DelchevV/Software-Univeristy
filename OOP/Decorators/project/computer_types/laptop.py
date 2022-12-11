from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        'AMD Ryzen 9 5950X': 900,
        'Intel Core i9-11900H': 1050,
        'Apple M1 Pro': 1200
    }
    RAMS = {
        2: 100,
        4: 200,
        8: 300,
        16: 400,
        32: 500,
        64: 600,
    }

    def configure_computer(self, processor, ram):
        if processor not in Laptop.PROCESSORS:
            raise ValueError(f"{processor} is not "
                             f"compatible with laptop {self.manufacturer} "
                             f"{self.model}!")

        if ram not in Laptop.RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += Laptop.PROCESSORS[processor]
        self.price += Laptop.RAMS[ram]

        return f"Created {self.manufacturer} {self.model} " \
               f"with {processor} and " \
               f"{ram}GB RAM for {self.price}$."
