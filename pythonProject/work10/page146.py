class A:
    def hello(self):
        print("Hello,I'm A")
class B(A):
    pass
a = A()
b = B()
a.hello()
b.hello()
print("===============")
class B(A):
    def hello(self):
        print("Hello,I'm B")
b = B()
b.hello()