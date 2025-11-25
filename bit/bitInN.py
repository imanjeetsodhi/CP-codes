# given an integer n count how many set bit are there in n.
n = 10
count = 0

while n>0:
    if (n & 1) == 1:
        count += 1
    n = n >> 1

print(count)

# function 
def count_set_bits(n):
   count = 0
   while n>0:
    if (n & 1) == 1:
        count += 1
    n = n >> 1

    return count
   
print(count_set_bits(10))
   
