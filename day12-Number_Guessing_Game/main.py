import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!\n")
print("I'm thinking of a number between 1 and 100. guess\n")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()

def number_list():
    """
    The function "number_list" creates a list of numbers from 1 to 100.
    :return: a list of numbers from 1 to 100.
    """
    numbers = []
    for num in range(1, 101):
        numbers.append(num)
    return numbers

def attempt_count():
    """
    The function "attempt_count" returns the number of attempts based on the difficulty level.
    :return: The number of attempts based on the difficulty level.
    """
    attempt = 0
    if difficulty == 'easy':
        attempt = 10
    else:
        attempt = 5
    return attempt

def random_number_pick():
    """
    The function "random_number_pick" returns a randomly chosen number from a list called "numbers".
    :return: a randomly chosen number from the "numbers" list.
    """
    pick = random.choice(numbers)
    return pick

numbers = number_list()
count = attempt_count()
chosen_number = random_number_pick()

game_finished = False

for attempt in range(count):
    while count != 0 and not game_finished:
        print(f"You have {count} attempts remaining to guess the number.\n")
        guess = int(input("Make a guess: "))
        if guess > chosen_number:
            print("Too High")
            print("Guess again.")
        elif guess < chosen_number:
            print("Too Low")
            print("Guess again.")
        elif guess == chosen_number:
            game_finished = True
            print(f"You got it! the answer is {chosen_number}. You win!\n")
        if guess != chosen_number:
            count -= 1
        if count == 0:
            game_finished = True
            print("You have no attempts left. You lose\n")
