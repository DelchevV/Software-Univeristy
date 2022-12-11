from unittest import TestCase, main

from projects.hero import Hero


class TestHero(TestCase):
    def setUp(self):
        self.hero = Hero("Ivan", 10, 100, 20)
        self.enemy = Hero("Strahil", 20, 200, 40)

    def test_correct_initialization(self):
        self.assertEqual('Ivan', self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(100, self.hero.health)
        self.assertEqual(20, self.hero.damage)

    def test_battling_against_yourself_raise_exception(self):
        self.enemy.username="Ivan"
        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_zero_health(self):
        self.hero.health = 0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)

        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_enemy_hero_zero_health(self):
        self.enemy.health=0
        with self.assertRaises(ValueError) as ve:
            self.hero.battle(self.enemy)
        self.assertEqual("You cannot fight Strahil. He needs to rest",str(ve.exception))

    def test_is_the_game_draw(self):
        self.hero.damage=10
        self.hero.health=100
        self.hero.level=10

        self.enemy.damage = 10
        self.enemy.health = 100
        self.enemy.level = 10
        self.assertEqual("Draw",self.hero.battle(self.enemy))

    def test_if_hero_wins_proper_stats_increasing(self):
        self.hero.damage = 10
        self.hero.health = 100
        self.hero.level = 10

        self.enemy.damage = 0
        self.enemy.health = 100
        self.enemy.level = 0

        self.assertEqual("You win", self.hero.battle(self.enemy))
        self.assertEqual(11,self.hero.level)
        self.assertEqual(105,self.hero.health)
        self.assertEqual(15,self.hero.damage)

    def test_if_enemy_wins_proper_stats_increasing(self):
        self.hero.damage = 0
        self.hero.health = 100
        self.hero.level = 0

        self.enemy.damage = 10
        self.enemy.health = 100
        self.enemy.level = 10

        self.assertEqual("You lose", self.hero.battle(self.enemy))
        self.assertEqual(11, self.enemy.level)
        self.assertEqual(105, self.enemy.health)
        self.assertEqual(15, self.enemy.damage)

    def test_proper_string_representation(self):
        result=f"Hero Ivan: 10 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 20\n"
        self.assertEqual(result, self.hero.__str__())



if __name__ == '__main__':
    main()
