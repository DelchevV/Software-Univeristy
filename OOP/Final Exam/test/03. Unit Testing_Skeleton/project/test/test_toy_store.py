from project.toy_store import ToyStore
from unittest import TestCase, main


class TestToyStore(TestCase):
    def setUp(self):
        self.store = ToyStore()

    def test_valid_initialization(self):
        self.assertEqual({'A': None, 'B': None, 'C': None, 'D': None, 'E': None, 'F': None, 'G': None},
                         self.store.toy_shelf)

    def test_adding_toy_to_not_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("Q", "Dog")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_adding_toy_in_shelf_with_the_same_toy(self):
        self.store.toy_shelf["A"] = "Dog"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Dog")
        self.assertEqual("Toy is already in shelf!", str(ex.exception))

    def test_adding_toy_to_filled_shelf(self):
        self.store.toy_shelf["A"] = "Dog"
        with self.assertRaises(Exception) as ex:
            self.store.add_toy("A", "Doll")
        self.assertEqual("Shelf is already taken!", str(ex.exception))

    def test_adding_toy_expect_success(self):
        result = self.store.add_toy("A", "Doll")
        self.assertEqual("Toy:Doll placed successfully!", result)
        self.assertEqual("Doll", self.store.toy_shelf["A"])

    def test_removing_toy_from_not_existing_shelf(self):
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("Q", "Dog")
        self.assertEqual("Shelf doesn't exist!", str(ex.exception))

    def test_removing_invalid_toy_from_shelf(self):
        self.store.toy_shelf["A"] = "Doll"
        with self.assertRaises(Exception) as ex:
            self.store.remove_toy("A", "Dog")
        self.assertEqual("Toy in that shelf doesn't exists!", str(ex.exception))

    def test_removing_toy_expect_success(self):
        self.store.add_toy("A", "Doll")
        result = self.store.remove_toy("A", "Doll")
        self.assertEqual("Remove toy:Doll successfully!", result)
        self.assertEqual(None, self.store.toy_shelf["A"])


if __name__ == "__main__":
    main()
