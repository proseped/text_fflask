import re
# [ABC]表示该字符可以是ABC中任意一个
# [A-Za-z]表示该字符是范围中的任意一个
# [0-9]数字中任意一个
# [A-Za-z0-9]表示范围是标识符

ret = re.search("b[ae]d", "I am bad, I have a bed!")
print(ret)
ret = re.search("b[A-Ca-c]d", "I am bad, I have a bed!")
print(ret)
ret = re.search("[a-z][ae][a-z]", "I am bad, I have a bed!")
print(ret)

# .表示任意字符，除了空格(\n)
# \w表示所有标识字符
# \W表示所有非标识符字符
# \s表示所有不可见标识字符，列如空格
# \S表示除了上述不可见字符
ret = re.search("b.d", "I am b&d, I have a bed!")
print(ret)
ret = re.search("b\wd", "I am b d, I have a b*d!")
print(ret)
ret = re.search("b\Wd", "I am b d, I have a bed!")
print(ret)
ret = re.search("b\sd", "I am b d, I have a bed!")
print(ret)
ret = re.search("b\Sd", "I am b d, I have a b d!")
print(ret)