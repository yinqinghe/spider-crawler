import pymysql
import re
import requests
import time
conn = pymysql.connect(host='127.0.0.1', port=3306, user='root', password='123456', database='ins',
                       charset='utf8')
# 创建游标
cursor = conn.cursor(pymysql.cursors.DictCursor)
header1={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie':'mid=YkfGHAALAAF1igAZ8-n9yf66yeyu; ig_did=CEB38969-85AD-4953-B039-F51ACDDCE4FF; ig_nrcb=1; shbid="10251\0548655111426\0541683433774:01f7bd2e9860d302adee1b909bf21c93ede5972584b2e7433ca8a719e61a2e04bc0531ac"; shbts="1651897774\0548655111426\0541683433774:01f75385a37d299f2b38b52e40509fe14fdd3f4950b12bb0babda8b149fa6157de20b31b"; dpr=1.25; datr=a8Z4YnK3a_9seA77vC9LUDp7; csrftoken=6llADXs9Zw0JbL3MlAO6gOb0MIoZOAxn; ds_user_id=52997330262; sessionid=52997330262:GDaE1fbhGPpc5P:6; rur="VLL\05452997330262\0541683939813:01f78519325a75f0d5096827dcbe0c47fc5a8d74b12af77393b120844b791eea64effe3e"',
    # 'referer':'https://www.instagram.com/',
    'x-ig-app-id': '936619743392459',

}
proxie={'http':'http://127.0.0.1:7890','https':'https://127.0.0.1:7890'}

for i in range(10, 11):  # 176    100
    num = i * 10

    sql_query_id = f"select username from username where id between 441 and 445"
    cursor.execute(sql_query_id)
    result = cursor.fetchall()  # 接收查询到的结果
    print(result)
    print(len(result))
    for r in result:
        list=[]
        username=r['username']
        url = f'https://www.instagram.com/{username}/'
        time.sleep(10)
        res=requests.get(url,proxies=proxie,headers=header1)
        ro = re.compile('<meta property="og:description" content="(?P<content>.*?)"/>')
        # print(res.text)
        roer = ro.search(res.text)
        con = roer.group('content').split(' ')
        # print(con)
        time1 = time.localtime(time.time())
        nowtime = time.strftime('%Y-%m-%d %H:%M:%S', time1)
        list.append(con[0])
        list.append(con[2])
        list.append(con[4])
        list.append(nowtime)
        list.append(username)

        print(list)
        sql_add = "insert into users_single(Followers,Following,Posts,nowtime,username) values (%s,%s,%s,%s,%s)"
        cursor.execute(sql_add,list)
        # 提交  不然无法保存
        conn.commit()

    # for rr in range(0,len(result)):
    #     # print(result[rr]['shortcode'])
    #     asyncio.run(DownLoadPics(contents=result[rr]))
    #     print('finish')


#关闭游标
cursor.close()
#关闭连接
conn.close()