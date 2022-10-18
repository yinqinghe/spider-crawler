import requests

url = 'https://www.huya.com/g/4769'
dic={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp=requests.get(url,headers=dic)
print(resp)
print(resp.text)
