# 从第一个开始依次和后面的数比较
def select_sort(ls:list):
    for i in range(0, len(ls)-1):
        for j in range(i+1, len(ls)):
            if ls[i] > ls[j]:
                ls[i], ls[j] = ls[j], ls[i]
    return ls


print(select_sort([2, 3, 4, 5, 8, 4, 6]))