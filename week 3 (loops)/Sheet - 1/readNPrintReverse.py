# Read N, Print Reverse of N.

num = int(input("Enter an integer: "))
reverse_num = 0
while num > 0:
    reverse_num = reverse_num * 10 + num % 10 
    num //=10 
print("Reverse of the number:", reverse_num)