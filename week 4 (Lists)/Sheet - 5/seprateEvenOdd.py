a=list(map(int,input().split()))
b=[]
c=[]
for i in a:
    if(i%2!=0):
        print(i,end=" ")
print()
for i in a:
    if(i%2==0):
        print(i,end=" ")


