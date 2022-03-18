# 从前往后两两比较，大的往后面排，依次循环
def bubble_sort(ls: list):
    for i in range(0, len(ls)-1):
        for j in range(0, len(ls)-1-i):
            if ls[j] > ls[j+1]:
                ls[j], ls[j+1] = ls[j+1], ls[j]
    return ls


print(bubble_sort([2, 4, 7, 7, 8, 3]))
