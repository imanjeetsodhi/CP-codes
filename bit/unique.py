# given an array elements, every elements is repeaes twice except 1, find the unique element in the array 

arr = [2,3,4,3,2]
# def find_unique(arr, n):
#     if n == 1:
#         return arr[0]
    
#     return arr[n-1] ^ find_unique(arr, n-1)

# n = len(arr)
# print(find_unique(arr, n))

# # using loop 
unique = 0
for i in arr:
    unique ^= i 
print(unique)
