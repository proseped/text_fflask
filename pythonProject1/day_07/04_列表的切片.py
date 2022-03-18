ls = ["zero","one","two","three","four","five"]
print(ls[0],ls[1])
print(ls[0:4])
print(ls[4:-1])
print(ls[2:])
print(ls[1:4:2])
print(ls[4:1:-1])
print(ls[-1],ls[-2])
print(ls[1:-1])


#切片可以直接修改列表的元素，没有个数限制
ls[2:4] = ["hello","hello","world","world","studing"]
print(ls)