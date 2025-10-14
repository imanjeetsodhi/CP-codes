# WAP to reverse th eorder of the words in a given string

s = "Hello Python"
words = s.split()
rev_words = " ".join(reversed(words))
print(rev_words)

# WAP to reverse each word in a given string 
s = "Hello Python"
words = s.split()
rev_word = [word[::-1] for word in words]
rev_string = " ".join(rev_word)
print(rev_string)