#打印26层字母金字塔
for i in range(1, 27):
    print(' '*(27-i), end=' ')
    print('*'*(2*i-1))