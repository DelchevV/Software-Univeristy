from unittest import TestCase, main

from projects.worker import Worker


class TestWorker(TestCase):
    def setUp(self):
        self.worker = Worker('Ivan', 10, 5)

    def test_correct_initialization(self):
        self.assertEqual("Ivan",self.worker.name)
        self.assertEqual(10,self.worker.salary)
        self.assertEqual(5,self.worker.energy)
        self.assertEqual(0,self.worker.money)

    def test_zero_energy_raise_exception(self):
        self.worker.energy=0
        with self.assertRaises(Exception) as ex:
            self.worker.work()

        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_money_raise_after_work(self):
        self.worker.work()
        self.assertEqual(self.worker.salary, self.worker.money)

    def test_energy_decrease_after_work(self):
        self.worker.work()
        self.assertEqual(4, self.worker.energy)

    def test_rest_expect_energy_raise_by_one(self):
        self.worker.rest()
        self.assertEqual(6,self.worker.energy)

    def test_get_info_correct(self):
        self.assertEqual("Ivan has saved 0 money.", self.worker.get_info())

if __name__ == "__main__":
    main()
