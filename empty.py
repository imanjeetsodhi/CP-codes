# # print the square using for loop 
# a = int(input("enter the number : "))
# b = int(input("enter the number : "))

# result = 1
# for i in range(b):
#     result = result * a
# print(result)


# # -------------------------------------------------------------------
# # print n number of star
# n = 5

# for i in range(0,n):
#     print("*", end=" ")


# # -------------------------------------------------------------------
#print grid pattern with star
# n = int(input("enter the number: "))
# m = int(input("enter the numebr: "))
# for i in range(n):
#     for j in range(m):
#         print("*", end=" ")
#     print()


# # -------------------------------------------------------------------
# # a pyramid 
# rows = int(input("enter the number of rows: "))
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# #reverse 
# rows = int(input("enter the nunmber of rows: "))
# for i in range(rows, 0, -1):
#     for j in range(i):
#         print("*", end=" ")
#     print()



# # -------------------------------------------------------------------
# # write a program to print
# # 1
# # 1 * 
# # 1 * 3
# # 1 * 3 *
# # 1 * 3 * 4

# pattern = [1, '*', 3, '*', 4]
# for i in range(1, len(pattern) + 1):
#     print(*pattern[:i])


# # ------------------------------------------------------------------
# # Hollow Pyramid Pattern
# # **********
# # ****  ****
# # ***    ***
# # **      **
# # *        * 

# rows = 5
# for i in range(rows):
#     left_stars = rows - i
#     spaces = i * 2
#     print('*' * left_stars + ' ' * spaces + '*' * left_stars)

# rows = 5
# width = rows * 2

# for i in range(rows):
#     for j in range(width):
#         if j < rows - i or j >= rows +i:
#             print('*', end='')
#         else:
#             print(' ', end='')
#     print()


# # Reverse of Hollow Pyramid Pattern
# # *        *
# # **      **
# # ***    ***
# # ****  ****
# # **********

# rows = 5
# width = rows * 2

# for i in range(1, rows + 1):
#     stars = '*' * i
#     spaces = ' ' * (width - 2 * i)
#     print(stars + "       " +stars)


# num = 5

# for i in range(1, num+1):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*")
#     print()


#           * 
#         * * * 
#       * * * * * 
#     * * * * * * * 
#   * * * * * * * * * 
# n = 5
# for i in range(n):
#     for j in range(i,n):
#         print(" ", end=" ")
#     for j in range(i):
#         print("*", end=" ")
#     for j in range(i+1):
#         print("*", end=" ")
#     print()


#   * * * * * * * * * 
#     * * * * * * * 
#       * * * * * 
#         * * * 
#           * 
# n =5 
# for i in range(n):
#     for j in range(i+1):
#         print(" ", end=" ")
#     for j in range(i,n):
#         print("*", end=" ")
#     for j in range(i,n-1):
#         print("*", end=" ")
#     print()


