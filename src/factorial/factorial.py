from unittest import result


class Factorial():
    def __init__(self, num=20000,iter=200):
        self.num = num
        self.enable = True
        self.iter = iter

    def run(self):
        count = 0
        while(self.enable):
            if self.num < 0:
                raise ValueError("Factorial is not defined for negative numbers.")
            result = 1
            for i in range(2, self.num + 1):
                result *= i
            count += 1
            if self.iter == count:
                self.enable = False

# if __name__ == "__main__":
