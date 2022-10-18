import requests

url='https://fanyi.qq.com/api/translate'
headers={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.88 Safari/537.36',
'Cookie': 'RK=Yfboa75XMb; ptcz=7352e81f3c4981fd2686c19cc04746029239b2914718be0496f3740c07293dc0; pgv_pvid=7584648572; o_cookie=987746808; pac_uid=1_987746808; tvfe_boss_uuid=525e1f166e2765a6; AMCV_248F210755B762187F000101%40AdobeOrg=-1712354808%7CMCIDTS%7C18737%7CMCMID%7C40697895736740892801300024882196339242%7CMCAAMLH-1619414521%7C11%7CMCAAMB-1619414521%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1618816921s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C4.3.0; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%2217cd546b5489a7-0d5f1881bd9c42-57b193e-1327104-17cd546b549b4f%22%2C%22first_id%22%3A%22%22%2C%22props%22%3A%7B%22%24latest_traffic_source_type%22%3A%22%E5%BC%95%E8%8D%90%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC%22%2C%22%24latest_referrer%22%3A%22https%3A%2F%2Fwww.yoozhibo.com%2F%22%7D%2C%22%24device_id%22%3A%2217cd546b5489a7-0d5f1881bd9c42-57b193e-1327104-17cd546b549b4f%22%7D; sd_userid=38181637038529568; sd_cookie_crttime=1637038529568; _qpsvr_localtk=0.29756169088417006; pgv_info=ssid=s2646578892; pvpqqcomrouteLine=a20220120hnztz; tokenParams=%3FADTAG%3Dmedia.buy.baidubrand.title; eas_sid=F1o6A4A4x6X4j3G7M8G362V8i5; fqm_sessionid=b979a08f-594a-4e44-9d3b-39783938e01b; fqm_pvqid=51f3b8ba-2872-4d06-b6f0-e7cf16c9be6d; tmeLoginType=2; euin=NKcl7ivsNenF; video_omgid=09b3a32d9ca9e2af; vversion_name=8.2.95; qqmusic_fromtag=66; fy_guid=394e870c-d2f9-45e4-a091-6d688db27dd9; ADHOC_MEMBERSHIP_CLIENT_ID1.0=338e452e-bd9d-836e-2203-beeccc370eeb; gr_user_id=96b21773-d807-493c-a994-7dddeba152d5; login_type=1; wxopenid=; wxrefresh_token=; wxunionid=; psrf_qqunionid=B5C03AA3F5543A7A7DCC116982BD8A92; psrf_qqaccess_token=9C5088751065C3E46756D67ECC8F8E1D; psrf_access_token_expiresAt=1657072411; psrf_qqrefresh_token=E9FA18DCA003D1307C10A662BE6EC03C; psrf_qqopenid=29E6102E824D13C45C498938F12AC76E; uin=o0987746808; skey=@oRB6xgkoX; luin=o0987746808; lskey=00010000c02e96dc0bf4b98537f2f73ce1371442b70e1db35da13b6aaf281f60503a2a81e6dd27b47624763b; rv2=809128C3F8886F06911CEECD6890C543F1AD35439236FE20D4; property20=CF4975D2A4AF5F984E88E210680533F997473A9DB269FD11A56C746B9532E6FEB04C63781813DB1A; openCount=3; qtv=813f920be541fe25; qtk=e3S9f2X7RmhWBn9xXp6esVgniAoX5YkLxB2UBer6wEzXJCY0P8S6NQLkw47fDTQjWZEwyUAYADBOtAlKD9oQhBiEADJ+4CcLjrnbetIZspnpdWwgVQ4+uYLYa3GzwOzDtZJ7qOCm+j32CPVmE17H5A==; 8507d3409e6fad23_gr_session_id=9dc308db-7d66-4924-a5c1-d7bcdf431ae8; 8507d3409e6fad23_gr_session_id_9dc308db-7d66-4924-a5c1-d7bcdf431ae8=true',
}
data={
'source': 'auto',
'target': 'zh',
'sourceText': '펜트하우스원피스',
'qtv': '813f920be541fe15',
'qtk': 'e3S9f2X7RmhWBn9xXp6esVgniAoX5YkLxB2UBer6wEzXJCY0P8S6NQLkw47fDTQjWZEwyUAYADBOtAlKD9oQhBiEADJ+4CcLjrnbetIZspnpdWwgVQ4+uYLYa3GzwOzDtZJ7qOCm+j32CPVmE17H5A==',
'ticket': '',
'randstr': '',
'sessionUuid': 'translate_uuid1650257560442',
}

res=requests.post(url,data=data,headers=headers)
print(res.text)