# import sys
# t = int(sys.stdin.readline())
# for i in range(t):
#     a,b = map(int, sys.stdin.readline().split())
#     if a>2*b or b>2*a:
#         sys.stdout.write("NO\n")
#     elif (a+b)%3 == 0:
#         sys.stdout.write("YES\n")
#     else:
#         sys.stdout.write("NO\n")
    


a, b, c = map(int, input().split())
if a+b<c or b+c<a or a+c<b:
    print("Not a Triangle")
else:
    if a==b==c:
        print("Equilateral")
    elif a==b!=c or b==c!=a or c==a!=b:
        print("Isosceles")
    elif a!=b!=c:
        print("Scalene")