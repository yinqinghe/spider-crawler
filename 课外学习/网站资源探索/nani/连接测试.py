import requests


url='http://t-nani.co.kr/shop/shopdetail.html?branduid=2025494&xcode=004&mcode=001&scode=&special=1&GfDT=bGx3VA%3D%3D'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',

}

res=requests.get(url,header)

print(res.text)