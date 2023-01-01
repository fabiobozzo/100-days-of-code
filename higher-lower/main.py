import art
import game_data
import os
import random


def cls():
    os.system('cls' if os.name == 'nt' else 'clear')


def next_random_profile(current_profile_index):
    """Return an instagram profile's index and data, different than the one at the given index"""
    next_profile_index = current_profile_index
    while next_profile_index == current_profile_index:
        next_profile_index = random.randint(
            0, len(game_data.instagram_profiles)-1)
    return next_profile_index, game_data.instagram_profiles[next_profile_index]


def check_guess(guess, profile_a, profile_b):
    """Given a guess as 'A' or 'B', returns true if the guess about the profile with the highest number of followers is correct, otherwie false"""
    if int(profile_a['follower_count']) > int(profile_b['follower_count']):
        return guess.upper() == 'A'
    else:
        return guess.upper() == 'B'


def print_profile(profile, letter):
    """Pretty-print an instagram profile and its given letter"""
    print(f"Compare {letter.upper()}: {profile['name']}, a {profile['description']} from {profile['country']}.")
    # DEBUG: # print(profile['follower_count'])


def input_guess():
    """Safe input of a profile-letter guess 'A' or 'B'"""
    guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
    if not (guess == "A" or guess == "B"):
        print("Please type 'A' or 'B'")
    return guess


def game():
    current_score = 0
    end_game = False
    index_a, profile_a = next_random_profile(0)
    index_b, profile_b = next_random_profile(index_a)

    while not end_game:
        cls()
        print(art.logo)
        if current_score > 0:
            print(f"You're right! Current score: {current_score}.\n")
        print_profile(profile_a, "a")
        print(art.vs)
        print_profile(profile_b, "b")
        guess = ""
        while not (guess == "A" or guess == "B"):
            guess = input_guess()
        if check_guess(guess, profile_a, profile_b):
            current_score += 1
            index_a = index_b
            profile_a = profile_b
            index_b, profile_b = next_random_profile(index_a)
        else:
            end_game = True
            cls()
            print(art.logo)
            print(f"Sorry, that's wrong. Final score: {current_score}.")

play_again = True
while play_again:
    game()
    if input("\nWanna play again? (y/n) ").lower() != 'y':
        play_again = False
        print("Bye.")
