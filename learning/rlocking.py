import threading


# rlock = threading.RLock()
rlock = threading.Lock()

with rlock:
    print("Acquired Lock the first Lcok")

    with  rlock:
        print("Again Locking")

print("completed without dead")