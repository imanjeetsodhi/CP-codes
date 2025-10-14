# company maintains a list of project deadlines. Two projects are called perfect pair if the sum of their deadlines is exactly equal to a given target k. find how many such pairs exist in the list.
n = int(input())
deadlines =[]

deadline = map(int, input("Enter deadline:").split())

k = int(input("target sum:"))
pairs = 0

for i in range(n):
    for j in range(i + 1, n):
        if deadlines[i] + deadlines[j] == k:
            pairs += 1

print(pairs)