'''
Program to calculate the average height from a list of heights
'''
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
print(student_heights)

total_height = 0
for n in student_heights:
    total_height += n

number_of_heights = 0
for n in student_heights:
    number_of_heights += 1

student_height = total_height / number_of_heights

print(f"The average height is {round(student_height)}")

