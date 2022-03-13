# -*-coding:utf-8 -*

import random
import pickle
import os
import re

round_to_play = 8
scores_file_name = os.path.dirname(__file__) +  "/scores"
words_file_name = os.path.dirname(__file__) + "/words.txt"

def get_word():
    with open(words_file_name, "r") as words_file:
        words = words_file.read().split(',')
        return random.choice(words)


def load_scores():
    if os.path.exists(scores_file_name) > 0:
        with open(scores_file_name, "rb") as scores_file:
            unpickler = pickle.Unpickler(scores_file)
            scores = unpickler.load()
    else:
        scores = {}

    return scores


def save_scores(player_name, score):
    scores = load_scores()
    if player_name in scores:
        scores[player_name] = scores[player_name] + score
    else:
        scores[player_name] = score

    with open(scores_file_name, "wb") as scores_file:
        pickler = pickle.Pickler(scores_file)
        pickler.dump(scores)


def get_player_name():
    player_name = input("Write your name: ")
    player_name = player_name.capitalize()
    return player_name


def hide_word(word):
    word_hidden = ""
    for _ in word:
        word_hidden += "*"
    return word_hidden


def guess_word(word_to_guess):
    word_proposed = input("Enter the word you want to propose: ")
    word_proposed = str(word_proposed)
    print(f'word proposed {word_proposed}, word to guess {word_to_guess}')
    if word_proposed == word_to_guess:
        print(f"Congratulations, you found the hidden word {word_to_guess}")
        return True
    else:
        return False


def propose_letter(word_to_guess, word_hidden):
    letter = input("Write the letter you want to propose: ")
    letter = letter.lower()
    if len(letter) > 1 or not letter.isalpha():
        print("Your letter in invalid")
        return propose_letter(word_to_guess, word_to_guess)

    letter_occurrence = [l.start() for l in re.finditer(letter, word_to_guess)]

    if len(letter_occurrence) > 0:
        print(f"This letter {letter} is present {len(letter_occurrence)} times in the word")
        word_hidden_letter_list = list(word_hidden)
        for l in letter_occurrence:
            word_hidden_letter_list[l] = letter

        return "".join(word_hidden_letter_list), True
    else:
        print(f"This letter {letter} is not in the word")
        return word_hidden, False

def continue_game(player):
    want_to_play = input("Do you want to continue to play? [y/n] ")
    want_to_play = str(want_to_play)
    if want_to_play.lower() == "n":
        scores = load_scores()
        print(f"Here's your scores {scores[player]}. Bye!")
        return False
    else:
        print("Launching a new game")
        return True