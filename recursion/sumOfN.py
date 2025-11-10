#sum of n natural numbers 
n = 5
sum = 0
for i in range(0,n+1):
    sum+=i

print(sum)

# using recursion
def sum(n):
    if n <= 0:
        return 0
    return n + sum(n - 1)

print(sum(n))