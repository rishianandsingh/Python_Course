# n = 4827
# rev = 0
# while n>0:
#     rev = rev*10 + n%10
#     n = n//10
# print(rev)

# n = int(input())
# count = 0
# while n>0:
#     count += 1
#     n = n//10
# print(count)


# ! GCD & LCM by Loops

# ? GCD

#! self
# a = int(input())
# b = int(input())
# i = 1
# minimum = min(a, b)
# if min(a, b) == 0:
#     gcd = max(a, b)
# elif max(a,b) % minimum == 0:
#             gcd = minimum
# else:
#     while i <= (minimum//2):
#         if a%i==0 and b%i == 0:
#             gcd =i
#         i += 1
# print(gcd)



# a = int(input())
# b = int(input())
# i = min(a ,b)
# if min(a, b) ==0:
#     gcd = max(a,b)
# else:
#     while i <= min(a,b):
#         if a%i==0 and b%i==0:
#             gcd = i
#             break
#         i -= 1
# print(gcd)


# ? LCM

# a = int(input())
# b = int(input())
# i = max(a, b)
# if a == 0 or b == 0:
#     lcm = 0
# else:
#     while i <= a*b:
#         if i%a == 0 and i%b == 0:
#             lcm = i
#             break
#         i += 1
# print(lcm)


# ?

# n = int(input())
# a = int(input())
# b = int(input())
# i = min(a,b)
# count = 0
# while i <= n:
#     if i%a == 0 or i%b == 0:
#         count += 1
#     i += 1
# print(count)


# n = int(input())
# a = int(input())
# b = int(input())
# i = max(a, b)
# if a == 0 or b == 0:
#     lcm = 0
# else:
#     while i <= a*b:
#         if i%a == 0 and i%b == 0:
#             lcm = i
#             break
#         i += 1
# ans = n//a + n//b - (n//lcm)
# print(ans)


#? Euclidean algo (gcd)

# a = int(input())
# b = int(input())
# dividend = max(a, b)
# divisor = min(a, b)
# if a == 0 or b == 0:
#     gcd = max(a,b)
# else:
#     while dividend%divisor != 0:
#         rem = dividend % divisor
#         divisor = rem
#         dividend = divisor
#     gcd = divisor
# print(gcd)



# ! GCD of n numbers
# n = int(input())
# a = list(map(int, input().split()))
# g = a[0]
# i = 1
# while i < n:
#     x = g
#     y = a[i]
#     while y != 0:
#         x, y = y, x % y
#     g = x
#     i = i + 1
# print(g)




# ? pattern 1
# n = 5
# i = 1
# while i <= n:
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     i += 1



# ? pattern 2
# n = int(input())
# i = 1
# spaces = n+2
# while i <= n:
#     j = 1
#     print(" "*spaces, end=" ")
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     print()
#     spaces -= 2
#     i += 1


# ? pattern 3
# n = int(input())
# i = 1
# spaces = n+2
# while i <= n:
#     j = i
#     print(" "*spaces, end=" ")
#     while j >= 1:
#         print(j, end=" ")
#         j -= 1
#     print()
#     spaces -= 2
#     i += 1


# ? pattern 4
# n = int(input())
# i = 1
# while i <= n:
#     print("  "*(n-i), end="")
#     j = 1
#     while j <= i:
#         print(j, end=" ")
#         j += 1
#     j = i-1
#     while j > 0:
#         print(j, end=" ")
#         j -= 1
#     print()
#     i += 1



#? star patten

# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <=n-i:
#         print(" ", end=" ")
#         j += 1
#     j = 1
#     while j <= i:
#         print("*", end=" ")
#         j += 1
#     j = i-1
#     while j > 0:
#         print("*", end=" ")
#         j -= 1
#     print()
#     i += 1



# n = int(input())
# i = 1
# while i <= n:
#     j = 1
#     while j <=n-i:
#         print(" ", end=" ")
#         j += 1
#     j = 1
#     while j <= 2*i-1:
#         print("*", end=" ")
#         j += 1
#     print()
    # i += 1





# n = int(input())
# i = 1
# while i <= n:
#     print("  "*(n-i), end="")
#     print("* "*(2*i-1))
#     i += 1




# ? pattern 5
# n = int(input())
# i = 1
# while i <= 