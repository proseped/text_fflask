def function(n, s):
    for i in range(n):
        print(s)
        yield True
    yield False


i1 = iter(function(5, "hello world!!"))
i2 = iter(function(6, "good morning!!"))

ret2 = ret1 = True

while ret1 or ret2:
    if ret1:
       ret1 = next(i1)
    if ret2:
        ret2 = next(i2)
