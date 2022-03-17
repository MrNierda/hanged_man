import unittest
from unittest.mock import patch, mock_open
from hangedMan.hanged_man import HangedManGame, _Constant

class FunctionTest(unittest.TestCase):

    hanged_man = None

    def setUp(self):
        self.hanged_man = HangedManGame()
        self.hanged_man.word_to_guess = "python"
        self.hanged_man.word_hidden = "******"

    @patch("builtins.open", mock_open(read_data="python,hello,world"))
    def test_get_word(self):
        words = ["python", "hello", "world"]
        returned_value = self.hanged_man.get_word()
        self.assertIn(returned_value, words)

    def test_hide_word(self):
        self.hanged_man.word_to_guess = "python"
        self.hanged_man.hide_word()
        self.assertEqual("******", self.hanged_man.word_hidden)

    def test_correct_guess_word(self):
        self.assertTrue(self.hanged_man.guess_word("python"))
        self.assertEqual(_Constant.MAX_ROUND_TO_PLAY, self.hanged_man.round_to_play)

    def test_incorrect_guess_word(self):
        self.assertFalse(self.hanged_man.guess_word("badGuess"))
        self.assertEqual(_Constant.MAX_ROUND_TO_PLAY - 1, self.hanged_man.round_to_play)

    def test_correct_guess_letter(self):
        self.assertTrue(self.hanged_man.guess_letter("y"))
        self.assertEqual(_Constant.MAX_ROUND_TO_PLAY, self.hanged_man.round_to_play)
        self.assertEqual(["y"], self.hanged_man.letters_played)
        self.assertEqual("*y****", self.hanged_man.word_hidden)

    def test_incorrect_guess_letter(self):
        self.assertFalse(self.hanged_man.guess_letter("z"))
        self.assertEqual(_Constant.MAX_ROUND_TO_PLAY - 1, self.hanged_man.round_to_play)
        self.assertEqual(["z"], self.hanged_man.letters_played)
        self.assertEqual("******", self.hanged_man.word_hidden)

    def test_incorrect_non_alpha_guess_letter(self):
        self.assertIsNone(self.hanged_man.guess_letter("5"))
        self.assertEqual(_Constant.MAX_ROUND_TO_PLAY, self.hanged_man.round_to_play)

if __name__ == '__main__':
    unittest.main()