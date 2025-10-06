import os
import tempfile
import unittest

from examples import (calc, guess_game, inventory, primes_under_n,
                      profile_save, string_utils)


class TestExamples(unittest.TestCase):

    def test_calc_basic(self):
        self.assertEqual(calc.calculate(2, 3, '+'), 5)
        self.assertEqual(calc.calculate(5, 2, '/'), 2.5)
        self.assertEqual(calc.calculate(5, 0, '/'), "Error: divide by zero")

    def test_profile_format_parse(self):
        line = profile_save.format_profile('Bob', 30, 'NY')
        parsed = profile_save.parse_profile(line)
        self.assertEqual(parsed['name'], 'Bob')
        self.assertEqual(parsed['age'], '30')

    def test_inventory_save_load(self):
        inv = {}
        inventory.add_item(inv, 'apple', 3)
        inventory.add_item(inv, 'banana', 2)
        fd, path = tempfile.mkstemp(suffix='.csv')
        os.close(fd)
        try:
            inventory.save_inventory(inv, path)
            loaded = inventory.load_inventory(path)
            self.assertEqual(loaded.get('apple'), 3)
            self.assertEqual(loaded.get('banana'), 2)
        finally:
            os.remove(path)

    def test_primes(self):
        self.assertIn(2, primes_under_n.list_primes(10))
        self.assertNotIn(4, primes_under_n.list_primes(10))

    def test_string_utils(self):
        self.assertEqual(string_utils.reverse_string('abc'), 'cba')
        self.assertTrue(string_utils.is_palindrome('Racecar'))
        self.assertEqual(string_utils.count_vowels('abcde'), 2)

    def test_guess_game_logic(self):
        secret = guess_game.pick_secret(1, 1)
        ok, hint = guess_game.check_guess(secret, 1)
        self.assertTrue(ok)


if __name__ == '__main__':
    unittest.main()
