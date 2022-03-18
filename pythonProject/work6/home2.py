days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
day = int(input('Day(1-7):'))
day_name = days[day-1]
if day > 7 or day < 0:
    print("输入错误！")
else:
    print(day_name)


