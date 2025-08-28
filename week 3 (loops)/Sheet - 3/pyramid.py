# _ _ _ _ *        
# _ _ _ * *           
# _ _ * * *           
# _ * * * * 
# * * * * *  


num = int(input("enter the number: "))

for i in range(num):
    print("_ " * (num - i - 1), end="")
    print("* " * (i + 1))