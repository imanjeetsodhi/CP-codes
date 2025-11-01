#given an array of integer a. if subarray of an array is said to be good, if it fullfills any one of the criteria:
# length of subarray is even, sum of all elements of the subarray must be less than b
# length of subarray is odd, sum of all elements of the subarray must be greater than b
# find the count of good subarray

arr = [1,2,3,4,5,6]
b = 15
n = len(arr)
count = 0
for i in range(n):
    sum = 0
    for j in range(i,n):
        sum = 0
        length = j - i + 1
        if(length%2 == 0 and sum < b ) or (length%2!=0 and sum > b):
            count += 1
print (count)

# given an integer array c of size a now you need to find a subarray so that the sum of countenious element is maximum but the sum must not excide b 