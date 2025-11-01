# given a string s and you have to find all the amazing substrings in it. an amazing substring is one which starts with a vowel (a,e,i,o,u) 
# a input ABEC output 6 (AB, ABE, ABEC, E, EC, C)
s = "ABEC"
vowel = "AEIOU"
count = 0
for i in range(len(s)):
    if s[i] in vowel:
        count += (len(s)-i)

print(count)

