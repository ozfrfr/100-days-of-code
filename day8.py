#Simple Function
def greet():
    print("Hello")
    print("How do you do?")
    print("Isn't the weather nice today?")

#Function that allows for input   
greet()
def greet_with_name(name):
    print(f"Hello {name}")
    print(f"How do you do {name}?")

greet_with_name("Billie")

#parameter = name of data
#argument = value of data

#Functions with more than one input
def greet_with(name, location):
    print(f"hello {name}")
    print(f"what is it like in {location}")
    
greet_with("Billie", "Nowhere")

#Function with keyword argument
greet_with(location = "Nowhere", name = "Billie")
