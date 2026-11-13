from src.factorial.factorial import Factorial
import time 
import decimal
import threading

import os

class Thread():
    def __init__(self):
        self.fact = Factorial()
        self.iter = 200
        self.worker_count = self.calculate_worker()
        self.base, self.extra = divmod(self.iter, self.worker_count)

    def calculate_worker(self):
        cores = os.cpu_count() or 1
        print(f"Total logical CPU cores: {cores}")
        return cores

    def worker(self):
        threads = []
        for w in range(self.worker_count):
            times = self.base + (1 if w < self.extra else 0)
            t = threading.Thread(target=self.create_thread, args=(times,))
            threads.append(t)
            t.start()

        for t in threads:
            t.join()

    def create_thread(self,times):
        for _ in range(times):
            self.fact.run()

    def run(self):
        start = time.perf_counter()
        self.worker()
        end = time.perf_counter()
        print(f"Total runtime of the program in thread is {end - start} seconds")
