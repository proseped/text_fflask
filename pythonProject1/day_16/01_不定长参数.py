def println(*args):
    for i in args:
        print(i)


println(1, 3, 45, 5)


def print_dict(**kwargs):  # 返回字典，键值对
    print(kwargs)


print_dict(d=4, ds=5, we=4)


def print_all(*args, **kwargs):
    pass
