# *        *
# **      **
# ***    ***
# ****  ****
# **********

rows = 5
width = rows * 2

for i in range(1, rows + 1):
    stars = '*' * i
    spaces = ' ' * (width - 2 * i)
    print(stars + "       " +stars)