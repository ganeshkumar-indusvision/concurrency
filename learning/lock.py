import threading,  time
counter = 0
lock = threading.Lock()
def bump(worker_name):
    global counter
    t0 = time.perf_counter()
    for _ in range(20000):
        # with lock: 
            counter +=1

    print(f"{worker_name}: {time.perf_counter() - t0:.3f}s")
    # with lock: 
        # [(counter := counter+ 1) for i in range(20000)]

outer = time.perf_counter()
ts = [threading.Thread(target=bump, args=(f"worker-{i}",))for i in range(4)]
[t.start() for t in ts];[t.join() for t in ts]
print(counter)
print(f"{time.perf_counter() - outer:.3f}s")