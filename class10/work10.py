# l = [[1,2,3],[0,8],[7,6,5,4]]
# i = 0
# while i < len(l):
#     sum = 0
#     j= 0
#     while j<len(l[i]):
#         sum += l[i][j]
#         j += 1
#     print(sum)
#     i += 1


#! taking matrix as input
# m = int(input())
# n = int(input())
# matrix = []
# i = 0
# while i < m:
#     row = []
#     j = 0
#     while j < n:
#         x = int(input())
#         row.append(x)
#         j += 1
#     i += 1
#     matrix.append(row)

# i = 0
# while i < m:
#     j = 0
#     while j < n:
#         print(matrix[i][j], end=" ")
#         j += 1
#     print()
#     i += 1

#! B2
# nums = list(map(int, input().split()))
# greatest = nums[0]
# lowest = nums[0]
# i = 0
# while i < len(nums):
#     if nums[i] > greatest:
#         greatest = nums[i]
#     if nums[i] < lowest:
#         lowest = nums[i]
#     i += 1
# print(greatest, lowest)


#! second max
# nums = list(map(int, input().split()))
# maximum = float("-inf")
# secmax = float("-inf")
# i = 0
# while i < len(nums):
#     if nums[i] > maximum:
#         secmax = maximum
#         maximum = nums[i]
#     elif nums[i] > secmax and nums[i] != maximum:
#         secmax = nums[i]
#     i += 1
# print(secmax)

#! B3
# n = int(input())
# nums = list(map(int, input().split()))
# sum = 0
# i = 0
# while i < n:
#     sum += nums[i]
#     i += 1
# avg = sum/n

# i = 0
# count = 0
# while i < n:
#     if nums[i] > avg:
#         count += 1
#     i += 1
# print(count)


#! B4
# r, c = map(int, input().split())
# i = 0
# matrix = []
# while i < r:
#     row = list(map(int, input().split()))
#     matrix.append(row)
#     i += 1

# i = 0
# while i < r:
#     j = 0
#     row_sum = 0
#     while j < c:
#         row_sum += matrix[i][j]
#         j += 1
#     print(row_sum, end=" ")
#     i += 1
# print()

# j = 0
# while j < c:
#     col_sum = 0
#     i = 0
#     while i < r:
#         col_sum += matrix[i][j]
#         i += 1
#     print(col_sum, end=" ")
#     j += 1

#! B5
# n = int(input())
# i = 0
# diag_sum, anti_diag_sum = 0, 0
# while i < n:
#     row = list(map(int, input().split()))
#     diag_sum += row[i]
#     anti_diag_sum += row[n-i-1]
#     i += 1
# print(diag_sum, anti_diag_sum)

#! B7
# r, c = map(int, input().split())
# i = 0
# matrix = []
# while i < r:
#     rows = list(map(int, input().split()))
#     matrix.append(rows)
#     i += 1

# t = []
# j = 0
# while j < c:
#     row = []
#     i = 0
#     while i < r:
#         row.append(matrix[i][j])
#         i += 1
#     t.append(row)
#     j += 1


# for _ in t:
#     print(*_)


