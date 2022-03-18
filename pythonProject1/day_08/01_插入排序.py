#插入排序
#将【1,2,4,5,3】从小到大排序
def insert_sort(ls:list):
    n_ls = []
    for i in ls:
        for j in range(0,len(n_ls)+1):
            if len(n_ls) == j or n_ls[j] > i:
                n_ls.insert(j,i)
                break
    ls.clear()
    ls.extend(n_ls)
ls = [4,3,5,1,2]
insert_sort(ls)
print(ls)
