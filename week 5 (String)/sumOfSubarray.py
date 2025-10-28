#WAP to print sum of every singlesubarray in an array
arr = [10,20,30]
print("array is: ", arr )
print("The sum of every subarray is: ")
n = len(arr)
for i in range(n):
    for j in range(i,n):
        print(sum(arr[i:j+1]))


#find the subarray with the largest sum and return its subarray
print("The largest sum is: ")
max_sum = 0
for i in range(n):
    for j in range(i,n):
        current_sum = sum(arr[i:j+1])
        max_sum = max(max_sum,current_sum) 

print(max_sum) 

#WAP to print sum of all the subarrays in an array
total_sum = 0
for i in range(n):
    for j in range(i,n):
        total_sum += sum(arr[i:j+1])
print("total sum is: ", total_sum)

# if we know in how many subarrays an element is present then we can directly calculate the sum of all subarrays













