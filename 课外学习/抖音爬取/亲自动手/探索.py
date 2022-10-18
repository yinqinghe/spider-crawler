import json

import requests
import time

year = ('2018', '2019', '2020', '2021','2022')
month = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
timepool = [x + '-' + y + '-01 00:00:00' for x in year for y in month]
# print(timepool)
k = len(timepool)
num_i=0
# print(k)
print('begintime=' + timepool[0])
print('endtime=' + timepool[1])
beginarray = time.strptime(timepool[45], "%Y-%m-%d %H:%M:%S")
endarray = time.strptime(timepool[46], "%Y-%m-%d %H:%M:%S")
t1 = int(time.mktime(beginarray) * 1000)
t2 = int(time.mktime(endarray) * 1000)
print(t1, t2)
sec_uid='MS4wLjABAAAA2Wl_bUvtNX1OnqWHXF0SFM5_KOVbn7N3zmw8bYjfb_s'
params = {
    'sec_uid': sec_uid,
    'count': 200,
    'min_cursor': t1,
    'max_cursor': t2,
    'aid': 1128,
    '_signature': 'PtCNCgAAXljWCq93QOKsFT7QjR'
}
headers = {
    "user-agent": "Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Mobile Safari/537.36"
}
awemeurl = 'https://www.iesdouyin.com/web/api/v2/aweme/post/?'
awemehtml = requests.get(url=awemeurl, params=params, headers=headers)
# print(url)
data=awemehtml.json()
re_json=json.dumps(data)
print(type(re_json))
# print(data)
# print(type(data['aweme_list']))
# awemenum = len(data['aweme_list'])
# print(awemenum)
# list_data=data['aweme_list'][0]['video']
# print(list_data)
# for i in list_data:
#     print(i)
# for i in range(awemenum):
#     videotitle = data['aweme_list'][i]['desc'].replace("?", "").replace("\"", "").replace(":", "")
#     videourl = data['aweme_list'][i]['video']['play_addr']['url_list'][0]
#     print(videotitle)
#     print(videourl)

