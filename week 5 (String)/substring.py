# funtion to print substring of a string
def substring(s):
    n = len(arr)
    for i in range(n):
        for j in range(i,n):
            print(arr[i:j+1])   

#WAP to print total number of subarray in an array of size n
arr = [10,20,30,40,50]
n = len(arr)
subarray = n*(n+1)//2
print(subarray)
 

# WAP to print all the value of subarray
substring(arr)
    
