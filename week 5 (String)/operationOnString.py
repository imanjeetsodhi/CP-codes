# concatinate the string with itself, Delete all the upper case letters, replace each vowels with #, 
# given a string a of size n consisting of lower case and upper case english alphabets. You have to perform the following operations on the string:

A = "aeiOUz"
vowels = "aeiou"
A = A + A 
A = ''.join([ch for ch in A if ch.islower()])
A = ''.join(['#' if ch in vowels else ch for ch in A])
print(A)
