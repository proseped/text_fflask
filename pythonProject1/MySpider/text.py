import requests
path = "view-source:https://movie.douban.com/subject/1794171/"
ret = requests.get(path)
print(ret.content.decode("utf-8"))