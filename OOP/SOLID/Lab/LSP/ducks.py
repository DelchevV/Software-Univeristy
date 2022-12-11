from abc import abstractmethod, ABC


class Duck(ABC):
    def __init__(self):
        pass
    @abstractmethod
    def quack(self):
        pass


class RubberDuck(Duck):

    def quack(self):
        return "Squeek"


class RobotDuck(Duck):
    HEIGHT = 50

    def __init__(self):
        super(RobotDuck, self).__init__()
        self.height = 0

    def quack(self):
        return 'Robotic quacking'

    @staticmethod
    def walk():
        return 'Robotic walking'

    def fly(self):
        """can only fly to specific height but
        when it reaches it starts landing automatically"""
        if self.height == RobotDuck.HEIGHT:
            self.land()
        else:
            self.height += 1

    def land(self):
        self.height = 0


r_duck=RubberDuck()
robot_duck=RobotDuck()

print(r_duck.quack())

print(robot_duck.quack())
print(robot_duck.walk())
print(robot_duck.fly())