import requests

session=requests.session()
data={
    "loginName":"18536384331",
    "password":"@Y18536384331"
}
url="https://passport.17k.com/ck/user/login"
resp=session.post(url,data=data)
resp.encoding="utf-8"
# print(resp.text)
# print(resp.cookies)


resp=session.get('https://user.17k.com/ck/author/shelf?page=1&appKey=2406394919')
print(resp.json())
resp.close()