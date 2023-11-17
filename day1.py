#function to print the number of chars in a string
print(len(input("what is your name? ")))
#or
name = input("what is your name? ")
len = len(name)

print(f"there are {len} chars in {name}")

#write a function to generate a band name using your city and pet name
print("function to generate a band name")
city = input("what city where you born? ")
pet = input("what is your pet's name? ")

#using concatenation to print the string 
print("your band name is " + city + " " + pet )
