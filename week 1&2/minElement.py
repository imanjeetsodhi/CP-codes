# Write a program to input three numbers(A, B & C) from the user and print the minimum element among A, B & C.
a = int(input("Enter the 1st number: "))
b = int(input("Enter the 2nd number: "))
c = int(input("Enter the 3rd number: "))    
if a < b and a < c:
    print(a, "is the smallest number")
elif b < a and b < c:
    print(b, "is the smallest number")
else:
    print(c, "is the smallest number")