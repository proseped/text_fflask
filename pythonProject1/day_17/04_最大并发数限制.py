import threading
import time

lock = threading.Semaphore(1)


def function(n):
    global lock
    with lock:
        for j in range(n):
            time.sleep(0.1)
            print("hello world", threading.current_thread().name, threading.current_thread().is_alive())


for i in range(5):
    thread = threading.Thread(target=function, args=(5,))
    thread.name = "子线程{}".format(i)
    thread.start()
