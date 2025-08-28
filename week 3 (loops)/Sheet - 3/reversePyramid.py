# * * * * *          
# _ * * * *        
# _ _ * * *         
# _ _ _ * *        
# _ _ _ _ * 

num = 5

for i in range(num):
    print("_ " * i, end="")
    print("* " * (num - i))