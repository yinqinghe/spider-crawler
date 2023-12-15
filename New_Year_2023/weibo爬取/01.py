cookies="XSRF-TOKEN=HFVN75npxEc6HCEJfTLJ0CmJ; SSOLoginState=1678761231; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WFRkM7ofXBqTSG-KTYyorpe5JpX5KMhUgL.FoMNSo.01Kq4She2dJLoI7pSIg_LIJvE9s8Vehzt; ALF=1682307943; SCF=AspUIZKFp_dZvFulvONf1yrz8X5_NrEbOusV9VJkBZ8XUPTR7f71U2A8Z71jGcIOUJxlmwLpKAxd7uAThGgavBc.; SUB=_2A25JGh44DeRhGeFJ7VsS-SjFzz-IHXVqbgjwrDV8PUNbmtAGLUz6kW9Nf1XPsYCjtCUcPwJXKdezpylrqIyqI1Hh; _s_tentry=www.weibo.com; Apache=5110636533571.143.1679715960822; SINAGLOBAL=5110636533571.143.1679715960822; ULV=1679715960907:1:1:1:5110636533571.143.1679715960822:; WBPSESS=DQswqYJs0y3GED0LZ7HfbTR1Mj06ey6K7vktgXD4vvvVsZUvYx-3oqHJUkE1hTTlbzDsdcs9XAipWb8v3RhZoFLDfidhGAbADwM5K56S76a-UP-DJJ_XY1ztRYI00Dq62UqzEkdmtwa-K9yw-TtdDA==; PC_TOKEN=11ace3c08a"
import string
import random
# print(cookies.split(';'))

# url='https://wx1.sinaimg.cn/large/008s2azpgy1hapg9ylmylj30zo1rfnpd.jpg'
url='http://f.video.weibocdn.com/o0/pHgfqR0Alx082PE8Yl6U01041200cff90E010.mp4?label=mp4_1080p&template=1080x1920.24.0&media_id=4864696105500693&tp=8x8A3El:YTkl0eM8&us=0&ori=1&bf=4&ot=v&lp=000017785p&ps=mZ6WB&uid=8tNB3V&ab=9298-g4,8224-g0,7397-g1,8012-g2,3601-g32,8143-g0,8013-g0,7598-g0&Expires=1679730535&ssig=yxYTFo6Z6o&KID=unistore,video'
url=url.split('/')[-1]
print(url[14:24])


# 定义随机字符串的长度
length = 8

# 定义随机字符串的可选字符集
characters = string.ascii_letters + string.digits

# 生成随机字符串
random_string = ''.join(random.choices(characters, k=length))

print(random_string)

for i in range(10,19):
    print(i)