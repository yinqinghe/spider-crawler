import requests

url='https://cdn.sex.com/images/pinporn/2022/03/10/26848771.gif?width=300'

header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # 'cookie': '__auc=311b8f9817fe9b4c42dd78f3bb6; _ga=GA1.2.342629658.1648893413; _gid=GA1.2.1301796258.1648893413; _pk_id.1.bca8=d3f2cbe0cfb077b2.1648893413.; __asc=96c4001e17fe9e97af2218fd649; _pk_ref.1.bca8=%5B%22%22%2C%22%22%2C1648896867%2C%22https%3A%2F%2Ftheporndude.com%2F%22%5D; _pk_ses.1.bca8=1',
    'referer': 'https://www.sex.com/',

}

res=requests.get(url,headers=header)

with open('3.gif',mode='wb') as f:
    f.write(res.content)
print(res.status_code)