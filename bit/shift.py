#using right shift operator 
num = 18  # binary: 10010
count = 0
while num > 0:
    if (num & 1) == 1:
        count += 1
    num = num >> 1
print(count)
