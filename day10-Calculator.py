'''
Calculator program
'''
#Add
def add(n1, n2):
    return n1 + n2
#Subtract
def subtract(n1, n2):
    return n1 - n2
#Multiply
def multiply(n1, n2):
    return n1 * n2
#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

num1 = int(input("What's the first number? "))

for symbol in operations:
    print(symbol)

operation_symbol = input("Pick an operation from the line above: ")

first_num = num1

should_continue = True

while should_continue:
    next_num = int(input("What's the next number? ")) 
    calculation_function = operations[operation_symbol]
    answer = calculation_function(first_num, next_num)
    print(f"{first_num} {operation_symbol} {next_num} = {answer}")
    first_num = answer
    continue_or_exit = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to exit.: ").lower()
    if continue_or_exit == 'n':
        should_continue = False
    if continue_or_exit == 'y':
        operation_symbol = input("Pick another operation: ")


