from src.mul.mul import Mul
import time 

class Simple():
    def __init__(self):
        self.mul = Mul()

    def run(self):
        start = time.time()
        self.mul.run()
        end = time.time()
        print(f"Total runtime of the program in simple is {end - start} seconds")