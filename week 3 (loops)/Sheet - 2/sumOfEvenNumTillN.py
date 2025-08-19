num = int(input("enter the number : "))
sum_of_even_numbers = 0
for i in range(2, num+1):
    if i%2 ==0:
        sum_of_even_numbers += i
print("Sum of even numbers from 1 to", num, "is:", sum_of_even_numbers)