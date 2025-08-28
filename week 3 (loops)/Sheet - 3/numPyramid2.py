# 1 
# 2 3 
# 4 5 6 
# 7 8 9 10 

num = 5
count = 1
for i in range(num+1):
    for j in range(i):
        print(count, end=" ")
        count+=1
    print()