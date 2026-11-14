# import threading

# 

# print(stop.is_set())      
# stop.set()

# print(stop.is_set())
# stop.clear()

# print(stop.is_set())

import queue,threading,time
q = queue.Queue()

stop = threading.Event()
def produce():
    stop.set()
    for i in range(5):
        q.put(i)
        print("Added :", i)
        time.sleep(2)  
    q.put(None)




def consume():

    while stop.is_set():
        item= q.get()
        if item != None:
            print(item)
        if item == None:
            stop.clear()
        


producer = threading.Thread(target=produce)

consumer = threading.Thread(target=consume)

producer.start();consumer.start()


producer.join();consumer.join()