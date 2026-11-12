from src.mul.mul import Mul
import time 

mul = Mul()
start = time.time()
mul.run()
end = time.time()
print(f"Total runtime of the program is {end - start} seconds")