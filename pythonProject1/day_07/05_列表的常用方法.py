def creat_list():
    return [i for i in "零一二三四五六七八九十"]
ls = creat_list()

#增
# ls.append("十一")
# print(ls)
# ls.insert(5,"ABCD")  #每次打印都创建了一个新列表
# print(ls)
# ls.extend([1234])  #追加到列表末尾
# print(ls)

#删
ls = creat_list()
ls.pop()
print(ls)

ls = creat_list()
ls.pop(4)
print(ls)

ls = creat_list()
ls.remove("三")
print(ls)

ls = creat_list()
ls.clear()
print(ls)

#改
ls[2:4] = [1,2,3,4,5]
ls = creat_list()
ls.reverse()
print(ls)

ls = [5,5,7,3,9,7,2]
ls.sort()
print(ls)

ls = [5,5,7,3,9,7,2]
ls.sort(reverse=True)
print(ls)

ls = ["ohfoo","jfioshf","lofol","fkff","kf"]
ls.sort(key=len,reverse=False)    #比较返回值大小，key为键值对
print(ls)

ls = [i for i in "一零十四五六七八九二三"]
print(ls)
def comp(s):
    return "零一二三四五六七八九十".find(s)
ls.sort(key=comp)
print(ls)

#查
ls = creat_list()

print("八" in ls)
print("fl" in ls)

print(ls.index("九"))
print(ls.index("九",4,11))
















