#. 输入三角形三边长，判断是否构成三角形。如果能构成三角形，打印输入是正三角形、等腰三角形、直角三角形、还是等腰直角三角形。
a,b,c = eval((input('请输入边长(用逗号隔开)：')))
if a + b < c or a + c < b or b + c < a :
    print('不构成三角形，请在次输入！')
else :
    if a == b and b == c and a == c :
        print('正三角形')
    elif a == b or b == c or a == c :
        print('等腰三角形')
    elif a*a + b*b == c*c or a*a + c*c == b*b or c*c + b*b == a*a :
        print('直角三角形')
    elif (a*a + b*b == c*c and a ==b) or (a*a + c*c == b*b and a == c) or (c*c + b*b == a*a and b == c) :
        print('等腰直角三角形')
    else :
        print('普通三角形')