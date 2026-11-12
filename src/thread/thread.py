from src.factorial.factorial import Factorial
import time 
import decimal
import threading

class Thread():
    def __init__(self):
        self.fact = Factorial()


    def run(self):
        start = decimal.Decimal(str(time.time()))
        # self.fact.run()
        threads = []
        for i in range(5):
            t =  threading.Thread(target=self.fact.run)
            threads.append(t)
            t.start()
        # Start the thread
        # thread.start()
        # Wait for the thread to finish before exiting the main program
        # thread.join()
        for t in threads:
            t.join()
        print("Main thread: Execution finished")
        end = decimal.Decimal(str(time.time()))
        print(f"Total runtime of the program in thread is {end - start} seconds")


# for i in range(5):
#     t = threading.Thread(target=worker, args=(i,))
#     threads.append(t)
#     t.start()
# for t in threads:
#     t.join()  # Wait for all threads to complete