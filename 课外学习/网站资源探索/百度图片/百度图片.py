import requests

header = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; YAL-AL00 Build/HUAWEIYAL-AL00; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/86.0.4240.99 XWEB/3209 MMWEBSDK/20220204 Mobile Safari/537.36',
}

url = 'https://image.baidu.com/search/acjson?'
def request(params):
    res = requests.get(url, headers=header, params=params).json()
    # print(res)
    data = res['data']
    print(len(data))
    arry=[]
    i=0
    for d in range(0,len(data)-1):
        arry.append([])
        item = data[d]
        hoverURL = item['hoverURL']
        # print(hoverURL)
        bdImgnewsDate = item['bdImgnewsDate']
        # print(bdImgnewsDate)
        fromPageTitleEnc = item['fromPageTitleEnc']
        # print(fromPageTitleEnc)
        pageNum=item['pageNum']
        # item.hash_key('')
        # print(pageNum)
        arry[i].append(bdImgnewsDate)
        arry[i].append(fromPageTitleEnc)
        arry[i].append(hoverURL)
        arry[i].append(pageNum)
        if 'replaceUrl' in item.keys():
            replaceUrl = item['replaceUrl']
            for r in range(0, len(replaceUrl)):
                chunk = replaceUrl[r]
                FromURL = chunk['FromURL']
                ObjURL = chunk['ObjURL']
                arry[i].append(FromURL)
                arry[i].append(ObjURL)
        else:
            print("replaceurl不存在")
        # null='null'
        while len(arry[i])!=10:
            arry[i].append(pageNum)
        print(len(arry[i]))

        i=i+1
    return arry
