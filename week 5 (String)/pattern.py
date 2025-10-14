# WAP to print the following pattern
# A
# BB
# CCC
# DDDD    

n = 4
for i in range(n):
    for j in range(i+1):
        print(chr(65+i), end=" ")
    print()
