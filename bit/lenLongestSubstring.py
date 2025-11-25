# given a string calculate the length of longest palindromic substring

s = "luvass"
n = len(s)
max_len = 1 

for i in range(n):
    for j in range(i, n):
        sub = s[i:j+1]
        if sub == sub[::-1]:
            if len(sub) > max_len:
                max_len = len(sub)
print(max_len)
