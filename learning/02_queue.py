import queue,threading
q = queue.Queue()


def produce():
    for i in range(5):
        q.put(i)
        print("Added :", i)
    q.put(None)


def consume():

    while True:
        # item = 
    # for i in range(5):
        item= q.get()
        # if item == None:
            # return
        print(item)


producer = threading.Thread(target=produce)

consumer = threading.Thread(target=consume)

producer.start();consumer.start()


producer.join();consumer.join()




# try:
    # q.get(timeout=1)
# except queue.Empty:
    # print("It's emty bro")

# q.put("it's")
# q.put("done")
# q.put("bro")

# print(q.get())
# print(q.get())
# print(q.get())