#WAP to find in how many subarrays element at index k is present
arr = [3,-2,4,-1,2,6] 
n = len(arr)
k = 3
count = 0

for i in range(n): 
    for j in range(i,n): 
        if i<=k<=j:
        # count =(k + 1) * (n - k)
            count += 1
print(count)