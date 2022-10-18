import requests
import json
import os
import time
import re

"""
1.根据用户页面分享的字符串提取短url
2.根据短url加上302获取location,提取sec_id
3.拼接视频列表请求url
params = {
    'sec_uid' : 'MS4wLjABAAAAbtSlJK_BfUcuqyy8ypNouqEH7outUXePTYEcAIpY9rk',
    'count' : '200',
    'min_cursor' : '1612108800000',
    'max_cursor' : '1619251716404',
    'aid' : '1128',
    '_signature' : 'PtCNCgAAXljWCq93QOKsFT7QjR'
}
"""
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
}
# string  = '在抖音，记录美好生活！ https://v.douyin.com/ekkTsYw/'
string = input('粘贴分享链接：')

shroturl = re.findall('[a-z]+://[\S]+', string, re.I | re.M)[0]
# print(shroturl)
startpage = requests.get(url=shroturl, headers=headers, allow_redirects=False)
# print(startpage.headers)
location = startpage.headers['location']
print(location)
sec_uid = re.findall('(?<=sec_uid=)[a-z，A-Z，0-9, _, -]+', location, re.M | re.I)[0]
print(sec_uid)
getname = requests.get(url='https://www.iesdouyin.com/web/api/v2/user/info/?sec_uid={}'.format(sec_uid),
                       headers=headers).text
# print(getname)
userinfo = json.loads(getname)
name = userinfo['user_info']['nickname']
print(name)
Path = name
# if os.path.exists(path=Path) == False:
#     os.mkdir(path=Path)
# else:
#     print('directory exist')
# os.chdir(path=Path)
#
# """new function"""
# year = ('2018', '2019', '2020', '2021','2022')
# month = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
# timepool = [x + '-' + y + '-01 00:00:00' for x in year for y in month]
# print(timepool)
# k = len(timepool)
# num_i=0
# print(k)
# for i in range(k):
#     if i < k - 1:
#         # print('begintime=' + timepool[i])
#         # print('endtime=' + timepool[i + 1])
#         beginarray = time.strptime(timepool[i], "%Y-%m-%d %H:%M:%S")
#         endarray = time.strptime(timepool[i + 1], "%Y-%m-%d %H:%M:%S")
#         t1 = int(time.mktime(beginarray) * 1000)
#         t2 = int(time.mktime(endarray) * 1000)
#         # print(t1, t2)
#
#         params = {
#             'sec_uid': sec_uid,
#             'count': 200,
#             'min_cursor': t1,
#             'max_cursor': t2,
#             'aid': 1128,
#             '_signature': 'PtCNCgAAXljWCq93QOKsFT7QjR'
#         }
#         awemeurl = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?'
#         awemehtml = requests.get(url=awemeurl, params=params, headers=headers)
#         # print(url)
#         data=awemehtml.json()
#         # print(data)
#         # print(type(data))
#         awemenum = len(data['aweme_list'])
#         if awemenum==0:
#             print('null')
#         else:
#             print(data)
#             break
        #     for i in range(awemenum):
        #         videotitle = data['aweme_list'][i]['desc'].replace("?", "").replace("\"", "").replace(":", "")
        #         videourl = data['aweme_list'][i]['video']['play_addr']['url_list'][0]
        #         print(videourl)

        #         num_i=num_i+1
        #         print(videotitle)
            #     start = time.time()
            #     print('{} ===>downloading'.format(videotitle))
            #     with open(videotitle + '.mp4', 'wb') as v:
            #         try:
            #             v.write(requests.get(url=videourl, headers=headers).content)
            #             end = time.time()
            #             cost = end - start
            #             print('{} ===>downloaded ===>cost {}s'.format(videotitle, cost))
            #         except Exception as e:
            #             print('download error')
# print(num_i)