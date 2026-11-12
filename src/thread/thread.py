from src.mul.mul import Mul
import threading
import time 

class Thread():
    def __init__(self):
        self.mul = Mul()


    def run(self):
        start = time.time()
        # self.mul.run()
      
        thread = threading.Thread(target=self.mul.run)
        # Start the thread
        thread.start()
        # Wait for the thread to finish before exiting the main program
        thread.join()
        print("Main thread: Execution finished")
        end = time.time()
        print(f"Total runtime of the program in thread is {end - start} seconds")