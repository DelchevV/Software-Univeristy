from unittest import TestCase, main

from projects.cat import Cat


class TestCat(TestCase):
    def setUp(self):
        self.cat = Cat("Sushi")

    def test_correct_initialization(self):
        self.assertEqual("Sushi", self.cat.name)
        self.assertFalse(self.cat.fed)
        self.assertFalse(self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_eat_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()

        self.assertEqual('Already fed.', str(ex.exception))

    def test_change_cat_attributes_after_eat(self):
        self.cat.eat()
        self.assertTrue(self.cat.fed)
        self.assertTrue(self.cat.sleepy)
        self.assertEqual(1,self.cat.size)

    def test_cat_sleep_expect_to_be_false(self):
        self.cat.fed=True
        self.cat.sleepy=True

        self.cat.sleep()

        self.assertFalse(self.cat.sleepy)

    def test_cat_sleep_when_cat_is_not_fed_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()

        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

if __name__ == "__main__":
    main()
