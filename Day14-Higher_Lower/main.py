import os
import random
from art import logo
from art import vs
from game_data import data


def compare_a_message():
    name_a = a['name']
    description_a = a['description']
    country_a = a['country']
    return f"Compare A: {name_a}, a {description_a}, from {country_a}"

def compare_b_message():
    name_b = b['name']
    description_b = b['description']
    country_b = b['country']
    return f"Compare B: {name_b}, a {description_b}, from {country_b}"

def highest():
    max_followers = max(followers_a_count, followers_b_count)
    return max_followers


score = 0
game_end = False

while not game_end:
    a = random.choice(data)
    followers_a_count = a['follower_count']
    b = random.choice(data)
    followers_b_count = b['follower_count']

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}")

    print(compare_a_message())
    print(vs)
    print(compare_b_message())

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == "a":
        user_choice = followers_a_count
    elif user_input == "b":
        user_choice = followers_b_count

    if user_choice == highest():
        score += 1
        game_end = False
        os.system('clear')
    else:
        os.system('clear')
        print(logo)
        print(f"Sorry thats wrong. Final score: {score}")
        game_end = True
