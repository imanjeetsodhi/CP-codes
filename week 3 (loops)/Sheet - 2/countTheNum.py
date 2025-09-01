num = int(input("enter the number: "))
digit = int(input("enter the digit: "))
count = 0

while(num>0):
    last_digit = num%10
    if (last_digit == digit):
        count+=1
    num //=10
print(count)