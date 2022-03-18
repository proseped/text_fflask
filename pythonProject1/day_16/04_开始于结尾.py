# ^表示字符的开始
# $表示字符的结尾
# \A表示字符串开始
# \Z表示字符串结束
import re

ret = re.search("^good", "good morning!")
print(ret, ret.group())
ret = re.search("morning$", "good morning")
print(ret)
ret = re.search("^good$", "good")
print(ret)


# 输入一个字符串，判断是否为电话号码
def is_phone_num(num):
    re.search("1[3-9][0-9]{9}", num)
    return ret != None


s = input()
print(is_phone_num(s))
