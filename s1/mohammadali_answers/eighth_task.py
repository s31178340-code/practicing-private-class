# #1
# import random
# b=[random.randint(1,100)
# for a in range(10)]
# print(b)

# 2
b = [2, 41, 20, 87, 59, 31, 62, 64, 18, 50]
c = []


def a():
    for a in b:
        print(type(a//2))
        if type(a//2) == int:
            c.append(a)
            print(c)


# call
a()
