# a company stores n employee IDs in a list. HR wants to print only those Ids that are even number (science odd IDs are temporary employees). print all even employee IDs seprated by space if none, print -1

# n = int(input())
# employee = []
# for i in range(n):
#     id = int(input())
#     employee.append(id)

employee = [101, 103, 103, 107, 105]

even_ids = []
for id in employee:
    if id % 2 == 0:
        even_ids.append(id)

if len(even_ids) == 0:
    print(-1)
else:
    print(even_ids)



