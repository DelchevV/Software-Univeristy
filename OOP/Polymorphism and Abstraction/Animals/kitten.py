from Animals.cat import Cat



class Kitten(Cat):
    GENDER = 'Female'

    def __init__(self, name, age,gender=GENDER):
        super(Kitten, self).__init__(name, age,gender)
        self.gender = Kitten.GENDER

    def make_sound(self):
        return f'Meow'






