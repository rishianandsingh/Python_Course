# n = int(input())
# if n%2 == 0:
#     print("even")
# if n%2 != 0:
#     print("odd")



# n = int(input())
# if n%3 == 0 :
#     print("fizz", end="")
# if n%5 == 0:
#     print("buzz")


# x = int(input())
# if x>20:
#     x = x+25
# elif x>10:
#     x = x+15
# print(x)


# score = int(input())
# if score>90:
#     print("A")
# elif score>80:
#     print("B")
# elif score>70:
#     print("C")
# elif score>60:
#     print("D")
# elif score>50:
#     print("E")
# else:
#     print("F")

# ? 25A
# age = int(input())
# if age>=18:
#     print("You can vote.")

# ? 31A
# y = int(input())
# if y%4==0:
#         if y%100==0:
#                 if y%400==0:
#                         print("Leap")
#                 else:
#                         print("Not Leap")
#         else:
#                 print("Leap")
# else:
#         print("Not Leap")


# ? 26A
# bill = int(input())
# if bill>1000:
#     disc_price = bill - (0.1*bill)
#     print(f"Discounted price: Rs.{disc_price:.2f}")


# ? 27A
# score = int(input())
# if score>=135:
#     x = (score/150)*100
#     print(f"Merit scholarship awarded. Percentage: {x:.2f}%")

# ? 28A
# !
# a = int(input())
# b = int(input())
# c = int(input())
# average = (a+b+c)/3
# if average>80 and a> 60 and b>60 and c>60:
#     print("Distinction awarded.")


# ? 30B
# units = int(input())
# print("Bill: Rs.", end="")
# if units <=100:
#     x =  units*1.5
#     print(f"{x:.2f}")
# else:
#     y = units*2.5
#     print(f"{y:.2f}")
    

# ? 32B
# km = float(input())
# if km ==0:
#     print("No trip.")
# elif km<=2:
#     print("Fare: Rs.50.00")
# elif km>=2:
#     x = 50.00 + 15*(km-2)
#     print(f"Fare: Rs.{x:.2f}")


# ? 33C
# import sys
# n = int(sys.stdin.readline())
# if n > 0:
#     sys.stdout.write("Positive\n")
# if n % 2 == 0:
#     sys.stdout.write("Even\n")
# if n > 100:
#     sys.stdout.write("Large\n")
    

# ? 34C
import sys
score = int(sys.stdin.readline())
attendance = int(sys.stdin.readline())
if score>90:
    sys.stdout.write("Star student\n")
if attendance>90:
    sys.stdout.write("Perfect attendance\n")
