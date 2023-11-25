
'''
Grading program exercise
'''
# The code is creating a dictionary called `student_scores` that contains the scores of different
# students. It then creates an empty dictionary called `student_grades`.
student_scores ={
    "Harry": 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}
student_grades = {}
# The code is iterating over each key in the `student_scores` dictionary. For each key, it checks the
# corresponding value (student score) and assigns a grade to that student based on their score.
for i in student_scores:
    if student_scores[i] > 90:
        student_grades[i] = "outstanding"
    elif student_scores[i] > 80:
        student_grades[i] = "exceeds expectations"
    elif student_scores[i] > 70:
        student_grades[i] = "acceptable"
    elif student_scores[i] < 70:
        student_grades[i] = "fail"

print(student_grades)