# Write a program to input two numbers(A & B) from the user and print the maximum element among A & B. 
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
if a > b:
    print("The maximum element is:", a)
elif b > a:
    print("The maximum element is:", b)
else:
    print("Both numbers are equal:", a)