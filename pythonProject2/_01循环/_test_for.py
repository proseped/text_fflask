# 打印100以下正整数，跳出个位带7的数
for i in range(100):
    if i < 9:
        print(i)
    else:
        if i % 10 == 7:
            continue
        print(i)

# 1到100的和
sum = 0
for i in range(101):
    sum += i
print(sum)
