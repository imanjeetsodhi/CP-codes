
num = int(input("Enter a positive integer: "))
sum_of_odd_numbers = 0
for i in range(1, num + 1):
    if i % 2 != 0:
        sum_of_odd_numbers += i
print("Sum of odd numbers from 1 to", num, "is:", sum_of_odd_numbers)