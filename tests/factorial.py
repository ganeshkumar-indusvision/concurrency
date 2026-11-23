import math
from decimal import Decimal, getcontext


class Fact:
    def __init__(self):
        getcontext().prec = 1_000_000

    def factorial(self, n: int) -> Decimal:
        result = Decimal(1)

        for i in range(2, n + 1):
            result *= Decimal(i)

        return result


def test_factorial():
    calc = Fact()

    test_values = [0, 1, 5, 10, 20, 50, 100, 500, 1000]

    for n in test_values:
        expected = math.factorial(n)
        actual = calc.factorial(n)

        assert actual == Decimal(expected), f"Mismatch at {n}!"

        print(f"{n}! -> PASS ({len(str(actual))} digits)")

    print("All tests passed!")


if __name__ == "__main__":
    test_factorial()