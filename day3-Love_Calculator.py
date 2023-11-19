"""
Program to calculate love between two people
"""
print("Warm welcome to the love calculator")
name1 = input("What is your name? ")
name2 = input("Enter their name? ")

combined_names = name1 + name2
combined_lower = combined_names.lower()

t = combined_lower.count("t")
r = combined_lower.count("r")
u = combined_lower.count("u")
e = combined_lower.count("e")

l = combined_lower.count("l")
o = combined_lower.count("o")
v = combined_lower.count("v")
e = combined_lower.count("e")

true_sum = t + r + u + e
love_sum = l + o + v + e

true_str = str(true_sum)
love_str = str(love_sum)

score_str = true_str + love_str
score_int = int(score_str)

if score_int < 10 or score_int > 90:
    print(f"Your score is {score_str}, you go together like coke and mentos.")
elif score_int >= 40 and score_int <= 50:
    print(f"Your score is {score_str}, you are alright together.")
else:
    print(f"Your score is {score_str}.")