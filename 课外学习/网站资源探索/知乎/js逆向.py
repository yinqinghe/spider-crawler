import execjs
import hashlib

# d
str_to_md5 = '101_3_2.0+/api/v4/questions/278922791/answers?include=data%5B%2A%5D.is_normal%2Cadmin_closed_comment%2Creward_info%2Cis_collapsed%2Cannotation_action%2Cannotation_detail%2Ccollapse_reason%2Cis_sticky%2Ccollapsed_by%2Csuggest_edit%2Ccomment_count%2Ccan_comment%2Ccontent%2Ceditable_content%2Cattachment%2Cvoteup_count%2Creshipment_settings%2Ccomment_permission%2Ccreated_time%2Cupdated_time%2Creview_info%2Crelevant_info%2Cquestion%2Cexcerpt%2Cis_labeled%2Cpaid_info%2Cpaid_info_content%2Creaction_instruction%2Crelationship.is_authorized%2Cis_author%2Cvoting%2Cis_thanked%2Cis_nothelp%2Cis_recognized%3Bdata%5B%2A%5D.mark_infos%5B%2A%5D.url%3Bdata%5B%2A%5D.author.follower_count%2Cvip_info%2Cbadge%5B%2A%5D.topics%3Bdata%5B%2A%5D.settings.table_of_content.enabled&limit=5&offset=5&platform=desktop&sort_by=default+"ACAV1v76ZRKPTtjEVrUBNTAHTuOeLV43NIw=|1608861437"+3_2.0ae3TnRUTEvOOUCNMTQnTSHUZo02p-HNMZBO8YD_qo6Ppb7tqXRFZQi90-LS9-hp1DufI-we8gGHPgJO1xuPZ0GxCTJHR7820XM20cLRGDJXfgGCBxupMuD_Ie8FL7AtqM6O1VDQyQ6nxrRPCHukMoCXBEgOsiRP0XL2ZUBXmDDV9qhnyTXFMnXcTF_ntRueThXtGnv9YUhLKaDHY8Mcf69OfqCSpODVGgqtmkhxCiwFOeML1MbSmr6g8T9YPvHXCyw2BbHNC1Up1kGVYQGVL2wX0uqef0hO1dwxBYUeG6XLYtwwmjU3LYv3feQXsZBx1-CNC2eN_tUCpqBL9xwYYtce1IBYsaGN0HwpBbMxmcCe1CUtm4qfzquHBk4NVPCC0ihXMwgHOo0SBWCY9YgCfLqwCnUo_ngVfdGNfFrxL68c_VJeGTGwYjUV9FUx9pJeYBMF_PDUmkLLKarxmUGw1CGHYihgYqvOM10XOQArC'
node=execjs.get()
# d转换成md5
fmd5 = hashlib.md5(str_to_md5.encode(encoding='utf-8')).hexdigest()
print(fmd5)
# A.signature:__g._encrypt加密
with open('zhihu.js', 'r' ,encoding='utf-8') as f:
    ctx1 = execjs.compile(f.read(), cwd=r'C:\Windows\System32\node_modules')
encrypt_str = ctx1.call('b', fmd5)
print(encrypt_str)# aXYyNg98gwxxb0O80BtBNcrqrLtYNwSqMLF0nJ9qnG2p
#x-zse-96
