import json

from tencentcloud.common import credential
from tencentcloud.common.profile.client_profile import ClientProfile
from tencentcloud.common.profile.http_profile import HttpProfile
from tencentcloud.common.exception.tencent_cloud_sdk_exception import TencentCloudSDKException
from tencentcloud.tmt.v20180321 import tmt_client, models
# try:
#     # cred = credential.Credential("你的SecretId", "你的SecretKey")
#     cred = credential.Credential("AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK", "hFdL5iDZnusiS0Oeoomcu2yrfXPK7zlN")
#
#     httpProfile = HttpProfile()
#     httpProfile.endpoint = "tmt.tencentcloudapi.com"
#
#     clientProfile = ClientProfile()
#     clientProfile.httpProfile = httpProfile
#     client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)
#
#     req = models.TextTranslateRequest()
#     req.SourceText = "傻逼"
#     req.Source = "zh"
#     req.Target = "ko"
#     req.ProjectId = 0
#
#     resp = client.TextTranslate(req)
#     print(resp.to_json_string())
#
# except TencentCloudSDKException as err:
#     print(err)

cred = credential.Credential("AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK", "hFdL5iDZnusiS0Oeoomcu2yrfXPK7zlN")

httpProfile = HttpProfile()
httpProfile.endpoint = "tmt.tencentcloudapi.com"

clientProfile = ClientProfile()
clientProfile.httpProfile = httpProfile
client = tmt_client.TmtClient(cred, "ap-beijing", clientProfile)
def tmt_SOK(text):
    req = models.TextTranslateRequest()
    req.SourceText = f"{text}"
    req.Source = "ko"
    req.Target = "zh"
    req.ProjectId = 0

    resp = client.TextTranslate(req)
    resp=resp.to_json_string()
    res=json.loads(resp)
    # print(res)
    # print(type(res))
    # print(res['TargetText'])
    return res['TargetText']
# tmt_SOK('dd')