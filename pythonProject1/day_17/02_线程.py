import threading
import time


def function(n):
    for i in range(n):
        time.sleep(1)
        print("hello world", threading.current_thread().name)


thread = threading.Thread(target=function, args=(5,))
thread.name = "子线程"
thread.start()

threading.current_thread().name = "主线程"
function(5)