from src.factorial.factorial import Factorial
import time 
import decimal

class Simple():
    def __init__(self):
        self.fact = Factorial()
        self.iter = 200

    def worker(self):
        for i in range(self.iter):
            self.fact.run()
    def run(self):
        start = time.perf_counter()

        self.worker()
        end = time.perf_counter()
        print(f"Total runtime of the program in simple is {end - start} seconds")