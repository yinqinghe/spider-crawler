import argparse
from DrissionPage import WebPage,SessionPage,SessionOptions
import  httpx
import requests
# 定义随机字符串的可选字符集
# characters = string.ascii_letters + string.digits

so=SessionOptions()
# cookies="XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; _s_tentry=weibo.com; appkey=; Apache=4602726757926.523.1656506096124; SINAGLOBAL=4602726757926.523.1656506096124; ULV=1656506096144:1:1:1:4602726757926.523.1656506096124:; WB_register_version=2022070116; login_sid_t=c602f3b69391d0bb20f099b5269dd1b7; cross_origin_proto=SSL; WBtopGlobal_register_version=2022081718; SCF=Aumg2f5Y26rzSqRY9YyhyKbNEXgg32VhSINhjFBDMr0nKaIg3LxHdfjqKZRoxK9UiStEUmrWPpw2b-VenhOAnBY.; SSOLoginState=1678416322; SUB=_2A25JDumSDeRhGeBN71UY8yrLyD6IHXVq8PfarDV8PUJbkNAGLRj4kW1NRH-6lYXWUzZZTm7UFert_bDLr_rbMw_0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW8uqDhrAfGgmST18ARPTyU5NHD95Qce0BN1KeXS0eEWs4DqcjiCJvE9s8VSo9.; UOR=,,www.suredian.com; WBPSESS=0R6t4Qf2wwe9jzS0Ncn6IAk5AfTSeXKZsq_ZnDYrAyWPvMXv46cPuuALly_B9Jo_YvoUpwZOGCI1zjlv0aGInerPP3qBhvlI3gs5XlzdJT-Xx14GKQLtIb70KE3ANHpJQehW7Rnw-THsbMT53EhSkw=="
cookies="XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; _s_tentry=weibo.com; appkey=; Apache=4602726757926.523.1656506096124; SINAGLOBAL=4602726757926.523.1656506096124; ULV=1656506096144:1:1:1:4602726757926.523.1656506096124:; WB_register_version=2022070116; login_sid_t=c602f3b69391d0bb20f099b5269dd1b7; cross_origin_proto=SSL; WBtopGlobal_register_version=2022081718; SCF=Aumg2f5Y26rzSqRY9YyhyKbNEXgg32VhSINhjFBDMr0nKaIg3LxHdfjqKZRoxK9UiStEUmrWPpw2b-VenhOAnBY.; SSOLoginState=1678416322; SUB=_2A25JDumSDeRhGeBN71UY8yrLyD6IHXVq8PfarDV8PUJbkNAGLRj4kW1NRH-6lYXWUzZZTm7UFert_bDLr_rbMw_0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW8uqDhrAfGgmST18ARPTyU5NHD95Qce0BN1KeXS0eEWs4DqcjiCJvE9s8VSo9.; UOR=,,www.suredian.com; PC_TOKEN=7e9a9ada76; WBPSESS=0R6t4Qf2wwe9jzS0Ncn6IAk5AfTSeXKZsq_ZnDYrAyWPvMXv46cPuuALly_B9Jo_gpAvyzWAk_akOCqRSpasAfEtjsr_ZlKH-LuDlaku3ObrTYvgqtwakuXW2cZkOJ2k-_Zo8WV3iWbRMzBgyR1oqg=="
so.set_cookies(cookies.split(';'))
page=SessionPage(session_or_options=so)

gif_url="https://video.weibo.com/media/play?livephoto=https%3A%2F%2Fus.sinaimg.cn%2F0035y2gwgx084F73cMGX0f0f01006vwR0k01.mov"
rename=gif_url.split('/')[-1][65:85]
print(rename)
page.download(gif_url,goal_path=fr'D:\C#\python\爬虫\New_Year_2023\weibo爬取',rename=rename,show_msg=True)

filename=r"D:\C#\python\爬虫\New_Year_2023\weibo爬取\aa.mov"
headers={"cookies":"XSRF-TOKEN=cvk-RVYhyoTZvJpXapAAgQon; _s_tentry=weibo.com; appkey=; Apache=4602726757926.523.1656506096124; SINAGLOBAL=4602726757926.523.1656506096124; ULV=1656506096144:1:1:1:4602726757926.523.1656506096124:; WB_register_version=2022070116; login_sid_t=c602f3b69391d0bb20f099b5269dd1b7; cross_origin_proto=SSL; WBtopGlobal_register_version=2022081718; SCF=Aumg2f5Y26rzSqRY9YyhyKbNEXgg32VhSINhjFBDMr0nKaIg3LxHdfjqKZRoxK9UiStEUmrWPpw2b-VenhOAnBY.; SSOLoginState=1678416322; SUB=_2A25JDumSDeRhGeBN71UY8yrLyD6IHXVq8PfarDV8PUJbkNAGLRj4kW1NRH-6lYXWUzZZTm7UFert_bDLr_rbMw_0; SUBP=0033WrSXqPxfM725Ws9jqgMF55529P9D9WW8uqDhrAfGgmST18ARPTyU5NHD95Qce0BN1KeXS0eEWs4DqcjiCJvE9s8VSo9.; UOR=,,www.suredian.com; PC_TOKEN=7e9a9ada76; WBPSESS=0R6t4Qf2wwe9jzS0Ncn6IAk5AfTSeXKZsq_ZnDYrAyWPvMXv46cPuuALly_B9Jo_gpAvyzWAk_akOCqRSpasAfEtjsr_ZlKH-LuDlaku3ObrTYvgqtwakuXW2cZkOJ2k-_Zo8WV3iWbRMzBgyR1oqg==",
         "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36",
         "Referer":"https://weibo.com/u/7743317355"
         }
res=requests.get(gif_url)
print(res)
with open(filename, "wb") as f:
    # for chunk in res:
    f.write(res.content)

# # 创建ArgumentParser对象
# parser = argparse.ArgumentParser(description='Process some integers.')
#
#
#
# parser.add_argument('-uid', type=str, help='姓')
# parser.add_argument('-u', type=str, required=True, default='', help='名')
# # 解析命令行参数
# args = parser.parse_args()
#
# # 打印结果
# print(args)
# print(args.u)
