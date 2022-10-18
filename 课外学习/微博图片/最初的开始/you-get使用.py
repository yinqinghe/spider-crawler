import you_get
import os
url="https://www.bilibili.com/video/BV1jZ4y1C79z"
os.system(r"you-get -i " + url)#在命令行里执行命令
# out=("you-get -i"+url)
# print(out)
# you_get --info url
you_get.main()
