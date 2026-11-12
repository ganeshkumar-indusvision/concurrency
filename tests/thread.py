import time
import threading
import sys, sysconfig
print(sys.version)                                       
print("GIL disabled at build:", sysconfig.get_config_var("Py_GIL_DISABLED"))
print("GIL enabled at runtime:", sys._is_gil_enabled())
def factorial(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

def worker(times):
    for _ in range(times):
        factorial(40000)
if __name__ == "__main__":
    start = time.perf_counter()

    # 1 is worker and 200 is number of iteration.
    # base is the number of iteration and extra is the remaining iteration.
    # this will help to divide the work among the workers.
    worker_num = 24
    base, extra = divmod(200,worker_num)
    print(f"base: {base}, extra: {extra}")
    workers = []
    for w in range(worker_num):
        times = base +(1 if w < extra else 0)
        t = threading.Thread(target= worker , args=(times,))
        t.start()
        workers.append(t)

    for w in workers:
        w.join()


        
    
    end = time.perf_counter()
    print(f"Total runtime of the program in worker is {end - start} seconds")
