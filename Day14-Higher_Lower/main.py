import os
import random
from art import logo
from art import vs
from game_data import data


def compare_a_description():
    name_a = a['name']
    description_a = a['description']
    country_a = a['country']
    return f"Compare A: {name_a}, a {description_a}, from {country_a}"

def compare_b_description():
    name_b = b['name']
    description_b = b['description']
    country_b = b['country']
    return f"Compare B: {name_b}, a {description_b}, from {country_b}"

def highest():
    max_followers = max(followers_a_count, followers_b_count)
    return max_followers


score = 0
game_end = False
prev_b = None

while not game_end:
    os.system('clear') # or  os.system('cls') on Windows
    a = prev_b if prev_b else random.choice(data) 
    followers_a_count = a['follower_count']
    
    b = random.choice(data)
    followers_b_count = b['follower_count']

    print(logo)

    if score > 0:
        print(f"You're right! Current score: {score}")

    print(compare_a_description())
    print(vs)
    print(compare_b_description())

    user_input = input("Who has more followers? Type 'A' or 'B': ").lower()

    if user_input == "a":
        user_choice = followers_a_count
    elif user_input == "b":
        user_choice = followers_b_count

    if user_choice == highest():
        score += 1
        game_end = False
        prev_b = b # This is done so that in the next iteration of the while loop, the value of `b` from the current iteration can be used as the value of `a` in the next iteration. 
        os.system('clear') # or os.system('cls') on Windows
    else:
        os.system('clear') # or or os.system('cls') on Windows 
        print(logo)
        print(f"Sorry thats wrong. Final score: {score}")
        game_end = True
