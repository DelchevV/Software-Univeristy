from project.plantation import Plantation
from unittest import TestCase, main




class TestPlantation(TestCase):
    def setUp(self):
        self.plantation = Plantation(10)

    def test_valid_initialization(self):
        self.assertEqual(10, self.plantation.size)
        self.assertEqual(dict(), self.plantation.plants)
        self.assertEqual(list(), self.plantation.workers)

    def test_negative_size_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.size = -4
        self.assertEqual("Size must be positive number!", str(ve.exception))

    def test_hire_existing_worker(self):
        self.plantation.workers.append("Jimmy")
        with self.assertRaises(ValueError) as ve:
            self.plantation.hire_worker("Jimmy")
        self.assertEqual("Worker already hired!", str(ve.exception))

    def test_hire_new_worker(self):
        self.assertEqual("Jimmy successfully hired.", self.plantation.hire_worker("Jimmy"))
        self.assertEqual(["Jimmy"], self.plantation.workers)

    def test_proper_counting_of_len_method(self):
        self.plantation.plants["Jimmy"] = ["tulip", "other", "dont know other species"]
        self.assertEqual(3, len(self.plantation))

    def test_planting_with_not_existing_worker(self):
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Jimmy", "tulip")
        self.assertEqual("Worker with name Jimmy is not hired!", str(ve.exception))

    def test_planting_plants_with_full_garden_raise_error(self):
        self.plantation.workers.append("Jimmy")
        self.plantation.size = 3
        self.plantation.plants["Jimmy"] = ["tulip", "other", "dont know other species"]
        with self.assertRaises(ValueError) as ve:
            self.plantation.planting("Jimmy", "flower")
        self.assertEqual("The plantation is full!", str(ve.exception))

    def test_planting_plant_by_existing_worker(self):
        self.plantation.workers.append("Jimmy")
        self.plantation.plants["Jimmy"] = ["tulip"]
        result = self.plantation.planting("Jimmy", "flower")
        self.assertEqual(f"Jimmy planted flower.", result)
        self.assertEqual(["tulip", "flower"], self.plantation.plants["Jimmy"])

    def test_planting_plant_by_new_worker(self):
        self.plantation.workers.append("Jimmy")
        result = self.plantation.planting("Jimmy", "flower")
        self.assertEqual("Jimmy planted it's first flower.", result)
        self.assertEqual(["flower"], self.plantation.plants["Jimmy"])

    def test_string_representation(self):
        self.plantation.plants["Jimmy"] = ["f1", "f2"]
        self.plantation.plants["Woddie"] = ["f1", "f2"]
        result = [
            "Plantation size: 10",
            '\n'
            "Jimmy planted: f1, f2",
            "Woddie planted: f1, f2"
        ]
        self.assertEqual("\n".join(result), str(self.plantation))

    def test_representation(self):
        self.plantation.workers = ["Jimmy", "Woddie"]
        result = 'Size: 10\n' \
                 'Workers: Jimmy, Woddie'

        self.assertEqual(result, repr(self.plantation))


if __name__ == "__main__":
    main()
