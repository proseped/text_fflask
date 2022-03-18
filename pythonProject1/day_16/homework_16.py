# 判断一个输入的邮箱是否为正确的邮箱

import re


def is_email_address(s):
    pattern = '\w{1, 20}@\w{1, 10}(\.cn|\.com|\.net|\.cn\.com)'
    return re.search(pattern, s) != None


def is_email(s):
    pattern = '[0-9]{1,15}@qq\.com|\w{1,20}@(136|126|gmail)\.com'
    return re.search(pattern, s) != None


print(is_email_address("5555555@qq.com"))
print(is_email("5555555@qq.com"))
