#given an array of n non negative numbers and a non negative number b find the number of sunbarray a with a sum less than b
arr = [1,11,2,3,15]
b = 10
n = len(arr)
count = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum += arr[j]
        if sum < b:
            count += 1
        else:
            break
print(count)