#判断闰年
years = int(input('请输入年份：'))
if (years % 4 ==0 and years % 100 != 0) or (years % 400 == 0):
    print(years,'是闰年')
else:
    print(years,'不是闰年')
