def isinstring(s1:str,s2:str):
    for i in s1:
        if i not in s2:
            return False
        return True
print(isinstring("1235","0123456789"))
print(isinstring("sdjI","abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ"))

#进行整形加一判断
ret = input()
if (isinstring(ret,"0123456789")):
    print(int(ret)+1)

#二次封装
def isinnum(s:str):
    return isinstring(s,"0123456789")
def isinapah(s:str):
    return (s,"abcdefghijklmnopqrstuvwxyzABCDEFGHIGKLMNOPQRSTUVWXYZ")
