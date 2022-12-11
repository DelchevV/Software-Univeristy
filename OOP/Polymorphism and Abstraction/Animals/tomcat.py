from Animals.cat import Cat


class Tomcat(Cat):
    GENDER = "Male"

    def __init__(self, name, age, gender=GENDER):
        super(Tomcat, self).__init__(name, age, gender)
        self.gender = Tomcat.GENDER

    def make_sound(self):
        return 'Hiss'
