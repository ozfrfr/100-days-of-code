import random

print('''
program to randomly choose who would pay the bill today.
''')
# capture inputted names
inp = input("what are you\'re names? (separate each name with a comma)  ")
print("\n")
# convert the input into list by separating ot the commas using str.split(",")
names = inp.split(",")
# access the number of names in names variable
num = len(names)
# used random module to generate random pick from num list. -1 is to capture the beginning and ending index of num list.
random_pick = random.randint(0, num - 1)
# used the number gotten from random_pick to check for the index of the number in names list
pick = names[random_pick]
# prints who pays by concatenating pick with a message
print(pick + " is going to pay the bill today.\n")

#or
# using random.choice()
# pick = random.choice(names)
# print(pick + " is going to pay the bill today.\n")