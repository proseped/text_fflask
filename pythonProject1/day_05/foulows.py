#编写一个函数，打印所有的水仙花数

def foulows():
    for i in range(100,1001):
        a = i % 100
        b = i // 10 % 10
        c = i % 10
        if i == a*a*a + b*b*b + c*c*c:
            print(i)
    foulows()