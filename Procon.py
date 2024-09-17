import threading as th
import time as t
import random as r
from queue import Queue
BUFFER_SIZE = 5
buffer = Queue(maxsize=BUFFER_SIZE)
def producer():
    while True:
        item = r.randint(1, 100)
        buffer.put(item)
        print("Producer Produced: ",item)
        t.sleep(r.uniform(0.5, 2))
def consumer():
    while True:
        item = buffer.get()
        print("Consumer consumed: ",item)
        t.sleep(r.uniform(0.5, 2))
pt = th.Thread(target=producer)
ct = th.Thread(target=consumer)
pt.start()
ct.start()
'''pt.join()
ct.join()'''