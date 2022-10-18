import requests

url='https://cn-hnzz-cmcc-v-04.bilivideo.com/upgcxcode/36/01/50280136/50280136_da2-1-30080.m4s?' \
    'e=ig8euxZM2rNcNbdlhoNvNC8BqJIzNbfqXBvEqxTEto8BTrNvN0GvT90W5JZMkX_YN0MvXg8gNEV4NC8xNEV4N03eN0B5tZlqNxTEto8BTrNvNeZVuJ10Kj_g2UB02J0mN0B5tZlqNCNEto8BTrNvNC7MTX502C8f2jmMQJ6mqF2fka1mqx6gqj0eN0B599M=' \
    '&uipk=5&nbs=1&deadline=1648459092&gen=playurlv2&os=bcache&oi=3747624803&trid=00005ce4e5af7359400688ae32675940f533u' \
    '&platform=pc&upsig=1f6f28652be8f2fb05545fb7a1ab5149&uparams=e,uipk,nbs,deadline,gen,os,oi,trid,platform&cdnid=5362' \
    '&mid=0&bvc=vod&nettype=0&orderid=0,3&agrr=1&bw=365115&logo=80000000'

header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    'Origin': 'https://www.bilibili.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.bilibili.com/video/av28989880',
    'Range': 'bytes=246876-327766',
    'If-Range': "ltylGCkxilFkAESppyvHKd1ugZTg",
}
resp=requests.get(url,headers=header)
print(resp.text)
# with open('001.mp4',mode='wb') as f:
#     f.write(resp.content)