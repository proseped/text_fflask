def bubble_sort(ls : list):
    for i in range(0, len(ls) - 1):
        for j in range(0, len(ls) - 1 - i):
            if ls[j] > ls[j + 1]:
                ls[j], ls[j + 1] = ls[j + 1], ls[j]


ls = [2, 3, 4, 1, 5]
bubble_sort(ls)
print(ls)
