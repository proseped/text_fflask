import time

ls = [1, 2, 3, 4, 5]
i = iter(ls)

while True:
    time.sleep(1)
    try:
        print(next(i))
    except StopIteration:
        break
