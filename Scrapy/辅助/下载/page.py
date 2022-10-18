import json
import re
import requests

url='https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_article&token=MS4wLjABAAAAzWKMSpUD00qeyjBtAm5-sIDbF2MCDpJD1C5EyzgAcSNs5Tot4WamsjJlPYOKtVYh&max_behot_time=1633655016739&aid=24&app_name=toutiao_web'
header = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    # 'cookie':'tt_webid=7081250641512121870; ttcid=84b17e80b7e341c4aae41e92d97d65ea36; s_v_web_id=verify_l29nfh0y_B5Acau7h_wXEr_4c98_9DkI_jHq7AndlRNji; local_city_cache=; csrftoken=b4b36a61f1f11a200cb8426558f3efcb; _tea_utm_cache_24=undefined; passport_csrf_token=3e05b9ccb777243cf9d3dd12d7e64295; passport_csrf_token_default=3e05b9ccb777243cf9d3dd12d7e64295; ttwid=1|MJCfWonzOscnfKFlhveST6Oo46EA-dE99S1AFMqdkzc|1650584732|49ba681ef6a1555154bd74e2672c992d64c74ecd5ee7e839422fe598c0f66957; MONITOR_WEB_ID=d1833ac6-3ef1-4d38-a5be-ba5e4fe2688d; tt_scid=43dyg5XsN1lWcHtb5nGXvmowP-s56G2IhD0SNTy8HzXuPq4iyQu9bAtVqOwhTVau7a3f',
    # 'cookie':'tt_webid%3D7081250641512121870%3B%20ttcid%3D84b17e80b7e341c4aae41e92d97d65ea36%3B%20s_v_web_id%3Dverify_l29nfh0y_B5Acau7h_wXEr_4c98_9DkI_jHq7AndlRNji%3B%20local_city_cache%3D%E5%8C%97%E4%BA%AC%3B%20csrftoken%3Db4b36a61f1f11a200cb8426558f3efcb%3B%20_tea_utm_cache_24%3Dundefined%3B%20passport_csrf_token%3D3e05b9ccb777243cf9d3dd12d7e64295%3B%20passport_csrf_token_default%3D3e05b9ccb777243cf9d3dd12d7e64295%3B%20ttwid%3D1%7CMJCfWonzOscnfKFlhveST6Oo46EA-dE99S1AFMqdkzc%7C1650584732%7C49ba681ef6a1555154bd74e2672c992d64c74ecd5ee7e839422fe598c0f66957%3B%20MONITOR_WEB_ID%3Dd1833ac6-3ef1-4d38-a5be-ba5e4fe2688d%3B%20tt_scid%3D43dyg5XsN1lWcHtb5nGXvmowP-s56G2IhD0SNTy8HzXuPq4iyQu9bAtVqOwhTVau7a3f',
    # 'cookie':'tt_webid=7081250641512121870;%20ttcid=84b17e80b7e341c4aae41e92d97d65ea36;%20s_v_web_id=verify_l29nfh0y_B5Acau7h_wXEr_4c98_9DkI_jHq7AndlRNji;%20local_city_cache=%E5%8C%97%E4%BA%AC;%20csrftoken=b4b36a61f1f11a200cb8426558f3efcb;%20_tea_utm_cache_24=undefined;%20passport_csrf_token=3e05b9ccb777243cf9d3dd12d7e64295;%20passport_csrf_token_default=3e05b9ccb777243cf9d3dd12d7e64295;%20ttwid=1%7CMJCfWonzOscnfKFlhveST6Oo46EA-dE99S1AFMqdkzc%7C1650584732%7C49ba681ef6a1555154bd74e2672c992d64c74ecd5ee7e839422fe598c0f66957;%20MONITOR_WEB_ID=d1833ac6-3ef1-4d38-a5be-ba5e4fe2688d;%20tt_scid=43dyg5XsN1lWcHtb5nGXvmowP-s56G2IhD0SNTy8HzXuPq4iyQu9bAtVqOwhTVau7a3f',
    'cookie':'tt_webid=7081250641512121870; ttcid=84b17e80b7e341c4aae41e92d97d65ea36; s_v_web_id=verify_l29nfh0y_B5Acau7h_wXEr_4c98_9DkI_jHq7AndlRNji; local_city_cache=%E5%8C%97%E4%BA%AC; csrftoken=b4b36a61f1f11a200cb8426558f3efcb; _tea_utm_cache_24=undefined; passport_csrf_token=3e05b9ccb777243cf9d3dd12d7e64295; passport_csrf_token_default=3e05b9ccb777243cf9d3dd12d7e64295; tt_scid=YSxOL7ZK-5JOcBH07gtkgFA9vXPmEg3YwSij554uk0S-h.6Kvwi3HucflBvF0kkm35cb; ttwid=1%7CMJCfWonzOscnfKFlhveST6Oo46EA-dE99S1AFMqdkzc%7C1650585580%7Caada01f93c5761e2f8a6b45aa98a6e66e8d9df1e7a84eb4791f996c95437c768; MONITOR_WEB_ID=d1833ac6-3ef1-4d38-a5be-ba5e4fe2688d',
'Referer': 'https://www.toutiao.com/c/user/token/MS4wLjABAAAAzWKMSpUD00qeyjBtAm5-sIDbF2MCDpJD1C5EyzgAcSNs5Tot4WamsjJlPYOKtVYh/?source=tuwen_detail&log_from=7ce90bb166a0a_1650584565745&tab=article',
}
res=requests.get(url,headers=header).json()
# print(res)
# print(url)
# res=res.split('(')[1].split(')')[0]
list=res['data']
print(list)
print(len(list))