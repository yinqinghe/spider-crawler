import execjs
import requests
from lxml import html

# etree = html.etree
# url = "https://passport.wanmei.com/sso/login?service=passport&isiframe=1&location=2f736166652f"
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
# }
# page_text = requests.get(url, headers=headers).text
# tree = etree.HTML(page_text)
# key = tree.xpath('//input[@id="e"]/@value')[0]
# print(key)
# key="MIGfMA0GCSqGSIb3DQEBAQUAA4GNADCBiQKBgQCjfeE0MIYsZes/HwV06/kvRw34Hmhn9WPt0feLPp1PVqdqZz1/xFvPPEAJ/lAvfqt5kyn+A06bvYXIhizTjlOzPgLE4897ihuSYXgfwcUshPZvydRLbftU6Exj5SLbv5tw4GInbgQv7RWLWOKyQA81q6lWae2Kcgd1XpDRsQNXVwIDAQAB"
key="1"
node = execjs.get()

ctx=node.compile(open('./wanmei.js',encoding='utf-8').read())
funcName = 'getPwd("{0}","{1}")'.format('123456',key)
pwd = ctx.eval(funcName)
print(pwd)
