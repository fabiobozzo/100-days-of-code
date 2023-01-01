import random

import os

from word_list import *
from hangman_art import stages, logo


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


chosen_word = random.choice(word_list)
word_length = len(chosen_word)

displayed_word = []
for i in range(word_length):
    displayed_word.append("_")

end_of_game = False
lives = 6

print(logo)

while not end_of_game:
    guess = input("\nGuess one letter of the mistery word: ").lower()

    cls()

    if guess in displayed_word:
        print("\nYou already guessed that letter. Please try a new one.")

    for i in range(word_length):
        if chosen_word[i] == guess:
            displayed_word[i] = chosen_word[i]

    if guess not in chosen_word:
        print(f"'{guess}' is not in the mystery word.")
        lives -= 1
        if lives <= 0:
            end_of_game = True
            print("You lost... :((")
            print(f"The mistery word was: {chosen_word}")

    if not "_" in displayed_word:
        end_of_game = True
        print("\nYou won! :))\n")

    print(f"\n{' '.join(displayed_word)}")
    print(stages[lives])
