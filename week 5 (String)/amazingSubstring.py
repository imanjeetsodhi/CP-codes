# given a string s and you have to find all the amazing substrings in it. an amazing substring is one which starts with a vowel (a,e,i,o,u) 
# a input ABEC output 6 (AB, ABE, ABEC, E, EC, C)
s = "ABEC"
vowel = "AEIOU"
count = 0
for i in range(len(s)):
    if s[i] in vowel:
        count += (len(s)-i)

print(count)

def maxSubArraySum(arr, size, limit):
    max_sum = 0        # stores maximum valid sum found
    curr_sum = 0       # tracks current window sum
    start = 0          # window start index
    
    for end in range(size):
        curr_sum += arr[end]  # expand window
        
        # Shrink window if sum exceeds limit
        while curr_sum > limit and start <= end:
            curr_sum -= arr[start]
            start += 1
            
        max_sum = max(max_sum, curr_sum)
    
    return max_sum

# Test the function
arr = [2, 1, 3, 4, 5]  # input array
n = len(arr)           # size of array
b = 10                 # maximum sum limit

result = maxSubArraySum(arr, n, b)
print(f"Maximum subarray sum not exceeding {b}: {result}")