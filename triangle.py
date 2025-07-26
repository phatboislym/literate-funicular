def triangle(size):
    for i in range(1, size + 1):
        print("*" * i)


def triangle2(size):
    if size <= 0:
        return
    triangle2(size - 1)
    print("*" * size)


triangle2(5)


"""
triangle2(5)
size = 5
is 5 <= 0

triangle2(4)
is 4 <= 0
triangle2(3)
...
triangle2(2)
"*" * size **
trianlge2(1)
"*" * size *
triangle2(0)
is 0 <= 0
"""
