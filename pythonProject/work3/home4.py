mylist = ['jack','tom','rose','mike']
print(mylist[0],'抱歉，你已被删除')
print(mylist[3],'抱歉，你已被删除')
mylist.remove("jack")
mylist.pop()

for x in mylist:
    print(x)