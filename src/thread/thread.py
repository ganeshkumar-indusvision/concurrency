from src.mul.mul import Mul
import threading
import time 

class Thread():
    def __init__(self):
        self.mul = Mul()


    def run(self):
        start = time.time()
        # self.mul.run()
        threads = []
        for i in range(5):
            t =  threading.Thread(target=self.mul.run)
            threads.append(t)
            t.start()
        # Start the thread
        # thread.start()
        # Wait for the thread to finish before exiting the main program
        # thread.join()
        for t in threads:
            t.join()
        print("Main thread: Execution finished")
        end = time.time()
        print(f"Total runtime of the program in thread is {end - start} seconds")


# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()  # Wait for all threads to complete