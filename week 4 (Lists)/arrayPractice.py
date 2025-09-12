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
# arr = list(map(int, input("enter the number: ").split()))
# target = int(input("enter the target number: "))
# count = 0
# for i in arr:
#     if i == target:
#         count += 1
# print("the accurence of the target number is: ", count)

# given an array and an increament number, genrate a new array which contains all values of orignal array inreased by the increament number
# arr = list(map(int, input("enter the number: ").split()))
# increament = int(input("enter the increament number: "))
# newarr = []
# for i in arr:
#     newarr.append(i+increament)
# print("the number after incraement is: ", newarr)/

# given an array, genrate an array with square of each element in the array
# arr = list(map(int, input("enter the number: ").split()))
# newarr = []
# for i in arr:
#     newarr.append(i**2)
# print("the square of each element in the array is: ", newarr)

# given an array filter all the odd numbers and print them in a new array
# arr = list(map(int, input("enter the number: ").split()))
# newarr = []
# for i in arr:
#     if i%2 != 0:
#         newarr.append(i)
# print("the odd numbers in the array are: ", newarr)

# Given a list and a target no. find and print the index of the target in the list
# list = list(map(int, input("enter the list elements: ").split()))
# target = int(input("enter the target number: "))
# for i in range(len(list)):
#     if list[i] == target :
#         index = i
# print("index of the target number is: ", index)


# adding two list element wise and storing the result in a new list
list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8]
result = []
for i in range(len(list2)):
    result.append(list1[i] + list2[i])
print("the sum of two list is: ", result)