# 打印100以下跳过7的倍数
n = -1
while n < 100:
    n += 1
    if n % 7 == 0:
        continue
    print(n)