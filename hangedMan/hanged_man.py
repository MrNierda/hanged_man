# -*-coding:utf-8 -*

import sys
import random
import pickle
import os
import re
from dataclasses import dataclass, field
# from .hanged_man_function import *
from typing import List

# player = get_player_name()

# continue_to_play = True

# while continue_to_play:
#     word_to_guess = get_word()
#     word_hidden = hide_word(word_to_guess)

#     round_to_play = 8

#     print(f'Try to find the hidden world {word_hidden}\n')

#     while round_to_play > 0 and not word_to_guess == word_hidden:
#         print(f'Player {player} has {round_to_play} chances to find the hidden word\n')

#         (word_hidden, was_good_letter) = propose_letter(word_to_guess, word_hidden)
#         if not was_good_letter:
#             round_to_play -= 1

#         print(f'The word to guess is {word_hidden}\n')

#         tryToFindTheWord = input("Do you want to propose a word? [y/N] ")
#         tryToFindTheWord = str(tryToFindTheWord)
#         if tryToFindTheWord.lower() == "y":
#             success = guess_word(word_to_guess)
#             if success:
#                 print(f"You mark {round_to_play} points")
#                 save_scores(player, round_to_play)
#                 break
#             else:
#                 print("You didn't find the word")
#                 round_to_play -= 1

#     continue_to_play = continue_game(player)

# sys.stdin.read(1)

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

    def init_game(self):
        self.player = self.get_player_name()

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


    def save_scores(self, player_name, score):
        scores = self.load_scores()
        if player_name in scores:
            scores[player_name] = scores[player_name] + score
        else:
            scores[player_name] = score

        with open(self.scores_file_name, "wb") as scores_file:
            pickler = pickle.Pickler(scores_file)
            pickler.dump(scores)


    def get_player_name(self):
        player_name = input("Write your name: ")
        player_name = player_name.capitalize()
        return player_name


    def hide_word(self, word):
        word_hidden = ""
        for _ in word:
            word_hidden += "*"
        return word_hidden


    def guess_word(self, word_to_guess):
        word_proposed = input("Enter the word you want to propose: ")
        word_proposed = str(word_proposed)
        print(f'word proposed {word_proposed}, word to guess {word_to_guess}')
        if word_proposed == word_to_guess:
            print(f"Congratulations, you found the hidden word {word_to_guess}")
            return True
        else:
            return False


    def propose_letter(self, word_to_guess, word_hidden):
        letter = input("Write the letter you want to propose: ")
        letter = letter.lower()
        if len(letter) > 1 or not letter.isalpha():
            print("Your letter in invalid")
            return self.propose_letter(word_to_guess, word_to_guess)

        self.letters_played.append(letter)

        letter_occurrence = [l.start() for l in re.finditer(letter, word_to_guess)]

        if len(self, letter_occurrence) > 0:
            print(f"This letter {letter} is present {len(letter_occurrence)} times in the word")
            word_hidden_letter_list = list(word_hidden)
            for l in letter_occurrence:
                word_hidden_letter_list[l] = letter

            return "".join(word_hidden_letter_list), True
        else:
            print(f"This letter {letter} is not in the word")
            return word_hidden, False

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