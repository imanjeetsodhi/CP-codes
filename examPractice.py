#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 

# n = 5
# for i in range(n+1):
#     for j in range(i):
#         print(" ", end=" ")
#     for k in range(i, n):
#         print("*", end=" ")
#     for l in range(i, n-1):
#         print("*", end=" ")
#     print()

# -------------------------------------------------------------------
# Exam Result Analyzer

# n = int(input())
# result = list(map(int, input().split()))
# passcount = 0
# failcount = 0
# for i in range(n):
#     if result[i] >= 35:
#         passcount += 1
#     else:
#         failcount += 1

    
# print(passcount, failcount)

# -------------------------------------------------------------------
# Employee ID Filter

# n = int(input())
# emp_ids = list(map(int, input().split()))
# id = []

# for i in range(n):
#     if emp_ids[i] % 2 == 0:
#         id.append(emp_ids[i])

# if len(id) == 0:
#     print(-1)
# else:
#     print(*id)

# -------------------------------------------------------------------
# The Product Sales Report

# n = int(input())
# arr = list(map(int, input().split()))
# highest = arr[0]
# lowest = arr[0]

# for i in range(n):
#     if arr[i] > highest:
#         highest = arr[i]
#     if arr[i] < lowest:
#         lowest = arr[i]

# print(highest, lowest)

# -------------------------------------------------------------------
# The Scholarship Eligibility 








# -------------------------------------------------------------------
# LIST

# sum of all elements in the list
# arr = list(map(int, input().split()))
# sum = 0

# for i in range(len(arr)):
#     sum = sum + arr[i]
# print(sum)


# add a number to each element in the list
# arr = list(map(int, input().split()))
# num = int(input())
# copyArr = []

# for i in range(len(arr)):
#     copyArr.append(arr[i]+num)

# print(*copyArr)


# find the maximum and minimum element in the list
# arr = list(map(int, input().split()))
# max = arr[0]
# min = arr[0]
# for i in range(len(arr)):
#     if arr[i] > max:
#         max = arr[i]
#     if arr[i] < min:
#         min = arr[i]
# print(max, min)

# find the index of a given number in the list
# arr = list(map(int, input().split()))
# n = int(input())

# for i in range(len(arr)):
#     if arr[i] == n:
#         print(i)
#         break

# print all the negative numbers in the list
# arr = list(map(int, input().split()))
# for i in range(len(arr)):
#     if arr[i] < 0:
#         print(arr[i])
    
# count the number of even and odd numbers in the list
# arr = list(map(int, input().split()))
# even = 0
# odd = 0
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         even += 1
#     else:
#         odd += 1
# print(even-odd)

# separate the even and odd numbers into two different lists
# arr = list(map(int, input().split()))
# even = []
# odd = []
# for i in range(len(arr)):
#     if arr[i] % 2 == 0:
#         even.append(arr[i])
#     else:
#         odd.append(arr[i])
# print(*even)
# print(*odd)

# create a new list with the square of each element in the original list
# arr = list(map(int, input().split()))
# sarr = []
# for i in range(len(arr)):
#     sarr.append(arr[i]**2)

# print(*sarr)

# create a new list with the cube of each element in the original list
# arr = list(map(int, input().split()))
# sarr = []
# for i in range(len(arr)):
#     sarr.append(arr[i]**3)

# print(*sarr)

# reverse the list
# arr = list(map(int, input().split()))
# rarr = reversed(arr)
# print(*rarr)

# arr = list(map(int, input().split()))
# arr2 = list(map(int, input().split()))

# for i in range(len(arr)):
#     if arr[i] not in arr2:
#         arr2.append(arr[i])

# print(*arr2.sort())



# n = 1589
# sum = 0

# while n>0:
#     sum += n % 10
#     n //= 10

# print(sum)


# a = 131
# org = a
# rev = 0

# while a>0:
#     digit = a%10
#     rev = rev * 10 + digit
#     a //= 10

# if org == rev:
#     print('yes')
# else:
#     print('no')


arr = list(map(int, input().split()))
arr2 = list(map(int, input().split()))
arr3 = []

for i in range(len(arr)):
    arr3.append(arr[i]+arr2[i])

print(*arr3)


