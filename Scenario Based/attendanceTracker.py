#A teacher records attendance for n students, where 1 means present and 0 means absent. Write a program to count the number of consecutive absences (0) that lasted the longest. 
n = int(input())
attendance = list(map(int, input("Enter attendance:").split()))

max_absences = 0
current_absences = 0
for i in range(n):
    if attendance[i] == 0:
        current_absences += 1
        max_absences = max(max_absences, current_absences)
    else:
        current_absences = 0
print(max_absences)