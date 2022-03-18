import threading
import time


lock = threading.Lock()


def function(n):
    global lock
    with lock:
        for i in range(n):
            time.sleep(1)
            print("hello world", threading.current_thread().name)

    for i in range(5):
        print("good morning", threading.current_thread().name)


for i in range(5):
    thread = threading.Thread(target=function, args=(5,))
    thread.name = "子线程{}".format(i)
    thread.start()

threading.current_thread().name = "主线程"
function(5)