import numpy as np

class Mul():
    def __init__(self, size=2000,iter=10):
        self.size = size
        self.a_matrix = None
        self.a_matrix = None
        self.enable = True
        self.iter = iter
        self.generate_random()

    def generate_random(self):
        self.a_matrix = np.random.rand(self.size,self.size)
        self.b_matrix = np.random.rand(self.size,self.size)

    def run(self):
        count = 0 
        while(self.enable):
            result = self.a_matrix @ self.b_matrix
            count = count + 1
            if count == self.iter:
                self.enable = False

# if __name__ == "__main__":
 