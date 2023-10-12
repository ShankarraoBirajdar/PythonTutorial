import args


class ArithmaticOperation:
    def add(*args: int) -> int:
        x: int = 0
        for num in args:
            x = x + num
        return x

    def sub(num1: int, num2: int) -> int:
        return num1 - num2

    def mul(num1: int, num2: int) -> float:
        return num1 * num2

    def div(num1: int, num2: int) -> float:
        return num1 / num2
