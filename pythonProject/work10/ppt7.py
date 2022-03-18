class Person(object):
    def __init__(self,name,age,gender):
        self.name = name
        self.age = age
        self.gender = gender
    def eat(self,food):
        print("%s正在吃%s"%(self.name,food))
    def marry(self,pohter):
        print("%s %d %s 开车去娶 %s"%(self.name,self.age,self.gender,pohter.name))
    def work(self,place):
        print("%s %d %s去%s砍柴"%(self.name,self.age,self.gender,place))

zs = Person('张三丰',22,'男')
ts = Person('铁扇公主',24,'女')
print(zs.name,zs.age,zs.gender)
zs.eat('旺旺雪饼')
zs.marry(ts)
zs.age += 1
zs.work('火焰山')