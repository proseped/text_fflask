while True:
    try:
        i = int(input())
        print(5 / i)  # 解释器无法处理这个操作，就会抛出一个异常

    except ZeroDivisionError as e:  # 监听并捕获异常，如果捕获到异常，就会执行下面的代码
        print("除数为零，请重新输入！", e)  # 捕获异常，给它一个引用e,打印出错误的地方
    except ValueError:
        print("传入的不是数字！")
    finally:
        print("无论对错，都执行")

