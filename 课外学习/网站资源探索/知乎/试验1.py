import requests
import execjs
import hashlib

s = requests.Session()

url = "/api/v4/questions/278922791/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=5&platform=desktop&sort_by=default"

f = "+".join(["101_3_2.0", url, '"ACAV1v76ZRKPTtjEVrUBNTAHTuOeLV43NIw=|1608861437"'])

fmd5 = hashlib.new('md5', f.encode()).hexdigest()

with open('zhihu.js', 'r') as f:
    ctx1 = execjs.compile(f.read(), cwd=r'C:\Windows\System32\node_modules')
encrypt_str = ctx1.call('b', fmd5)
print(encrypt_str)
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_4) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36",
    'cookie':'_zap=c51c6e33-0a23-4bca-996b-af02643781c1; d_c0="ACAV1v76ZRKPTtjEVrUBNTAHTuOeLV43NIw=|1608861437"; __snaker__id=nnkq3zskwtGGk88v; _9755xjdesxxd_=32; YD00517437729195%3AWM_TID=yi%2FmDDbgQiZAUEFFAAcq1LjU1MATAiYV; _xsrf=4f3754ad-0fd2-4dd9-a8e9-97faece6f657; gdxidpyhxdE=Caw9OTuo9bEZcp3c3EwVWlbq2hHna6LrPJYbpC8W6WV%2BNKYDQr1O9abr6L659U3XVhn3jeWJkqrRZyppIHkBNIAvmndUOj6jIQdjJ4qSLhU4hRNKTkz%2BN1GHi8u1d2GXMmNKUCHk8phHAnQye75QaLPPlRIXN6KxqQVK6MLtMfur1Ld1%3A1648604612374; YD00517437729195%3AWM_NI=Uiv8mXhe%2Fx0ZKg9drPo%2FJqbEETJM8%2BODlprk21L%2F2%2F9zmuYCOkjb7aI2ajZijt9jILRyG9U6l8rL9exGIiBlibLrhkIMLM0bXisBNApXsPkMFZd5qGo%2BoemwFhOWZ4aVODU%3D; YD00517437729195%3AWM_NIKE=9ca17ae2e6ffcda170e2e6ee98e564f5e7e1a2ea7cad968ba2c15f839f8fbab625f5918e82ce3e8e8da6d7f52af0fea7c3b92a97b7bad9f054acbbe199b35289b9f785f15cadf18692e14f878c86aebb218d9ca491f161f2ef84d0b125fba6a396dc498db5a683b66b8beeaf8bd963aaacf78bcc4892a789dad83eb0e8beadbc6fbc99878ac168abbe8493eb618b9384aeb36a9cb7bda3cd4bb488bdb1ea478686acd6f44dadf5a186f07d86b881b8d940a38a81a5d837e2a3; captcha_session_v2=2|1:0|10:1648603690|18:captcha_session_v2|88:Zlo0dURwNjc0VTZJUGdMVUF6UFc1L3YxUGZRRllQSzI5RzJwUU1aUlFQSHFrTjhQVEt3QjlZdWxNdTNwSFlwaw==|282fed304571dcc494d4a7775baff1e94e594763216675db5d2eb484bad131c0; captcha_ticket_v2=2|1:0|10:1648603716|17:captcha_ticket_v2|704:eyJ2YWxpZGF0ZSI6IkNOMzFfV2tEZVA2dG51WlFVWVlYVWRhWjlJSzBhVDhwaVNxMWl1RnJyeDZsdEt5aEpxaS1ZVWpXMGcwZVNfaXlhNDhmUjZnUEZTTUN1bTlxWkhMcmJGTEpXaWtvUTJWR3JTRF9TSzY5aVpxR19mRTRaSkttZERmR2lHQmdBVmpDWUY1V21QZWxzazE2SzdDa2RLTmw4aFpVWkZEOGloelViNEhpa3Q4b0dvTUkuaEpsWHU0N21raUZVaEZsS0xMNE91THJYR0d3cFhaTkFObzk2eC5VVkZXc3NBb1ZhY3JNTHBBaW1yelVzbTk2N094X2ZxMFZoLmoweVB2TEhtcVB1eG1fY2xZZllTeVRJNGNXX01lYVU0VDRfbFliS1A4dkpDbndMWnVYbV85SFE4RVZ4VXNpbWd4b1puOWt3VURJaXRIZ1FraTBPZHNwWkdicUpIWjJNempUd2hzTkpNMjlvMWlNOFYuZG8tbTlCeVZwOTZrcnB0SUh0ZXBKU0ExUXBVQmtOdkpVTmtWUVFPS1hHeEgwenNPdVRoN1FJdkI1QWw1ZktkT2thLXltUm92S2x3RzgxUWNZYnlwNklEbW90V1VhckI2YnM0TlhBeVJINXF6NUItbW13MEtmQ3hzWGlTMnpTQUxCU20yZEEuaWc4Z1ZPR2Qybkl4bnNYbzV6MyJ9|9b3227e167a686f01b68e52aba1770a9413734835b88604ca93f7b91f514f748; o_act=login; ref_source=other_https://www.zhihu.com/signin?next=/; l_n_c=1; l_cap_id="ZTI4NDIxODM4M2FjNGU2M2IzNzYyNzM2NzgyMTg5NGI=|1648603764|e84a0322ab43e06e97378c6228c9f1f677769d99"; r_cap_id="Yzg2YWJkMzFmMDM4NDgxMWE2ODZhOTdhZGQxMjI2MjY=|1648603764|5d33898572970b98791a42a3c44ae6f971c59f87"; cap_id="M2YwMmIzNjM0ZGQ5NDVmYjhjNjU0YTVmMTU5NTFjM2I=|1648603764|b26dc1da29150a3627ba18e40dfce5925d29cbac"; n_c=1; expire_in=15552000; z_c0=2|1:0|10:1648603781|4:z_c0|92:Mi4xVUcySERBQUFBQUFBSUJYV192cGxFaGNBQUFCZ0FsVk5oUUF4WXdDRVFhcFhsNDV6S3RTNEl3YmVHUmpNdmQwZ0lR|987948bbed4a35a7bb5cbb06a0db3091bf639294ed0604c2cbf3cfcc37cc6ef2; q_c1=ac33c0ababe749fb84e01fa9c6b0f239|1648603782000|1648603782000; tst=h; Hm_lvt_98beee57fd2ef70ccdd5ca52b9740c49=1649311533; SESSIONID=KETrF57NkdoaeHQcwjkUcWSGt2RfUDrR3SjUQJd6rBo; osd=V1gUBE4ZOIhCF9KUKBtt3ggQK_Q-V3zaMlHiomByWeYlcJrASrk82SIS1pMsClDwN-IKdxkSuVuuJLrzWXPBcMU=; JOID=VFsQAUsaO4xHEtGXLB5o3QsULvE9VHjfN1LhpmV3WuUhdZ_DSb053CER0pYpCVP0MucJdB0XvFitIL_2WnDFdcA=; NOT_UNREGISTER_WAITING=1; Hm_lpvt_98beee57fd2ef70ccdd5ca52b9740c49=1649809466; KLBRSID=ed2ad9934af8a1f80db52dcb08d13344|1649809479|1649809312',

    # "x-api-version": "3.0.91",
    "x-zse-93": "101_3_2.0",
    "x-zse-96": "2.0_%s" % encrypt_str,
}
# print(headers)

r = s.get("https://www.zhihu.com" + url, headers=headers)
print(r.text)
