def iteration(size):
    if size <= 0:
        return 0
    if size == 1:
        return 1

    num1, num2 = 0, 1
    for i in range(2, size + 1):
        num1, num2 = num2, num1 + num2
    return num2


def recursion(size: int) -> int:
    if size <= 0:
        return 0
    if size == 1:
        return 1

    return recursion(size - 1) + recursion(size - 2)


print(iteration(29))
print(recursion(29))
