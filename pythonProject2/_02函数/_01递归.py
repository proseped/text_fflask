# 找出n 和n-1的关系，加上最后一项
# 打印五个hello world
# def print_hello_word(n):
#     if n == 0:
#         return
#     print_hello_word(n-1)
#     print("hello world")
# print_hello_word(5)


# 1加到100的和
def count(n):
    if n == 1:
        return 1
    return count(n-1) + n


print(count(100))



