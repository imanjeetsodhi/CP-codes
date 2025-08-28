# *_ _ _ _ _*        
# *_ _ _ _*           
# *_ _ _*               
# *_ _*    
# *_*       


num = 5  # Number of rows

for i in range(num):
    print("*", end="")
    for j in range(num - i - 1):
        print("_ ", end=" ")
    print("*")