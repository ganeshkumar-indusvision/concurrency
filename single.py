import numpy as np
import time



class Mul():
    def __init__(self):
        self.size = 2000
        self.a_matrix = None
        self.a_matrix = None
        self.generate_random()

    def generate_random(self):
        self.a_matrix = np.random.rand(self.size,self.size)
        self.b_matrix = np.random.rand(self.size,self.size)

    def run(self):
        result = self.a_matrix @ self.b_matrix

if __name__ == "__main__":
    mul = Mul()
    start = time.time()
    mul.run()
    end = time.time()
    print(f"Total runtime of the program is {end - start} seconds")