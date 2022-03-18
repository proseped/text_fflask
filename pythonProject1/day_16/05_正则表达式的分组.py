import re


ret = re.search("\[(([0-9]{3,4})-([0-9]{8}))\]", "[0712-85334567]")
print(ret)
print(ret.group())
print(ret.group(0))
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))

# 分组原则
# 1.由外而内，由左而右
# 2.最外一层自动为group(0)

# 非捕获性分组
pattern = "(?:.+省)(.+市)(.+区)(.*)"
ret = re.search(pattern, "湖北省武汉市江夏区光谷大道")
print(ret.group(1))
print(ret.group(2))
print(ret.group(3))
# print(ret.group(4))

# 给分组加标题
pattern = "(?P<省>.+省)(?P<市>.+市)(?P<区>.+区)(?P<详细地址>.*)"
ret = re.search(pattern, "湖北省武汉市江夏区光谷大道")
print(ret.group("省"))
print(ret.group("市"))









