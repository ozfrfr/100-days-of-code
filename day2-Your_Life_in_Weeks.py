# Write a function that calculates the number of days, weeks , and months left,
# with 90 years being the total number of years given
# the output format should be "you have x days, y weeks, and z months left"
# where x, y, z are replaced with the actual calculated number.

age = input("what is your current age? ")

days_in_year = 365
months_in_year = 12
weeks_in_year = 52
life_total = 90

days_left = (days_in_year) * (life_total) - (days_in_year) * int(age)
weeks_left = (weeks_in_year) * (life_total) - (weeks_in_year) * int(age)
months_left = (months_in_year) * (life_total) - (months_in_year) * int(age)

print(f"You have {days_left} days, {weeks_left} weeks, and {months_left} months left")

#or

age = input("what is your current age? ")

age_as_int = int(age)

years_left = 90 - age_as_int
days_left = years_left * 365
weeks_left = years_left * 52
months_left = years_left * 12

message = f"you have {days_left} days, {weeks_left} weeks, and {months_left} months left"

print(message)