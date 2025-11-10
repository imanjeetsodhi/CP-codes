# In a class of n student each student marks are storedd in a list. A student passes if their marks are greater than or equal to 35. 
# write a program to count the number of students who passed and failed the exam.
n = int(input())
mark = []
for i in range(n):
    marks = int(input())
    marks.append(mark)

pass_students = 0
fail_students = 0
for marks in marks:
    if marks >= 35:
        pass_students += 1
    else:
        fail_students += 1

print(pass_students, fail_students)