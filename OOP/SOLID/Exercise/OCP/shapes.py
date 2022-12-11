from abc import ABC, abstractmethod


class AreaCalculator:

    def __init__(self, shapes):
        assert isinstance(shapes, list), "`shapes` should be of type `list`."
        self.shapes = shapes

    @property
    def total_area(self):
        total = 0
        for shape in self.shapes:
            total += shape.get_area()

        return total


class Shape(ABC):
    def __init__(self):
        pass

    @abstractmethod
    def get_area(self):
        pass


class Rectangle(Shape):

    def __init__(self, width, height):
        super().__init__()
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width


class Triangle(Shape):

    def __init__(self, width, height):
        super(Triangle, self).__init__()
        self.width = width
        self.height = height

    def get_area(self):
        return self.height * self.width / 2


shapes = [Rectangle(1, 6), Triangle(2, 3)]
calculator = AreaCalculator(shapes)

print("The total area is: ", calculator.total_area)

