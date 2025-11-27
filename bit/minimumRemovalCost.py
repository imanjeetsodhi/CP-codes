#given an array element at every step remove an array element, cost to remove element is equal to sum of array elements present in the array, find the minimum cost to remove all the  elements

# we have to delete the elements in decending order to get the minimum

def removalCost(arr):
    arr.sort(reverse=True)
    cost = 0
    
    while arr:
        cost += sum(arr) 
        arr.pop(0)             
    
    return cost

arr = [4, 2, 1]
print(removalCost(arr))