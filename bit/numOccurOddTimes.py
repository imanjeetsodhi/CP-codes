# given an array of n integers where all numbers occurs an even numbers of time except a number which occurs odd number of time find that mumber
# input format
#first line of the input contains integer n denoting the size of the array
#second line contains n space separated integers denoting the elements of the array

arr = [2,3,4,3,2,4,4]
n = len(arr)
unique = 0
for i in arr:
    unique ^= i
print(unique)



