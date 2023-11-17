#write a program that adds the digit in a 2 digit number.
#e.g if the input was 35, then the output should be 3 + 5 = 8

num = input("Enter a two digit number ")

#subscripting the first an second str in num
first = (num[0])
second = (num[1])

#changing type from str to int and adding them together
sum = int(first) + int(second)

print(f"{first} + {second} = {sum}")

#floor division
print(5 // 2) #result would be in type int instead of float 
# = 2

#rounding result
print(round(8 / 3, 2)) #rounding the result to 2 decimal place
# = 2.67

