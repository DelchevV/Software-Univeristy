class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __repr__(self):
        return f"{self.name} {self.surname}"

    def __add__(self, other):
        new_person = Person(self.name, other.surname)
        return new_person


class Group:
    def __init__(self, name: str, people: list):
        self.name = name
        self.people = people

    def __len__(self):
        return len(self.people)

    def __str__(self):
        names = [p.name +" "+ p.surname for p in self.people]
        return f"Group {self.name} with members {', '.join(names)}"

    def __add__(self, other):
        new_group = Group(f"{self.name} {other.name}", self.people + other.people)
        return new_group

    def __repr__(self):
        names = [p.name+" "+p.surname for p in self.people]
        return f"Group {self.name} with members" \
               f" {', '.join(names)}"

    def __getitem__(self, index):
        return f"Person {index}: {self.people[index].name + ' '+ self.people[index].surname}"



