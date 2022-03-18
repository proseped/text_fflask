# 正则表达式是查找字符串，提取指定字符串片段的一种工具，可以实现字符串模糊查找
# 对解析网络数据，尤其爬虫数据有奇效

import re
ret = re.match("www", "www.baidu.com")
print(ret, ret.span(), ret.group())

ret = re.search("www", "www.baidu.com")
print(ret, ret.span(), ret.group())

ret = re.findall("\.", "www.baidu.com")
print(ret)