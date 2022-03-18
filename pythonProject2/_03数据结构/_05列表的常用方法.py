def creat_list():
    return [i for i in "一二三四五六七八九十"]


ls = creat_list()
print(ls)
ls.append("十一")
print(ls)
# 插入
ls.insert(5, "ABC")
print(ls)
# 导入
ls.extend([1,2,3,4])
print(ls)
# 删除指定元素
ls = creat_list()
ls.pop(4)
print(ls)
# 删除指定值的元素
ls = creat_list()
ls.remove("九")
print(ls)

# 改
# 逆序
ls = creat_list()
ls[2:4] = [1,2,3,4,5]
print(ls)
ls.reverse()
print(ls)

# 排序
ls = []