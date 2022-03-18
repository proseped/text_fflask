# 导入到另一个列表当中，将数字插入，从前往后比较
def insert_num(ls: list):
    n_ls = []
    for i in ls:
        for j in range(0, len(n_ls)+1):
            if j == len(n_ls) or n_ls[j] > i:
                n_ls.insert(j, i)
                break
    ls.clear()
    ls.extend(n_ls)


ls = [2, 4, 5, 7, 9, 3, 4]
insert_num(ls)
print(ls)