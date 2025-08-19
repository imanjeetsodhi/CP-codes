# print the average of the three numbers 
a = int(input("enter the 1st number : "))
b = int(input("enter the 2nd number : "))
c = int(input("enter the 3rd number : "))

if(a<b and a<c):
    print(a," is the smallest number")
elif(b<a and b<c):
    print(b," is the smallest number")
else:
    print(c," is the smallest number")
