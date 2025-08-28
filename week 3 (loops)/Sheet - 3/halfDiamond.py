# * 
# ** 
# *** 
# **** 
# ***** 
# **** 
# *** 
# ** 
# * 

num = int(input("enter the number: "))

for i in range(num+1):
    for j in range(i):
        print("*", end=" ")
    print()

for i in range(num - 1, 0, -1):
    for j in range(1, i+1):
        print("*", end=" ")
    print()