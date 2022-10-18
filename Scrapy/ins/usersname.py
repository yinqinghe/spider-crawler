import re
import time

import requests

import pymysql
import asyncio
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='ins',
                       charset='utf8')
# 创建游标
cursor = conn.cursor(pymysql.cursors.DictCursor)
# url='https://i.instagram.com/api/v1/friendships/8655111426/following/?count=12'
url='https://i.instagram.com/api/v1/friendships/53136382080/following/?count=500&max_id=0'
# url='https://www.instagram.com/zdbzvk684/'
proxie={'http':'http://127.0.0.1:7890','https':'https://127.0.0.1:7890'}
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie': r'mid=YkfGHAALAAF1igAZ8-n9yf66yeyu; ig_did=CEB38969-85AD-4953-B039-F51ACDDCE4FF; ig_nrcb=1; csrftoken=oF7nHadJTDd4wQNtHAYFGx8oaHOWUxt0; ds_user_id=8655111426; sessionid=8655111426%3AUDawgScP6iQ057%3A28; shbid="10251\0548655111426\0541683433774:01f7bd2e9860d302adee1b909bf21c93ede5972584b2e7433ca8a719e61a2e04bc0531ac"; shbts="1651897774\0548655111426\0541683433774:01f75385a37d299f2b38b52e40509fe14fdd3f4950b12bb0babda8b149fa6157de20b31b"; rur="NAO\0548655111426\0541683434609:01f723150cca821ddc8b131eef738c9e60bfa1c392db878ce2a9ce0be938a6093f964566"',
    # 'x-asbd-id': '198387',
    # 'x-csrftoken': 'oF7nHadJTDd4wQNtHAYFGx8oaHOWUxt0',
    # 'x-ig-app-id': '936619743392459',
    # 'x-ig-www-claim': 'hmac.AR0Wkc6ZlHm-kqIKMYH1a2QGkHrbwhLZS2Y-wg-kRmhLKXFg',
}
header1={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie':r'mid=YkfGHAALAAF1igAZ8-n9yf66yeyu; ig_did=CEB38969-85AD-4953-B039-F51ACDDCE4FF; ig_nrcb=1; shbid="10251\0548655111426\0541683433774:01f7bd2e9860d302adee1b909bf21c93ede5972584b2e7433ca8a719e61a2e04bc0531ac"; shbts="1651897774\0548655111426\0541683433774:01f75385a37d299f2b38b52e40509fe14fdd3f4950b12bb0babda8b149fa6157de20b31b"; dpr=1.25; datr=a8Z4YnK3a_9seA77vC9LUDp7; csrftoken=OLfF38c6G3W2iieGGFcI97W6GKYX6xU0; ds_user_id=53136382080; sessionid=53136382080:qqr60oa8suSx4t:16; rur="VLL\05453136382080\0541683871632:01f7a161c7258b27aebed316824ce1796e715add99d73ff0310b31b255888c91e17af07b"',
    # 'referer':'https://www.instagram.com/',
    'x-ig-app-id': '936619743392459',

}
res=requests.get(url,proxies=proxie,headers=header1)

# print(res.text)
res=res.json()
print(res)
us=res['users']
print(len(us))
sql_add1="insert into username(username,nowtime) values  (%s,%s)"
time1 = time.localtime(time.time())
ti = time.strftime('%Y-%m-%d %H:%M:%S', time1)
for i in range(0,len(res['users'])):
        name=us[i]['username']
        cursor.execute(sql_add1,[name,ti])

#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()

# re_js=res.json()
# print(len(re_js['users']))
# ro = re.compile('<meta property="og:description" content="(?P<content>.*?)"/>')
# roer = ro.search(res.text)
# print(roer.group('content'))
# con=roer.group('content').split(' ')
# # Followers = con.split(' ')
# print(con)

