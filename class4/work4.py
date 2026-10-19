# Heron's formula to calculate the area of a triangle given its three sides
# a = 3
# b = 4
# c = 5
# s = (a + b + c) / 2
# area = (s * (s-a) * (s-b) * (s-c)) ** 0.5
# print(area)

# x = 5 # an inline comment, after some code
# # a whole line that is a comment
# print(x) 

# print(5 + 3)
# print(type(7 > 3))


# print(7 == 3)
# print(7 != 3)
# print(7 < 3)
# print(7 > 3)
# print(7 <= 7)
# print(3 >= 7)

# print(True == 1)
# print(False == 0)
# print(True + True)
# print(False + 5)

# print(2 +3 < 4 +1)
# print(2 +(3 < 4) +1)

# score = 55
# attendance = 80
# print(score >= 40 and attendance >= 75)

# print(True and False)
# print(True or False)
# print(not True)
# print((5 > 3) and (2 > 4))

# print(bool(0), bool(0.0), bool(""), bool(None))
# print(bool(5), bool("hi"), bool(-1))

# first truthy value is returned, or the last value if all are falsy
# ?print(0 or 5)
# ?print("" or "hi")
# ?print(0 or "" or 0.0)

# first falsy value is returned, or the last value if all are truthy
# !print(3 and 7 and "" and "vaibhav")
# !print(0 and 7)

# print(True or False and False)



# """"
# # ── driver_dispatch.py (RideSurge Technologies · Core Dispatch Module) ──
# # Business rules (Ops Manual v5.1):
# # Rule A: Driver can accept a PREMIUM ride ONLY IF all three hold:
# # rating >= 4.7 AND trips_completed >= 200 AND car_type == "sedan"
# # Rule B: SURGE pricing fires when the rider/driver ratio is AT LEAST 3 (>= 3)
# # AND it is currently raining.
# # Rule C: FREE-RIDE coupon issued when customer is a new user AND at least one
# # of: (referral code used) OR (promo is active).
# # Existing users are NOT eligible, even if a promo is running.
# driver_rating = 4.8
# trips_completed = 150 # below the required 200-trip threshold
# car_type = "sedan"
# active_riders = 114 # exactly 3 times active_drivers
# active_drivers = 38
# rain = True
# is_new_user = False # this is a returning customer, not a new one
# referral_code = ""
# promo_active = True
# # Rule A — Premium ride eligibility
# can_take_premium = driver_rating >= 4.7 or trips_completed >= 200 or car_type == "sedan"
# # Rule B — Surge pricing
# surge_active = (active_riders / active_drivers) > 3 and rain == True
# # Rule C — Free-ride coupon
# free_ride_coupon = is_new_user and referral_code != "" or promo_active
# print("Premium eligible:", can_take_premium)
# print("Surge active: ", surge_active)
# print("Free ride coupon:", free_ride_coupon) """



# print(2 + 3)
# print("2" + "3")

# print("Hello" + ", " + "World!")
# print("ha" * 3)
# print("-" * 30)
# print(type("ha" * 3))


# print("hello" - "ello")
# print("hello" / 2)

# print("123" + 4)
# print("123" == 4)

print([1, 2] + [3, 4])
print([1, 2] * 3)



# ! decimal to binary
# print(bin(13))
# print(bin(255))
# print(bin(22))

# ! binary to decimal
# print(int("10110", 2))
# print(int("1010", 2))
# print(int("11111", 2))


# print(bin(42)) # base 2
# print(oct(42)) # base 8
# print(hex(42)) # base 16

# print(int("101010", 2)) # binary string -> decimal
# print(int("52", 8)) # octal string -> decimal
# print(int("2a", 16)) # hex string -> decimal

# print(0b101010) # binary literal
# print(0o52) # octal literal
# print(0x2a) # hex literal



# print(13 & 10)

# print(bin(13))
# print(bin(10))
# print(bin(13 & 10))

# print(12 & 10)
# print(6 & 3)

# print(12 | 10)
# print(6 | 3)

# print(12 ^ 10)
# print(6 ^ 3)
# print(9 ^ 9)
# print(9 ^ 0)

# ? shifts all bits << left
# print(bin(3)) # 0b11
# print(bin(3 << 1)) # shift left 1
# print(bin(3 << 2)) # shift left 2
# print(bin(3 << 3)) # shift left 3

# ? shifting all bits >> right
# print(16 >> 1)
# print(16 >> 2)
# print(16 >> 3)
# print(7 >> 1) 



# ? bit flags
# READ = 0b100 # 4
# WRITE = 0b010 # 2
# EXECUTE = 0b001 # 1
# perms = READ | WRITE # user can read and write, but not execute
# print(bin(perms))
# print(bool(perms & READ)) # can the user read?
# print(bool(perms & EXECUTE)) # can the user execute?




# print(0.1 + 0.2)
# print(0.1 + 0.2 == 0.3)

# print(f"{1/3:.3f}")

# print(f"{0.1:.55f}")

# import sys
# print(sys.float_info.dig) # significant decimal digits of precision
# print(sys.float_info.max) # largest representable float

# print(f"{0.1:.20f}")
# print(f"{0.2:.20f}")
# print(f"{0.3:.20f}")
# print(f"{0.1 + 0.2:.20f}")

# print(f"{0.1 + 0.2:.1f}")   # 0.3

# print(not 2 == 1)
# print((not 2) == 1)

