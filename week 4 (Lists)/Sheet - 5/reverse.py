# method 1
a=list(map(int,input().split()))
for i in range(len(a)):
    a[i],a[len(a)-i-1]=a[len(a)-i-1],a[i]
print(a)


# method 2
mylist = [1.4, 2, 3, 4, 5, "Suyash"]
mylist.reverse()
print(mylist)