# | 多个字符选一,优先级最低
import re

ret = re.search("good|bad", "You are good!")
print(ret)


# python的re提供了三种模式
# re.I模式，忽略大小写模式
# re.S模式，单行模式
# re.M模式，多行模式
# 列如 .*表示任意字符串但是不能换行。但是加入re.S会忽略\n

ret = re.search("Mon|TUe|WEn|Tur|fri|Sat|Sun", "mon", re.I)
print(ret)

s = """
    <p>
        <a>sjalsl</a>
        <a>ccc</a>
    </p>
    """
ret = re.search("<P>(.*)</p>", s, re.S | re.I)
print(ret.group(1))

s = "<p<a>sjalsl</" \
    "a><a>cc" \
    "c<</p"
ret = re.search(".*", s, re.S)
print(ret)