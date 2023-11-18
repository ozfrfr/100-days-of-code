"""
Program that interprets the body mass index (BMI)
based on a user's weight and height 
and tells them the interpretation of their BMI based on the BMI value.
"""

height = input("what is your height in metres? ")
weight = input("what is your weight in kg? ")

BMI = int(weight) / (float(height) ** 2)

BMI_as_int = int(BMI)

if BMI_as_int < 18.5:
    print(f"Your BMI is {BMI_as_int}, you are Underweight")
elif BMI_as_int < 25:
    print(f"Your BMI is {BMI_as_int}, you have a Normal Weight")
elif BMI_as_int < 30:
    print(f"Your BMI is {BMI_as_int}, you are Overweight")
elif BMI_as_int < 35:
    print(f"Your BMI is {BMI_as_int}, you are Obese")
else:
    print(f"Your BMI is {BMI_as_int}, you are Clinically Obese")
