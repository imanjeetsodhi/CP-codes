n=int(input())
a=[]

for i in range(n):
    num=int(input())
    a.append(num)
print(a)
m=a[0]
n=a[0]
for j in a:
    if(m<j):
        m=j
    if(n>j):
        m=j
print(m,n)