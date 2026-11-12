from src.factorial.factorial import Factorial
import time 
import decimal

class Simple():
    def __init__(self):
        self.fact = Factorial()

    def run(self):
        start = decimal.Decimal(str(time.time()))
        self.fact.run()
        end = decimal.Decimal(str(time.time()))
        print(f"Total runtime of the program in simple is {end - start} seconds")