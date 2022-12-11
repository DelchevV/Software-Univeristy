from unittest import TestCase,main

from projects.mammal import Mammal


class TestMammal(TestCase):
    def setUp(self):
        self.mammal=Mammal("Rex","dog",'woof')

    def test_correct_initialization(self):
        self.assertEqual('Rex',self.mammal.name)
        self.assertEqual('dog',self.mammal.type)
        self.assertEqual('woof',self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_make_sound(self):
        self.assertEqual("Rex makes woof", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_get_info(self):
        self.assertEqual("Rex is of type dog", self.mammal.info())

if __name__=="__main__":
    main()