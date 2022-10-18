import re

import requests

# url='https://www.instagram.com/graphql/query/?query_hash=69cba40317214236af40e7efa697781d&variables={"id":"1336020390","first":12,"after":"QVFBMVI0dm4wNTE0UzRXTzQzQWlUSVRQUV9YOUx0MGxTaUQ5X1dPMVZHWmF2R2tuMGg5bWw3Y0ZqaDJPbVhHMlAyZ0EtVzNEMFE5UVYyajdzcnB2TmEwdA=="}'
# url='https://www.instagram.com/graphql/query/?query_hash=69cba40317214236af40e7efa697781d&variables={"id":"42870282089","first":12,"after":"QVFCVEtuZ1JJV0hhQ2FTR3lMbWRjSzFCUTkyRWtRVFVMLUdDY0xiWmNvRXJXaThZRlB3MGdZUWozR05SZXJLd0NDY1VVMTBTRWxrNjA5eG9RMTFUaTBsbQ=="}'

# url='https://i.instagram.com/api/v1/friendships/8655111426/following/?count=12'
# url='https://i.instagram.com/api/v1/friendships/36576750804/following/?count=50&max_id=0'
# url='https://www.instagram.com/zdbzvk684/'
url='https://i.instagram.com/api/v1/users/7719696/info/'
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
    # 'cookie':r'mid=YkfGHAALAAF1igAZ8-n9yf66yeyu; ig_did=CEB38969-85AD-4953-B039-F51ACDDCE4FF; ig_nrcb=1; shbid="10251\0548655111426\0541683433774:01f7bd2e9860d302adee1b909bf21c93ede5972584b2e7433ca8a719e61a2e04bc0531ac"; shbts="1651897774\0548655111426\0541683433774:01f75385a37d299f2b38b52e40509fe14fdd3f4950b12bb0babda8b149fa6157de20b31b"; dpr=1.25; datr=a8Z4YnK3a_9seA77vC9LUDp7; csrftoken=OLfF38c6G3W2iieGGFcI97W6GKYX6xU0; ds_user_id=53136382080; sessionid=53136382080:qqr60oa8suSx4t:16; rur="VLL\05453136382080\0541683871632:01f7a161c7258b27aebed316824ce1796e715add99d73ff0310b31b255888c91e17af07b"',
    'cookie':'mid=YkfGHAALAAF1igAZ8-n9yf66yeyu; ig_did=CEB38969-85AD-4953-B039-F51ACDDCE4FF; ig_nrcb=1; shbid="10251\0548655111426\0541683433774:01f7bd2e9860d302adee1b909bf21c93ede5972584b2e7433ca8a719e61a2e04bc0531ac"; shbts="1651897774\0548655111426\0541683433774:01f75385a37d299f2b38b52e40509fe14fdd3f4950b12bb0babda8b149fa6157de20b31b"; dpr=1.25; datr=a8Z4YnK3a_9seA77vC9LUDp7; csrftoken=6llADXs9Zw0JbL3MlAO6gOb0MIoZOAxn; ds_user_id=52997330262; sessionid=52997330262:GDaE1fbhGPpc5P:6; rur="VLL\05452997330262\0541683939765:01f7c51ad136162e1df48234ca0603b9de768fceb76de9e89c81d667bfbcfad27ce6ee21"',
    # 'referer':'https://www.instagram.com/',
    'x-ig-app-id': '936619743392459',

}
res=requests.get(url,proxies=proxie,headers=header1)

# print(res.text)
res=res.json()
print(res)
# print(len(res['users']))



# re_js=res.json()
# print(len(re_js['users']))
# ro = re.compile('<meta property="og:description" content="(?P<content>.*?)"/>')
# roer = ro.search(res.text)
# print(roer.group('content'))
# con=roer.group('content').split(' ')
# # Followers = con.split(' ')
# print(con)

