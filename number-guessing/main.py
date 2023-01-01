import constants
import random

def set_attempts_number_by_chosen_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if difficulty != "easy":
        difficulty = "hard"
    return constants.ATTEMPTS[difficulty]

number_to_guess = random.randint(1, 100)

print(constants.LOGO)
print(constants.INTRO)
#print(f"Pssst, the correct answer is {number_to_guess}")

attempts_left = set_attempts_number_by_chosen_difficulty()

win = False
while attempts_left > 0 and not win:
    print(f"\nYou have {attempts_left} left to guess the number.")
    guessed_number = int(input("Make a guess: "))
    if guessed_number == number_to_guess:
        win = True
        print("You guessed the right number. Congratulations, you win!")
    else: 
        attempts_left -= 1
        if guessed_number > number_to_guess:
            print("Too high.")
        else:
            print("Too low.")
        if attempts_left > 0:
            print("Guess again.")
        else:
            print(f"You've run out of guesses, you lose. The number was: {number_to_guess}")
    