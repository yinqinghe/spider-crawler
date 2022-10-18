import requests

url='https://i.instagram.com/api/v1/friendships/8655111426/following/?count=12&max_id=12'

proxie={'http':'http://127.0.0.1:7890','https':'https://127.0.0.1:7890'}
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.54 Safari/537.36',
    'cookie': r'mid=YkfGHAALAAF1igAZ8-n9yf66yeyu; ig_did=CEB38969-85AD-4953-B039-F51ACDDCE4FF; ig_nrcb=1; csrftoken=oF7nHadJTDd4wQNtHAYFGx8oaHOWUxt0; ds_user_id=8655111426; sessionid=8655111426%3AUDawgScP6iQ057%3A28; shbid="10251\0548655111426\0541683433774:01f7bd2e9860d302adee1b909bf21c93ede5972584b2e7433ca8a719e61a2e04bc0531ac"; shbts="1651897774\0548655111426\0541683433774:01f75385a37d299f2b38b52e40509fe14fdd3f4950b12bb0babda8b149fa6157de20b31b"; rur="NAO\0548655111426\0541683434609:01f723150cca821ddc8b131eef738c9e60bfa1c392db878ce2a9ce0be938a6093f964566"',
    # 'x-asbd-id': '198387',
    # 'x-csrftoken': 'oF7nHadJTDd4wQNtHAYFGx8oaHOWUxt0',
    'x-ig-app-id': '936619743392459',
    # 'x-ig-www-claim': 'hmac.AR0Wkc6ZlHm-kqIKMYH1a2QGkHrbwhLZS2Y-wg-kRmhLKXFg',
}
res=requests.get(url,proxies=proxie,headers=header)


print(res.json())