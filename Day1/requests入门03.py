import requests
url="https://movie.douban.com/j/search_subjects"
param={
    "type": "movie",
    "tag": "热门",
    "page_limit": "50",
    "page_start":"0",
}
header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp=requests.get(url=url,params=param,headers=header)
with open("doubai.html",mode="w",encoding="gbk") as f:
    f.write(resp.text)
print(resp.request.url)
print(resp.request.headers)
print(resp.json())
resp.close()