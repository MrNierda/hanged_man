from random import choice
from re import finditer
from os.path import dirname
from dataclasses import dataclass, field
from typing import List

@dataclass(frozen=True)
class _Constant:
    MAX_ROUND_TO_PLAY = 8

@dataclass
class HangedManGame():
    word_to_guess: str = field(init=False)
    round_to_play: int = _Constant.MAX_ROUND_TO_PLAY
    word_hidden: str = field(init=False)
    letters_played: List[str] = field(default_factory=list)
    words_file_name: str = dirname(__file__) + "/words.txt"

    def __post_init__(self):
        self.word_to_guess = self.get_word()
        self.hide_word()

    def get_word(self):
        with open(self.words_file_name, "r") as words_file:
            words = words_file.read().split(',')
            return choice(words)

    def hide_word(self):
        word_hidden = ""
        for _ in self.word_to_guess:
            word_hidden += "*"
        self.word_hidden=word_hidden

    def guess_word(self, proposed_word):
        good_guess = proposed_word == self.word_to_guess
        if not good_guess:
            self.round_to_play -= 1
        return good_guess

    def guess_letter(self, letter):
        if not letter.isalpha():
            return None

        self.letters_played.append(letter)

        letter_occurrence = [l.start() for l in finditer(letter, self.word_to_guess)]

        if len(letter_occurrence) > 0:
            word_hidden_letter_list = list(self.word_hidden)
            for l in letter_occurrence:
                word_hidden_letter_list[l] = letter

            self.word_hidden = "".join(word_hidden_letter_list)

            return True
        else:
            self.round_to_play -= 1
            return False
