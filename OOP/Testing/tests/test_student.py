from unittest import TestCase, main

from projects.student import Student


class TestStudent(TestCase):
    def setUp(self):
        self.student=Student("ime")

    def test_correct_initialization(self):
        self.assertEqual("Ivan", self.student.name)



if __name__ == "__main__":
    main()