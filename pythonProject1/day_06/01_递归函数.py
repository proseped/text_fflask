def print_n_helloworld(n):
    if n == 0:return
    print_n_helloworld(n-1)
    print("hello world!")
print_n_helloworld(5)

#计算1+2+3+。。。+100的值
def count(n):
    if n == 2:
        return 3
    return count(n-1) + n
print((count(100)))

#例如计算 m = 3,n = 4时 4+ 44+ 444的值
def count_sum(m,n):
    if m == 0:
        return 0
    s = 0
    for i in range(m):
        s = n * 10**i
    return count_sum(m-1,n) + s
print(count_sum(4,1))


def do_max_count(*n):
    x = n[0]
    while True:
        all = True
        for i in n:
            if i % x != 0:
                all = False
                break
        if all:
            return x
        else:
            x -= 1


do_max_count(2,4)