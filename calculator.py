from sys import exit
from typing import Tuple


def get_nums() -> Tuple[float, float]:
    num1: float = float(input("enter first number: "))
    num2: float = float(input("enter second number: "))

    return num1, num2


def calculator() -> None:
    options: str = """ Operations
        0: exit
        1: addition
        2: subtraction
        3: multiplication
        4: division
        """

    while 42:
        print(options)

        while 42:
            choice: int = int(input("select operation: "))

            if choice not in range(5):
                print("invalid selection, pick a number from 0 to 4")
                break
            elif choice == 0:
                exit()
            else:
                break

        nums: Tuple[float, float] = get_nums()

        match choice:
            case 1:
                print(nums[0] + nums[1])

            case 2:
                print(nums[0] - nums[1])

            case 3:
                print(nums[0] * nums[1])

            case 4:
                print(nums[0] / nums[1])


def with_eval():
    while 42:
        print("enter 0 to quit")
        data = input("enter equation: ").strip()
        if data == "0":
            exit()
        answer = eval(data)
        print(answer)


calculator()
# with_eval()
