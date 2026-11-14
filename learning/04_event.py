import queue,threading,time
q = queue.Queue()

stop = threading.Event()


def worker(name):
    while not stop.is_set():

        try:
            item=q.get(timeout=0.2)
        except queue.Empty:
            continue
        # item= q.get()
        if item != None:
            # print(item)
            time.sleep(0.3)                   # fake work
            print(f"{name} done with {item}")
            q.task_done()


        if item == None:
            q.task_done()
            return


workers = [threading.Thread(target=worker , args=(f"worker-{i}",)) for i in range(20)]
[worker.start() for worker in workers ]


[q.put(i) for i in range(200)]
time.sleep(1.0) 

q.join()     

stop.set()                 
for _ in workers:
    q.put(None)

for t in workers:
    t.join(timeout=2)
    assert not t.is_alive(),f"{t.name} is still alive!"

# worker.start();
print("It's over")

