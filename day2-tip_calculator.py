print("Welcome to the tip calculator!")
total_bill = float(input("what was the total bill? $"))
tip_percentage = int(input("what percentage tip would you ike to give? 10, 12, 15? "))
num_people = int(input("how many people to split the bill? "))

tip_amount = total_bill * (tip_percentage / 100)
total_amount = total_bill + tip_amount 
each_person_pay = total_amount / num_people

print(f"Each person should pay: ${each_person_pay:.2f}")







