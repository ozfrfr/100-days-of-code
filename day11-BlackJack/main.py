############### Blackjack Project #####################


############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

import os
from random import choice
from art import logo

def deal_card():
    """
    The function "deal_card" deals a random card from a deck.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_pick = choice(cards)
    return random_pick


def calculate_score(list):
    """
    The function calculates the score based on a given list.
    """
    if 10 in list and 11 in list and len(list) == 2:
        return 0
    elif 11 in list and sum(list) > 21:
        list.remove(11)
        list.append(1)
    
    return sum(list)

def compare(user_score, computer_score):
    """
    The function compares the scores of the user and the computer in a game and returns a message
    indicating the outcome of the game.
    """
    if user_score == computer_score:
        return "    Its a Draw 🙃"
    elif computer_score == 0:
        return "    You lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "    You Win with a Blackjack 😎"
    elif user_score > 21:
        return "    You went over. You lose 😭"
    elif computer_score > 21:
        return "    Opponent went over. You Win 😄"
    elif user_score > computer_score:
        return "    You Win 😃"
    else:
        return "   You lose 😤"

def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    is_game_over = False
    # The line `for count in range(2):` is a loop that iterates twice. It is used to deal two cards to
    # both the user and the computer at the beginning of the game.
    for count in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    # The line `while is_game_over == False:` is a while loop that continues to execute the code block
    # as long as the condition `is_game_over == False` is true. In other words, it keeps looping until
    # the variable `is_game_over` becomes `True`.
    while is_game_over == False:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)

        print(f"    Your cards: {user_cards}, current score: {user_score}")
        print(f"    Computer's first cards: {computer_cards[0]}\n")

        # The line `if user_score == 0 or computer_score == 0 or user_score > 21:` is checking if any
        # of the following conditions are true:
        # - If the user's score is 0 (indicating a Blackjack)
        # - If the computer's score is 0 (indicating a Blackjack)
        # - If the user's score is greater than 21 (indicating a bust)
        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            user_should_deal = input("Type 'y' to get another card, type 'n' to pass: \n").lower()
            if user_should_deal == 'y':
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # The line `while computer_score != 0 and computer_score < 17:` is a while loop that continues to
    # execute the code block as long as the condition `computer_score != 0 and computer_score < 17` is
    # true. In other words, it keeps looping until the computer's score is either 0 (indicating a
    # Blackjack) or greater than or equal to 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(compare(user_score, computer_score))
    print(f"    Computer's final hand: {computer_cards}, Computer final Score: {computer_score}\n")
    new_game = input("    Do you want to play another game of BlackJack. type 'y' to play or 'n' to end. ").lower()

    # The line `if new_game == 'y':` is checking if the user wants to play another game of Blackjack.
    # If the user enters 'y', the function `play_game()` is called again to start a new game. If the
    # user enters any other input, the variable `is_game_over` is set to True, indicating that the
    # game is over and the program will exit.
    if new_game == 'y':
        os.system("clear")
        play_game()
    else:
        is_game_over = True
        os.system("clear")

play_game()


