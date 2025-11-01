# given an integer array c of size a now you need to find a subarray so that the sum of countenious element is maximum but the sum must not excide b 

arr = [2,1,3,4,5]
n = len(arr)
b = 12
max_sum = 0
curr_sum = 0
start = 0

for i in range(n):
    curr_sum += arr[i]
    while curr_sum > b and start <= i:
        curr_sum -= arr[i]
        start += 1

    max_sum = max(max_sum, curr_sum)

print(max_sum)


def maxSubArraySum(arr, n):
    max_sum = arr[0]    # stores overall maximum sum
    curr_sum = arr[0]   # stores current window sum
    
    for i in range(1, n):
        # Either extend previous subarray or start new subarray
        curr_sum = max(arr[i], curr_sum + arr[i])
        # Update maximum sum if current sum is larger
        max_sum = max(max_sum, curr_sum)
        
    return max_sum

# Test array
arr = [2, 1, 3, 4, 5] 
n = len(arr)

result = maxSubArraySum(arr, n)
print(f"Maximum subarray sum: {result}")