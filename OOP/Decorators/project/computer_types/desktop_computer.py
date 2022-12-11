from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {
        'AMD Ryzen 7 5700G': 500,
        'Intel Core i5-12600K': 600,
        'Apple M1 Max': 1800
    }
    RAMS = {
        2: 100,
        4: 200,
        8: 300,
        16: 400,
        32: 500,
        64: 600,
        128: 800
    }

    def __init__(self, manufacturer, model):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor, ram):
        if processor not in DesktopComputer.PROCESSORS:
            raise ValueError(f"{processor} is not "
                             f"compatible with desktop computer {self.manufacturer} "
                             f"{self.model}!")
        if ram not in DesktopComputer.RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with "
                             f"desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        self.price += DesktopComputer.PROCESSORS[processor]
        self.price += DesktopComputer.RAMS[ram]

        return f"Created {self.manufacturer} {self.model} " \
               f"with {processor} and " \
               f"{ram}GB RAM for {self.price}$."
