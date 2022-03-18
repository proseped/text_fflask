people = {
    'Alice': {
        'phone': '2341',
        'addr': 'ftp.192.168.158.92'
    },

   'Cecil': {
        'phone': '2341',
        'addr': 'Bar street 42'
    },

    'Beth': {
        'phone': '1588',
        'addr': 'www.baidu.com'
    }
}

#用电话号码和地址的描述性标签，供打印输出时使用
labels ={
    'phone': 'phone number',
    'addr':'address'
}

name = input('Name:')

request = input('Phone number(p) or address(a)?')

#使用正确的键:
key = request#如果key既不是'p'也不是'a'
if request == 'p' : key ='phone'
if request == 'a' : key ='addr'

#使用get提供默认值
person = people.get(name,{})
label = labels.get(key,key)
result = person.get(key ,'not available')

print("{}'s {} is {}.".format(name,label,result))