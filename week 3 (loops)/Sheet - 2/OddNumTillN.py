# write a program that take input N and prints all odd numbers from 1 to N

num = int(input("Enter a positive integer: "))
for i in range(1, num + 1, 2):
    print(i, end=' ') 