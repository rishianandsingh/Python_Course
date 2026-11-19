# ! FOR LOOP INTRO

# print(range(5))

# print(type(range(5)))

# print(list(range(5)))



# for i in range(5):
#     print(i)

# print("=" * 20)

# for i in [0, 1, 2, 3, 4]:
#     print(i)


#? for i in range(start, end, step):


# d = [2, 9, 0, 7, 5, 6, 0]
# it = iter(d)

# while True:
#     try:
#         print(next(it))
#     except StopIteration:
#         break





#! 
# l = [(7,9), (1,2,3,4), (0, 9), (2,3,5), (1,2)]
# for x in l:
#     for y in x:
#         print(y, end=" ")



#? D1
# n = int(input())
# for i in range(11):
#     print(f"{n} x {i} = {n*i}")


#? D2
# r, c = map(int, input().split())
# for _ in range(r):
#     row = list(map(int, input().split()))
#     total = 0
#     for x in row:
#         total += x
#     print(total, end=" ")

#? E1
# n = int(input())
# dict = {}
# highest = float("-inf")
# total = 0
# for i in range(n):
#     name, score = input().split()
#     total += int(score)
#     if int(score) > highest:
#         highest = int(score)
#     dict[name] = int(score)

# print(total, highest)

