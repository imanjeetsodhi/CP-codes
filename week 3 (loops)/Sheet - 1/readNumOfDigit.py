#Read N, Print no. of digits in N

num = int(input("Enter a integer: "))
count = 0

while num > 0:
    num //= 10; count += 1
print("Number of digits:", count)
