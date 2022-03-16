import random
import pickle
import os
import re
from dataclasses import dataclass, field
from typing import List

@dataclass
class HangedManGame():
    word_to_guess: str = field(init=False)
    continue_to_play: bool = True
    player: str = None
    round_to_play: int = 8
    word_hidden: str = field(init=False)
    letters_played: List[str] = field(default_factory=list)
    scores_file_name: str = os.path.dirname(__file__) +  "/scores"
    words_file_name: str = os.path.dirname(__file__) + "/words.txt"

    def __post_init__(self):
        self.word_to_guess = self.get_word()
        self.word_hidden = self.hide_word(self.word_to_guess)

    def get_word(self):
        with open(self.words_file_name, "r") as words_file:
            words = words_file.read().split(',')
            return random.choice(words)

    def load_scores(self):
        if os.path.exists(self.scores_file_name) > 0:
            with open(self.scores_file_name, "rb") as scores_file:
                unpickler = pickle.Unpickler(scores_file)
                scores = unpickler.load()
        else:
            scores = {}

        return scores

    def hide_word(self, word):
        word_hidden = ""
        for _ in word:
            word_hidden += "*"
        return word_hidden

    def guess_word(self, proposed_word):
        good_guess = proposed_word == self.word_to_guess
        if not good_guess:
            self.round_to_play -= 1
        return good_guess

    def manage_letter(self, letter):
        if not letter.isalpha():
            return None

        self.letters_played.append(letter)

        letter_occurrence = [l.start() for l in re.finditer(letter, self.word_to_guess)]

        if len(letter_occurrence) > 0:
            word_hidden_letter_list = list(self.word_hidden)
            for l in letter_occurrence:
                word_hidden_letter_list[l] = letter

            self.word_hidden = "".join(word_hidden_letter_list)

            return True
        else:
            self.round_to_play -= 1
            return False

    def save_scores(self, player_name, score):
        scores = self.load_scores()
        if player_name in scores:
            scores[player_name] = scores[player_name] + score
        else:
            scores[player_name] = score

        with open(self.scores_file_name, "wb") as scores_file:
            pickler = pickle.Pickler(scores_file)
            pickler.dump(scores)


    def continue_game(self, player):
        want_to_play = input("Do you want to continue to play? [y/n] ")
        want_to_play = str(want_to_play)
        if want_to_play.lower() == "n":
            scores = self.load_scores()
            print(f"Here's your scores {scores[player]}. Bye!")
            return False
        else:
            print("Launching a new game")
            return True