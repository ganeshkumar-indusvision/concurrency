import threading
import time

# Even using RLock here will still cause a deadlock!
lock_1 = threading.Lock()
lock_2 = threading.Lock()

def worker_a():
    with lock_1:
        print("Worker A acquired Lock 1")
        time.sleep(0.5)  # Give Worker B time to grab Lock 2
        print("Worker A waiting for Lock 2...")
        with lock_2:
            print("Worker A acquired Lock 2")

def worker_b():
    with lock_2:
        print("Worker B acquired Lock 2")
        time.sleep(0.5)  # Give Worker A time to grab Lock 1
        print("Worker B waiting for Lock 1...")
        with lock_1:
            print("Worker B acquired Lock 1")

t1 = threading.Thread(target=worker_a)
t2 = threading.Thread(target=worker_b)

t1.start()
t2.start()

t1.join()
t2.join()