# take input of an array from user and compute the sum of all elements in the array
# array = [1,2,3,4,5,6,7,8,9]
# esum = 0
# for i in array:
#     esum = esum + i
# print("the sum of the array is: ", esum)


# n = int(input("enter the number of elements:  "))
# arr = []
# for i in range(n):
#     element = int(input("enter the element: "))
#     arr.append(element)
# print("the array is: ", arr)
# sum = 0
# for i in arr:
#     sum = sum + i
# print("the sum of the array is: ", sum)


# given an array find the maximum element in the array
# arr = list(map(int, input().split()))
# max = arr[0]
# for i in arr:
#     if i > max:
#         max = i
# print("the max num in the array is: ", max)

# given an array and a target, find number of accurence of target number in the array
arr = list(map(int, input("enter the number: ").split()))
target = int(input("enter the target number: "))
count = 0
for i in arr:
    if i == target:
        count += 1
print("the accurence of the target number is: ", count)