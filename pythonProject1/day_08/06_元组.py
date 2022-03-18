t = (1, 3, 5, 7, 9, "hello world!")
# print(t)
# print(t[5])
# print(len(t))
for j in t:
    print(j)

a,b = (1,2)
print(a,b)

def get_more_value():
    return ("192.168.96.1",8080)
ip ,port = get_more_value()
#print("ip[%s] port[%s]" % (ip,port))
#print([ip],[port])
print(get_more_value())

#交换字典键和值
d = {"One": 1, "Two": 2, "Three": 3, "Four": 4, "Five": 5}
d= {k : v for v,k in d.items()}
print(d)
