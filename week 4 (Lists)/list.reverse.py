
# we can also use [::-1] but it is slicing and it makes the copy in background.


# we can reverse the list element by using this 

list = [10, 20, 30, 40, 'manjeet']
print(list)

list.reverse()
print(list)


# by using reversed() it returns the reversed ittrator without modifing the orignal one 
list = [1, 2, 3, 4, 5]
print(list)

newList = list.__reversed__()
print(newList)