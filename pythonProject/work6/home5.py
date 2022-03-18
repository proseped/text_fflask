#输入10个整数存入列表，统计输出其中的正数、负数和零的个数。
a = [1, 3, 2, 4, 0, -1, -2.5, 0]
b = []
c = []
d = []
for i in a:
    if i > 0:
        b.append(i)
    elif i < 0:
        c.append(i)
    else:
        d.append(i)
print("列表a包含正数的数量是：%d，值是：%s" % (len(b), b))
print("列表a包含正数的数量是：%d，值是：%s" % (len(c), c))
print("列表a包含数字0，数量是：%d" % len(d))