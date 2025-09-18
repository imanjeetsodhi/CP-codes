n=int(input())
a=[]
for i in range(n):
    num=int(input())
    a.append(num)
print(a)
for i in a:
    if(i<0):
        print(i)
        