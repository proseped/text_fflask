def creat_dict():
    return {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}

#增
d = creat_dict()
d.setdefault("Six",6)
print(d)

d["Serven"] = 7
print(d)

d["Two"] = "二"
print(d)

#删
d = creat_dict()
#删除任意一个
d.popitem()
print(d)
#删除指定一个
d.pop("Two")
print(d)

d.clear()
print(d)

#改
d = creat_dict()
d["Two"] = "二"
print(d)

#查
d = creat_dict()
print(d["One"])









