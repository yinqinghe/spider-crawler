import requests
import execjs

url="https://store.steampowered.com/login/getrsakey/"
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36'
}
data={
    'donotcache': '1642560848164',
    'username': '123@qq.com'
}
response_json=requests.post(url,headers=headers,data=data).json()
mod=response_json['publickey_mod']
exp=response_json['publickey_exp']
print(mod,exp)
node=execjs.get()
ctx=node.compile(open('./steam.js',encoding='utf-8').read())

funcName='getPwd("{0}","{1}","{2}")'.format('123456',mod,exp)
pwd=ctx.eval(funcName)

print(pwd)