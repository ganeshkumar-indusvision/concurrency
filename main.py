from src.simple.simple import Simple
from src.thread.thread import Thread
from src.process.process import CreateProcess

import sys

# print()
# import time 

# mul = Simple()
# start = time.time()
# mul.run()
# end = time.time()
# print(f"Total runtime of the program is {end - start} seconds")

if __name__ == "__main__":
    print(sys.version)
    sim= Simple()
    sim.run()

    thread = Thread()
    thread.run()


    process = CreateProcess()
    process.run()