from unittest import TestCase,main

from projects.vehicle import Vehicle


class TestVehicle(TestCase):
    def setUp(self):
        self.vehicle=Vehicle(10,140)

    def test_correct_initialization(self):
        self.assertEqual(10, self.vehicle.fuel)
        self.assertEqual(10, self.vehicle.capacity)
        self.assertEqual(140, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_without_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(10000)

        self.assertEqual("Not enough fuel",str(ex.exception))

    def test_drive_successfully_the_given_distance(self):
        self.vehicle.drive(1)
        self.assertEqual(8.75, self.vehicle.fuel)

    def test_refueling_with_too_much_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(2000)

        self.assertEqual("Too much fuel",str(ex.exception))

    def test_refueling_legit_amount_of_fuel(self):
        self.vehicle.fuel=0
        self.vehicle.refuel(5)
        self.assertEqual(5,self.vehicle.fuel)

    def test_proper_string_representation(self):
        self.assertEqual(f"The vehicle has 140 horse power with 10 fuel left and 1.25 fuel consumption",self.vehicle.__str__())

if __name__=="__main__":
    main()