from unittest import TestCase, main

from projects.list import IntegerList


class TestList(TestCase):
    def setUp(self):
        self.integer_list=IntegerList(1,1.5,"h",2,3)

    def test_valid_initialization(self):
        self.assertEqual([1,2,3],self.integer_list._IntegerList__data)

    def test_add_not_integer_element_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.add("100")
        self.assertEqual("Element is not Integer", str(ve.exception))

    def test_add_number_to_integer_list(self):
        self.integer_list.add(4)
        self.assertEqual([1,2,3,4],self.integer_list._IntegerList__data)

    def test_remove_index_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.remove_index(8)
        self.assertEqual("Index is out of range",str(ie.exception))

    def test_remove_index_proper_removing(self):
        self.integer_list.remove_index(0)
        self.assertEqual([2,3], self.integer_list._IntegerList__data)

    def test_get_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.get(8)
        self.assertEqual("Index is out of range",str(ie.exception))

    def test_get_valid_number(self):
        self.assertEqual(1, self.integer_list.get(0))

    def test_insert_raise_index_error(self):
        with self.assertRaises(IndexError) as ie:
            self.integer_list.insert(10,2)
        self.assertEqual("Index is out of range",str(ie.exception))

    def test_insert_not_integer_raise_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.integer_list.insert(1,"j")
        self.assertEqual("Element is not Integer",str(ve.exception))

    def test_valid_inserting(self):
        self.integer_list.insert(1, 4)
        self.assertEqual([1,4,2,3],self.integer_list._IntegerList__data)

    def test_get_biggest(self):
        self.assertEqual(3, self.integer_list.get_biggest())

    def test_get_index(self):
        self.assertEqual(0,self.integer_list.get_index(1))



if __name__=="__main__":
    main()