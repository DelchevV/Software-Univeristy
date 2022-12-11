from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team("Bulls")

    def test_correct_initialization(self):
        self.assertEqual("Bulls", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_giving_name_with_numbers(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "12A"
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_correct_adding_members(self):
        self.team.members["Peter"] = 12
        members = {
            "Peter": 16,
            "Jonson": 22
        }
        result = self.team.add_member(**members)
        self.assertEqual("Successfully added: Jonson", result)
        self.assertEqual({"Peter": 12, "Jonson": 22}, self.team.members)

    def test_remove_not_existing_member(self):
        self.team.members["Peter"] = 12
        result = self.team.remove_member("Ivan")
        self.assertEqual("Member with name Ivan does not exist", result)

    def test_remove_existing_member(self):
        self.team.members["Peter"] = 12
        self.team.members["Jonson"] = 12
        result = self.team.remove_member("Peter")
        self.assertEqual("Member Peter removed", result)
        self.assertEqual({"Jonson": 12}, self.team.members)

    def test_gt(self):
        self.other_team = Team("Bucks")
        self.other_team.members["Gosho"] = 14
        self.other_team.members["Rick"] = 14
        result = self.team.__gt__(self.other_team)
        self.assertEqual(False, result)

        self.team.members["Gosho"] = 14
        self.team.members["Rick"] = 14
        self.team.members["Mickey"] = 14
        result = self.team.__gt__(self.other_team)
        self.assertEqual(True, result)

    def test_valid_len_of_members(self):
        self.team.members["Gosho"] = 14
        self.team.members["Rick"] = 14
        self.team.members["Mickey"] = 14
        self.assertEqual(3, len(self.team))

    def test_valid_adding_new_team(self):
        self.team.members["Gosho"] = 14
        self.team.members["Rick"] = 14
        self.team.members["Mickey"] = 14

        self.other_team = Team("Bucks")
        self.other_team.members["Ivan"] = 14
        self.other_team.members["Mick"] = 14

        name = f"{self.team.name}{self.other_team.name}"
        self.new_team = Team(name)
        self.new_team.add_member(**self.team.members)
        self.new_team.add_member(**self.other_team.members)
        self.assertEqual(self.new_team.name, "BullsBucks")
        members = {
            "Gosho": 14,
            "Rick": 14,
            "Mickey": 14,
            "Ivan": 14,
            "Mick": 14,
        }
        self.assertEqual(self.new_team.members, members)

    def test_correct_string(self):
        self.team.members["A"] = 14
        self.team.members["B"] = 14
        self.team.members["C"] = 14
        result = [
            "Team name: Bulls",
            "Member: A - 14-years old",
            "Member: B - 14-years old",
            "Member: C - 14-years old"
        ]
        self.assertEqual("\n".join(result), self.team.__str__())


if __name__ == "__main__":
    main()
