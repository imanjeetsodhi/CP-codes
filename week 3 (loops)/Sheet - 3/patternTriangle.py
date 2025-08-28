# 1
# 1 * 
# 1 * 3
# 1 * 3 *
# 1 * 3 * 4

pattern = [1, "*", 3, "*", 4]

for i in range(1, len(pattern) + 1):
    print(*pattern[:i])