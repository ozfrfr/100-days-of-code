"""
program to calculate pizza order
"""

print("Welcome to Python Pizza Deliveries")
size = input("What size of pizza do you want? (S, M, L) ")
add_pepperoni = input("Do you want pepperoni? (Y or N) ")
extra_cheese = input("Do you want extra cheese? (Y or N) ")

size = size.upper()
add_pepperoni = add_pepperoni.upper()
extra_cheese = extra_cheese.upper()

bill = 0

if size == "S":
    bill = 15
    if add_pepperoni == "Y":
        bill +=2
        if extra_cheese == "Y":
            bill +=1
elif size == "M":
    bill = 20
    if add_pepperoni == "Y":
        bill +=3
        if extra_cheese == "Y":
            bill +=1
elif size == "L":
    bill = 25
    if add_pepperoni == "Y":
        bill +=3
        if extra_cheese == "Y":
            bill +=1
else:
    print("Order Error  - You entered an invalid response")

print(f"Your final bill is: ${bill}.")
