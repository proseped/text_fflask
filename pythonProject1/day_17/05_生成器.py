def function():
    print("1"*5)
    print("2"*5)
    yield
    print("3"*5)
    print("4"*5)
    yield 0
    print("5"*5)
    yield 1


i = iter(function())    # 创建生成器，并没有调用函数
next(i)
print('============')
print(next(i))
print("-------------")
print(next(i))

# 生成器，提供了分步执行函数的可行性