import time


class Timer:  # 类名， 方法， 定时长， 重复次数，参数
    def __init__(self, obj, func, stepper, repeat, *arg):
        self.__obj, self.__func, self.__stepper, self.__repeat, self.__arg = obj, func, stepper, repeat, arg

    def __run(self):
        for i in range(self.__repeat):
            time.sleep(self.__stepper)
            self.__func(self.__obj, *self.__arg)

    def start(self):
        return self.__run()


class Stu:
    def __init__(self, name, arg):
        self.__name = name
        self.__arg = arg

    def speak_name(self):
        print("我是：{}{}".format(self.__name,self.__arg))


xiaoming = Stu("小明", "haha")
timer = Timer(xiaoming, Stu.speak_name, 5, 5)
timer.start()
