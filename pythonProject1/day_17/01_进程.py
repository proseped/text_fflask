import multiprocessing
import time
import os


def function(n):
    p = multiprocessing.current_process()
    for i in range(n):
        time.sleep(1)
        print(p.name, "world", p.pid, os.getppid())


if __name__ == '__main__':
    process = multiprocessing.Process(None, target=function, args=(8,), name="子进程")
    process.name = "子进程"
    process.start()
    multiprocessing.current_process().name = "主进程"

    function(5)