import queue
import threading
import time

q =  queue.Queue()
NUM_WORKERS = 4
d = {}
def worker():
    while True:
        update_id = q.get()
        if update_id is None:
            q.task_done()
            return
        value = d[update_id]
        # print(type(value));print(value)
        d[update_id] = value +1
        q.task_done()

    
def add():
    # global d
    for i in range(50000):
        d[i]= i
        q.put(i)
    return d


add()
workers = [threading.Thread(target=worker) for i in range( NUM_WORKERS)]
t = time.perf_counter()
for worker in workers:worker.start()
q.join()
for _ in range(NUM_WORKERS): q.put(None)

for worker in workers:worker.join()
end = time.perf_counter()
# worker()/
# print(d)

for key,value in d.items():
    # print(key)
    # print(key,value)
    if key != int(value-1):
        print("failed")
    
print(len(d), "completed")
print("takend time ", t - end)

