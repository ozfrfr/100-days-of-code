#function to calculate BMI

height = input("what is your height in metres? ")
weight = input("what is your weight in kg? ")

#changing type of weight to int and height to float, 
# while using equation for calculating BMI and PEMDAS
BMI = int(weight) / (float(height) ** 2)

#converting the result of BMI from float to int so as to get a whole number
BMI_as_int = int(BMI)

print(f"your BMI is {BMI_as_int}") 
