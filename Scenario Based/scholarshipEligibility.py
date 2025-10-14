# In a college n student applied for schlorship, the elegibility criteria is:
# 1. The student should have greater than or equal to 75% marks 
# 2. The student should have attendanvce greater than or equal to 80%

num = int(input())
student = []
for i in range(num):
    m = int(input("Enter marks: "))
    a = int(input("Enter attendance: "))
    student.append((m, a))

eligible = 0
for m, a in student:
    if m >= 75 and a >=80:
        eligible += 1

print(elegible)


