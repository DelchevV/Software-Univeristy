from unittest import TestCase, main

from project.train.train import Train


class TestTrain(TestCase):
    def setUp(self):
        self.train = Train("pof_paf", 1)

    def test_correct_initialization(self):
        self.assertEqual("pof_paf", self.train.name)
        self.assertEqual(20, self.train.capacity)
        self.assertEqual([], self.train.passengers)

    def test_add_to_many_people(self):
        self.train.passengers = ["Peter"]
        with self.assertRaises(ValueError) as ve:
            self.train.add("Mike")
        self.assertEqual("Train is full", str(ve.exception))

    def test_add_already_existing_passenger(self):
        self.train.capacity = 2
        self.train.passengers = ["Peter"]

        with self.assertRaises(ValueError) as ve:
            self.train.add("Peter")
        self.assertEqual("Passenger Peter Exists", str(ve.exception))

    def test_adding_valid_passenger(self):
        self.train.passengers = ["Peter"]
        self.train.capacity = 2
        result = self.train.add("Mike")
        self.assertEqual("Added passenger Mike", result)

    def test_removing_invalid_person(self):
        with self.assertRaises(ValueError) as ve:
            self.train.remove("Gosho")
        self.assertEqual("Passenger Not Found", str(ve.exception))

    def test_removing_valid_person(self):
        self.train.passengers = ["Peter"]
        result=self.train.remove("Peter")
        self.assertEqual("Removed Peter", result)



if __name__ == "__main__":
    main()
