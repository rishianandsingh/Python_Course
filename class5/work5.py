# names = "Python"
# scores = [95, 87, 92, 34, 45]
# tags = {"Python", "AI", "Beginner"}
# print(names[1])
# print(scores[1])
# print(tags[1])


# ? IndexError
# names = "Python"
# print(names[6])


# # ? [] ==> list
# scores = [95, 87, 92]
# print(type(scores))
# # ? {} ==> set
# tags = {95, 87, 92}
# print(type(tags))

# ? empty dict/set
# print(type({})) 
# print(type(set()))


# ? sets ignores duplicates
# print(len([1, 1, 2, 2, 2, 3, 3]))
# print(len({1, 1, 2, 2, 2, 3, 3}))

# ? index appliess to lists
# l1 = [3, 90, 7, 6]
# print(l1[2])

# ? sets cant do indexing since no order
# s1 = {3, 5, 67, 59}
# print(s1[2])

# ? TypeError: 'str' object does not support item assignment 
# ! str is immutable to promote reuse
# s = "hello"
# s[0] = "H"
# print(s)

# lst = [10, 20, 30]
# lst[0] = 99
# print(lst)

# ? you can change assignement of a name but not the assigned value itself
# x = 9
# y = 9.9
# z = "bombay"
# w = z
# print(id(x), id(y), id(z), id(w))


# name1 = "aditya"
# print(id(name1))
# name1 = name1.upper()
# print(id(name1))

# ? str, int, tuple are immutable
# s = {1, 2, 3}
# s.add(42)
# print(s)
# s.add("hello")
# print(s)
# s.add((10, 20)) ==> tuple
# print(s)
# ? TypeError because lists are unhashable/mutable
# s.add([1, 2])
# print(s)


# ? list is unhashable/mutable ==> TypeError
# print(hash((1, 2, 3))) 
# print(hash((1, [2, 3])))


# ? in/not in ===> membership operators
# print('y' in "Python")
# print(87 in [95, 87, 92])
# print("AI" in {"Python", "AI", "Beginner"})
# print('z' in "Python")
# print(100 in [95, 87, 92])
# print("SQL" in {"Python", "AI", "Beginner"})


# coords = {(0, 0), (1, 2), (3, 4), (1, 2)}
# print(coords)
# print(len(coords))


# ? indexing goes backward as well
# s = "Python"
# print(s[0])
# print(s[1])
# print(s[-1])
# print(s[-2])
# print(s[3])

# ? Slicing
# s = "Programming"
# print(s[3:4])
# print(s[:4])
# print(s[4:])
# print(s[-3:])
# print(s[:-2])
# print(s[:])
 
# ! self do
# x = input("Enter string: ")
# if len(x) % 2 != 0:
#     print(x[:3] + x[len(x)//2] + x[-3:])
# else:
#     print(x[:3] + x[len(x)//2 - 1] + x[len(x)//2] + x[-3:])

# ? stepwise slicing
# s = "abcdefghij"
# print(s[::2])
# print(s[::-1])


# ? upper/lower
# s = "Hello World"
# print(s.upper())
# print(s.lower())
# print(s)


# ? stripping lead/trailing space
# raw = " hello world "
# print(raw.strip())
# print(raw.lstrip())
# print(raw.rstrip())
# print(len(raw), len(raw.strip()))


# ? .split()
# x = " , , , , ,hello,world"
# print(x.split(","))


# line = "A101,Laptop,5,29999.99"
# parts = line.split(",")
# print(parts[0])
# print(parts[2])
# print(type(parts[2]))


# ? replace
# msg = "hello world"
# print(msg.replace("world", "python"))
# print(msg.replace("l", "L"))
# print(msg)

# ? ord/char
# print(ord('A'))
# print(ord('a'))
# print(ord('0'))
# print(chr(65))
# print(chr(97))
# print(chr(66))

# print(chr(ord('A')+3))
# print(chr(ord('z')-25))

# ! Tuples


