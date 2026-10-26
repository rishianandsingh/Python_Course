# i = 1
# while i <= 5:
#     print(i)
#     i += 1

# ? Non terminating loops
# i = 1
# while i <= 5:
#     print(i)


# i = 1
# while i != 6:
#     print(i)
#     i = i + 2

# ! self
# n = int(input())
# i = 1
# while i<=n:
#     print(i)
#     i = i + 2


# n = 0
# while n > 0:
#     print("body runs")
#     n -= 1
# print("done")

# i = 0
# while True:
#     print(i)
#     i = i+1
#     if i == 5:
#         break
#     print(i)

# while True:
#     cmd = input("cmd> ")
#     if cmd == "quit":
#         print("bye")
#         break
#     print("you said:", cmd)



# ? Q14
# while True:
#     password = input("Pass: ")
#     if password != "open sesame":
#         print("wrong, try again")
#     else:
#         print("unlocked")
#         break



# ! self (wrong)
# attempts = 0
# while True:
#     password = input()
#     attempts += 1
#     if password != "open sesame":
#         if attempts == 5:
#             print("blocked")
#             break
#         print("wrong, " + str(5 - attempts) + " attempts remaining")
#     else:
#         print("unlocked")
#         break


# ? P1 Multiplication table
# n = int(input())
# i = 1
# while i<=10:
#     print(n, "X", i, "=", n*i)
#     i= i+1


# ? Factors of a number
# import math
# n = int(input())
# i=1
# while i*i <= n:
#     if n%i == 0:
#         if  i == n//i:
#             print(i)
# #         else:
# #             print(i, n//i)     
# #     i = i+1


# # ? Factorial
# n = int(input())
# i = 1
# ans = 1
# while i<=n:
#     ans = ans * i
#     i = i + 1
# print(ans)


# ? Prime or not
# n = int(input())
# if n<2:
#     print("not prime")
# else:
#     i = 2
#     is_prime = True
#     while i*i <= n:
#         if n%i == 0:
#             is_prime = False
#             break
#         i = i+1
# if is_prime:
#     print("prime")
# else:
#     print("not prime")

