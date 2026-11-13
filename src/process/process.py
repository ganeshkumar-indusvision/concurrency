from src.factorial.factorial import Factorial
import time 
import decimal
from multiprocessing import Process

import os

class CreateProcess():
    def __init__(self):
        self.fact = Factorial()
        self.iter = 100
        self.worker_count = self.calculate_worker()
        # self.worker_count = 102
        self.base, self.extra = divmod(self.iter, self.worker_count)

    def calculate_worker(self):
        cores = os.cpu_count() or 1
        print(f"Total logical CPU cores: {cores}")
        return cores

    def worker(self):
        process = []
        for w in range(self.worker_count):
            times = self.base + (1 if w < self.extra else 0)
            t = Process(target=self.create_process, args=(times,))
            process.append(t)
            t.start()

        for t in process:
            t.join()

    def create_process(self,times):
        for _ in range(times):
            self.fact.run()

    def run(self):
        start = time.perf_counter()
        self.worker()
        end = time.perf_counter()
        print(f"Total runtime of the program in process is {end - start} seconds")
