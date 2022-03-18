import format_print

class Student:
    def __init__(self, name, age, score):
        self.__name = name
        self.__age = age
        self.__score = score

    @property
    def name(self):
        return self.__name

    def __repr__(self):
        return "姓名:{}\n年龄:{}\n成绩:{}".format(self.__name, self.__age, self.__score)


class StudentManager(format_print.FormatPrintDelegate):
    def __init__(self):
        self.__list = []
        names = ["张三", "李四", "王五", "赵六", "朱七"]
        for name in names:
            self.__list.append(Student(name, 15, 95))

    def show_students(self):
        fp = format_print.FormatPrint()
        fp.print_data(self)

    # 重写，返回数据量
    def get_nums(self):
        return len(self.__list)

    # 重写返回，每一行的内容
    def get_line_content(self, line):
        return self.__list[line]

    def get_line_title(self, line):
        return self.__list[line].name

    def get_title(self):
        return "学生列表"


s = StudentManager()
s.show_students()
