#一个将人名用作键的字典。每个人都用一个字典表示
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
if request == 'p' : key ='phone'
if request == 'a' : key ='addr'

#仅当名字是字典包含的键时才打印信息:
if name in people: print("{}'s {} is {}.".format(name,labels[key],people[name][key]))
