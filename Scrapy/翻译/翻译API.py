import requests
import time


ti=time.time()
print(int(ti))
ti=int(ti)
url=f'https://tmt.tencentcloudapi.com/?Action=TextTranslate&ProjectId=0&Source=en&SourceText=hello&Target=zh&Region=ap-beijing&Version=2018-03-21&Timestamp={ti}&Nonce=6494' \
    f'&SecretId=AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK&Signature=0fb3acd3d456f97147570c66c141b861dbe84568dc30bae2a9c49996e74d2128'
# url=f'https://tmt.tencentcloudapi.com/post?'
# url='https://tmt.tencentcloudapi.com/?Action=TextTranslate&Nonce=5866&ProjectId=0&Region=ap-hongkong&SecretId=AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK&SignatureMethod=HmacSHA256&Source=en&SourceText=hello world&Target=zh&Timestamp=1652796795&Version=2018-03-21&Signature=CtN79cNKqud4Ljh4xbZZb3GIBPvVJKMoeKGeEfOMaq8%3D'
data={
    'Action':'TextTranslate',
    'Source': 'en',
    'SourceText': 'hello',
    'Region': 'ap-beijing',
    'Timestamp': f'{ti}',
    'Nonce': '6494',
    'SecretId': 'AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK',
    'Signature': '0fb3acd3d456f97147570c66c141b861dbe84568dc30bae2a9c49996e74d2128',
    'Version': '2018-03-21',

}
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',

}
# res=requests.post(url,data=data,headers=header)
res=requests.get(url)
print(res.request.headers)
print(res.text)