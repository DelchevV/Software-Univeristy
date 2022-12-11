from project.library import Library
from unittest import TestCase,main

class TestLib(TestCase):
    def setUp(self):
        self.library=Library("Store1")

    def test_correct_initialization(self):
        self.assertEqual("Store1", self.library.name)
        self.assertEqual({}, self.library.books_by_authors)
        self.assertEqual({}, self.library.readers)

    def test_giving_empty_string_name(self):
        with self.assertRaises(ValueError) as ve:
            self.library.name=""
        self.assertEqual("Name cannot be empty string!", str(ve.exception))

    def test_add_new_book_with_new_author(self):
        self.library.add_book("A1", "b1")
        self.assertEqual({"A1":["b1"]}, self.library.books_by_authors)
        self.library.add_book("A1", "b2")
        self.assertEqual({"A1": ["b1", "b2"]}, self.library.books_by_authors)
        self.library.add_book("A1", "b2")
        self.assertEqual({"A1": ["b1", "b2"]}, self.library.books_by_authors)

    def test_add_already_added_reader(self):
        self.library.readers["Ivan"]=[]
        result=self.library.add_reader("Ivan")
        self.assertEqual(f"Ivan is already registered in the Store1 library.", result)

    def test_add_new_reader(self):
        self.library.add_reader("Ivan")
        self.library.add_reader("Gosho")
        self.assertEqual({"Ivan":[], "Gosho":[]}, self.library.readers)

    def test_rent_a_book_with_invalid_reader_name(self):
        self.library.books_by_authors["A1"]=["b1", "b2"]
        result=self.library.rent_book("Ivan", "A1", "b1")
        self.assertEqual("Ivan is not registered in the Store1 Library.", result)

    def test_rent_book_with_invalid_author(self):
        self.library.books_by_authors["A1"] = ["b1", "b2"]
        self.library.readers["Ivan"]=[]
        result = self.library.rent_book("Ivan", "Invalid", "b1")
        self.assertEqual("Store1 Library does not have any Invalid's books.",result)

    def test_rent_invalid_book(self):
        self.library.books_by_authors["A1"] = ["b1", "b2"]
        self.library.readers["Ivan"] = []
        result = self.library.rent_book("Ivan", "A1", "b3")
        self.assertEqual("""Store1 Library does not have A1's "b3".""", result)

    def test_rent_valid_book(self):
        self.library.books_by_authors["A1"] = ["b1", "b2"]
        self.library.readers["Ivan"] = []
        self.library.rent_book("Ivan", "A1", "b1")
        self.assertEqual({"A1":["b2"]}, self.library.books_by_authors)
        self.assertEqual({"Ivan":[{"A1":"b1"}]}, self.library.readers)
        

if __name__=="__main__":
    main()
