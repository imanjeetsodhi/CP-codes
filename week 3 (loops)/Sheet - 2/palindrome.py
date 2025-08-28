# write a program to check if the reverse of number is equal to the number or not 

num = int(input("enter the number : "))
original_num = num
reverse = 0

while num > 0:
    digit = num % 10
    reverse = reverse * 10 + digit
    num //= 10

if original_num == reverse:
    print("Palindrome")
else:
    print("Not Palindrome")
