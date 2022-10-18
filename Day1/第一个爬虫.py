from urllib.request import urlopen
url='https://www.52pojie.cn/'
resp=urlopen(url)


# print(resp.read().decode("utf-8"))
with open("mybaidu.html",mode="w") as f:
    f.write(resp.read().decode("gbk"))
print("binggo")