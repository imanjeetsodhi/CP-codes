# program that take input N and prints all natural numbers from N to 1

num = int(input("Enter a positive integer: "))
for i in range(num, 0, -1):
    print(i, end=' ')