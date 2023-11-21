import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
print('''
                ROCK PAPER SCISSORS
      ''')
inp = int(input("(Choose 0 for Rock, 1 for Paper, 2 for Scissors)  "))

rps_int = [0, 1, 2]
rps = [rock, paper, scissors]
rps_word = ["Rock", "Paper", "Scissors"]

player_rps = rps[inp]
player_rps_word = rps_word[inp]
print(player_rps)
print(f"You choose: {player_rps_word}")

comp_rand_int = random.choice(rps_int)
comp_rps = rps[comp_rand_int]
comp_rps_word = rps_word[comp_rand_int]
print(comp_rps)
print(f"computer choose: {comp_rps_word}\n")

if inp == 0 and comp_rand_int == 2:
    print("You Win!\n")
elif inp == 2 and comp_rand_int == 1:
    print("You Win!\n")   
elif inp == 1 and comp_rand_int == 0:
    print("You Win!\n")  
elif comp_rand_int == 0 and inp == 2:
    print("You lose\n")
elif comp_rand_int == 2 and inp == 1:
    print("You lose\n")   
elif comp_rand_int == 1 and inp == 0:
    print("You lose\n")
else:
    print("Draw\n")

