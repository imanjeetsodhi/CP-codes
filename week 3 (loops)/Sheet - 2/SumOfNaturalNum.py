# write a program to print sum of all natural numbers tili N

num = int(input("Enter a positive integer: "))
sum_of_natural_numbers = 0  
for i in range(1, num + 1):
    sum_of_natural_numbers += i
print("Sum of natural numbers from 1 to", num, "is:", sum_of_natural_numbers)