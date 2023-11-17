#write a program that adds the digit in a 2 digit number.
#e.g if the input was 35, then the output should be 3 + 5 = 8

num = input("Enter a two digit number ")

#subscripting the first an second int in num
first = (num[0])
second = (num[1])

sum = int(first) + int(second)

print(f"{first} + {second} = {sum}")
