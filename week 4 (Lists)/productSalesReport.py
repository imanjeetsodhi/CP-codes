# a store keeps a list of sales of n products. Each products hacs a sales count. The manager wants to print the highest selling product count and the lowest selling priduct count, print two integers max sales and min sales 

# n = int(input())
# sales = []
# for i in range(n):
#     count = int(input())
#     sales.append(count)

sales = [12, 34, 50, 20, 80, 45, 67]
max_sales = max(sales)
min_sales = min(sales)
print(max_sales, min_sales)
