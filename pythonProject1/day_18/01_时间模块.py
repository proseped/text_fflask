import time
import calendar

x = time.localtime()
print(x)
print(x.tm_year, x.tm_mon, x.tm_mday)

print(time.asctime(x))

s = time.strftime("%Y-%m-%d %H：%M：%S", x)
print(s)

a = calendar.month(2021, 4)
print(a)
b = calendar.calendar(2021)
print(b)