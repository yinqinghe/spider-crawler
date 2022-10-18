import requests

header={
    'user-agent':'Mozilla/5.0 (Linux; Android 10; YAL-AL00 Build/HUAWEIYAL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3209 MMWEBSDK/20220204 Mobile Safari/537.36',
}

url='https://vkceyugu.cdn.bspapp.com/'
res=requests.get(url,headers=header,verify=False)
print(res.text)