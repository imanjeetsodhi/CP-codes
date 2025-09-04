
# reversing a list by using for loop
list = [1, 2, 3, 4, 5]

for i in range(len(list)//2):
    temp = list[i]
    list[i] = list[len(list) - 1 - i]
    list[len(list) - 1 - i] = temp
print(list)