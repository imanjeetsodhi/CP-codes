# find number of occurance of verb of string a consisting of lower case english alphabets
a = 'abobc'
b = 'bob'
count = 0
for i in range(len(a)-len(b)+1):
    if a[i:i+len(b)] == b:
        count += 1
print(count)

