# write a program that take input N and prints all even numbers from 1 to N

num = int(input("Enter a positive integer: "))
for i in range(2, num + 1, 2):
    print(i, end=' ')
    