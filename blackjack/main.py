import art
import random
import os
import time

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')

def deal_card():
    """"Picks a random card from the blackjack infinite deck and return its value."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def calculate_score(cards):
    """Take a list of cards, calculate and return the score value, considering the ace rule."""
    score = sum(cards)
    if score > 21 and 11 in cards:
        cards.remove(11)
        cards.append(1)
        score = sum(cards)
    return score

def is_blackjack(cards):
    """Take a list of cards and determine whether they are a blackjack or not."""
    return len(cards) == 2 and 11 in cards and 10 in cards

def format_cards(cards, covered):
    """Take a list of cards and print them nicely to the stdout. If covered is True, only the first card is revealed."""
    formatted = f" {cards[0]}"
    for i in range(1,len(cards)):
        card = str(cards[i])
        if covered:
            card = "X"
        formatted += f" {card}"

    formatted = f"[{formatted} ]"
    if not covered:
        formatted += f" = {calculate_score(cards)}"

    return formatted

def print_table(player_cards, dealer_cards, dealer_covered):
    """"Print the blackjack table to stdout."""
    cls()
    print(art.logo)
    print(f"Dealer cards: {format_cards(dealer_cards, dealer_covered)}")
    print(f"Your cards: {format_cards(player_cards, False)}")

def play_game():
    winner = ""
    blackjack = False
    
    player_cards = []
    player_cards.append(deal_card())
    player_cards.append(deal_card())
    
    dealer_cards = []
    dealer_cards.append(deal_card())
    dealer_cards.append(deal_card())

    another_card = True
    while another_card and winner == "": 
        print_table(player_cards, dealer_cards, True)

        if is_blackjack(player_cards):
            winner = "player"
            blackjack = True
        elif is_blackjack(dealer_cards):
            winner = "dealer"
            blackjack = True
        elif calculate_score(player_cards) > 21:
            winner = "dealer"

        if winner == "":
            if input("\nDo you want another card? (y/n) ").lower() == 'y':
                player_cards.append(deal_card())
            else:
                another_card = False
    
    if winner == "":
        while calculate_score(dealer_cards) < 17:
            print("\nIt's dealer's turn.")
            time.sleep(1)
            dealer_cards.append(deal_card())
            print_table(player_cards, dealer_cards, False)
        
        dealer_score = calculate_score(dealer_cards)
        player_score = calculate_score(player_cards)
            
        if dealer_score > 21 or player_score > dealer_score:
            winner = "player"
        elif player_score < dealer_score:
            winner = "dealer"

    print_table(player_cards, dealer_cards, False)
    
    if winner == "":
        print("\nIt's a draw!")
    else:
        print(f"\n{winner.title()} wins.")
        if blackjack:
            print("Blackjack!")

new_game = True
while new_game:
    play_game()
    if input("\nDo you want to play again? (y/n) ").lower() != 'y':
        new_game = False