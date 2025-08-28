# **********
# ****  ****
# ***    ***
# **      **
# *        * 


# rows = 5
# for i in range(rows):
#     left_stars = rows - i
#     spaces = i * 2
#     print('*' * left_stars + ' ' * spaces + '*' * left_stars)

rows = 5
width = rows * 2

for i in range(rows):
    for j in range(width):
        if j < rows - i or j >= rows +i:
            print('*', end='')
        else:
            print(' ', end='')
    print()