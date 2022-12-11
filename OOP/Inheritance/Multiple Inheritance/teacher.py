from Person.employee import Employee
from Person.person import Person


class Teacher(Employee, Person):
    def teach(self):
        return "teaching..."


