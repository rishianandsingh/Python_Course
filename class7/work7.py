import sys

# ? Domino piling 50A
# m, n = map(int, sys.stdin.readline().split())
# x = (m*n)//2
# sys.stdout.write(str(x) + "\n")

# ? Codeforces checking 1791A
# t = int(sys.stdin.readline())
# for i in range(t):
#     c = sys.stdin.readline().strip()
#     if c in "codeforces":
#         sys.stdout.write("YES\n")
#     else:
#         sys.stdout.write("NO\n")


# ? 1955A Yogurt sale
# t = int(sys.stdin.readline())
# for i in range(t):
#     n, a, b = map(int, sys.stdin.readline().split())
    # if 2*a<b:
    #     x = n*a
    #     sys.stdout.write(str(x) + "\n")
    # else:
    #     x = (n//2)*b + (n%2)*a
    #     sys.stdout.write(str(x) + "\n")


# ? 1360A Minimal square
# t = int(sys.stdin.readline())
# for i in range(t):
#     a, b = map(int, sys.stdin.readline().split())
#     x = min(a, b)
#     y = max(a, b)
#     if 2*x >= y:
#         sys.stdout.write(str((2*x)*(2*x)) + "\n")
#     else:
#         sys.stdout.write(str(y*y) + "\n")


# ? 486A Calculating Functions
# n = int(sys.stdin.readline())
# if n%2 == 0:
#     fn = n//2
#     sys.stdout.write(str(fn) + "\n")
# else:
#     fn = -(n+1)//2
#     sys.stdout.write(str(fn) + "\n")


 # ? 1A Theatre Square
# n, m, a = map(int, sys.stdin.readline().split())
# rows = (n + a -1)//a
# cols = (m + a - 1)//a
# sys.stdout.write(str(rows*cols) + "\n")






n = int(sys.stdin.readline())
if n<10:
    print("yes") 
