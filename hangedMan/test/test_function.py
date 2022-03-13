import unittest
from unittest.mock import patch
from hanged_man_function import *

""" to execute test
    all : python3 -m unittest 
    specific : python3 -m unittest test.test_function.FunctionTest.test_get_word (package.module.class.function)
"""

class FunctionTest(unittest.TestCase):

    def setUp(self):
        """Initialisation des tests."""
        self.numbers = list(range(10))

    def test_get_word(self):
        words = ["python", "hello", "nothing", "puppy", "tyre", "school", "jupiter", "google", "machin", "kitty"]
        returned_value = get_word()
        self.assertIn(returned_value, words)

    # mock input example
    @patch('builtins.input', return_value='adrien')
    def test_get_player_name(self, mock_input):
        expected = "Adrien"
        self.assertEqual(get_player_name(), expected)

    @patch('builtins.input', return_value='hello')
    def test_guess_word(self, mock_input):
        self.assertTrue(guess_word("hello"))
        self.assertFalse(guess_word("world"))

    @patch('builtins.input', return_value='L')
    def test_propose_letter(self, mock_input):
        self.assertEqual(propose_letter("hello", "he**o"), ("hello", True))
        self.assertNotEqual(propose_letter("puppy", "*****"), ("*****", True))

    @patch('builtins.input', return_value='n')
    @patch('hanged_man_function.load_scores', return_value={"Adrien":0})
    def test_continue_game_stop(self, mock_input, mock_load_scores):
        self.assertFalse(continue_game("Adrien"))

    @patch('builtins.input', return_value='y')
    def test_continue_game_continue(self, mock_input):
        self.assertTrue(continue_game("Adrien"))


if __name__ == '__main__':
    unittest.main()