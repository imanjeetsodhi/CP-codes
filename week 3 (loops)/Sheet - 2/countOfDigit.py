# take a input num and count the digit in the number num

num = int(input("Enter a positive integer: "))
count_of_digits = 0
while num > 0:
    num //= 10
    count_of_digits += 1    
print("Count of digits in the number is:", count_of_digits)