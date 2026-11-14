import queue
q = queue.Queue()


q.put("it's")
q.put("done")
q.put("bro")

print(q.get())
print(q.get())
print(q.get())