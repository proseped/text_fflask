#1.进行数据传输，将【json】转换成字典格式，xml也非常类似字典格式。
#2.进行多选一操作，比if-else更加方便。

def translation(word,language):
    d = {
        "welcome": {
            "CHN":"欢迎您的使用！！",
            "ENG":"welcome to use my iteam!!",
            "BID":"飞士大夫呢！！"
        },
        "over": {
            "CHN": "期待您的下次使用！！",
            "ENG": "Tanks for using!!",
            "BID": "四大行代码v！！"
        }
    }
    return d[word][language]

creat_language = "CHN"
print(translation("welcome",creat_language))
print(translation("over",creat_language))