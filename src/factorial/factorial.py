from unittest import result


class Factorial():
    def __init__(self, num=20000):
        self.num = num

    def run(self):
        if self.num < 0:
            raise ValueError("Factorial is not defined for negative numbers.")
        result = 1
        for i in range(2, self.num + 1):
            result *= i
        return result
