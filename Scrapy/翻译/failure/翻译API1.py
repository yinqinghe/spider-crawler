# -*- coding: utf-8 -*-

# 作者：Dfounderliu（刘宇）
# 程序功能：腾讯云API DEMO

# 说明，在70,71行修改自己的secretId与secretKey
# 可以在https://console.cloud.tencent.com/capi 获取

# 运行结果：
#  {"Response":{"RequestId":"0fd2e5b4-0beb-4e01-906f-e63dd7dd33af","Source":"en","Target":"zh","TargetText":"\u4f60\u597d\u4e16\u754c"}}

import binascii
import hashlib
import hmac
import sys
import urllib.parse
import urllib.request
import time
import random

import requests


def sign(secretKey, signStr, signMethod):
    '''
    该方法主要是实现腾讯云的签名功能
    :param secretKey: 用户的secretKey
    :param signStr: 传递进来字符串，加密时需要使用
    :param signMethod: 加密方法
    :return:
    '''
    if sys.version_info[0] > 2:
        signStr = signStr.encode("utf-8")
        secretKey = secretKey.encode("utf-8")

    # 根据参数中的signMethod来选择加密方式
    if signMethod == 'HmacSHA256':
        digestmod = hashlib.sha256
    elif signMethod == 'HmacSHA1':
        digestmod = hashlib.sha1

    # 完成加密，生成加密后的数据
    hashed = hmac.new(secretKey, signStr, digestmod)
    base64 = binascii.b2a_base64(hashed.digest())[:-1]

    if sys.version_info[0] > 2:
        base64 = base64.decode()

    return base64

def dictToStr(dictData):
    '''
    本方法主要是将Dict转为List并且拼接成字符串
    :param dictData:
    :return: 拼接好的字符串
    '''
    tempList = []
    for eveKey, eveValue in dictData.items():
        tempList.append(str(eveKey) + "=" + str(eveValue))
    return "&".join(tempList)


# 用户必须准备好的secretId和secretKey
# 可以在 https://console.cloud.tencent.com/capi 获取
secretId = "AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK"
secretKey = "hFdL5iDZnusiS0Oeoomcu2yrfXPK7zlN"

# 在此处定义一些必须的内容
timeData = str(int(time.time())) # 时间戳
nonceData = int(random.random()*10000) # Nonce，官网给的信息：随机正整数，与 Timestamp 联合起来， 用于防止重放攻击
actionData = "TextTranslate" # Action一般是操作名称
uriData = "tmt.tencentcloudapi.com" # uri，请参考官网
signMethod="HmacSHA256" # 加密方法
requestMethod = "GET" # 请求方法，在签名时会遇到，如果签名时使用的是GET，那么在请求时也请使用GET
regionData = "ap-hongkong" # 区域选择
versionData = '2018-03-21' # 版本选择

# 签名时需要的字典
# 首先对所有请求参数按参数名做字典序升序排列，所谓字典序升序排列，
# 直观上就如同在字典中排列单词一样排序，按照字母表或数字表里递增
# 顺序的排列次序，即先考虑第一个“字母”，在相同的情况下考虑第二
# 个“字母”，依此类推。
signDictData = {
    'Action' : actionData,
    'Nonce' : nonceData,
    'ProjectId':0,
    'Region' : regionData,
    'SecretId' : secretId,
    'SignatureMethod':signMethod,
    'Source': "en",
    'SourceText': "hello world",
    'Target': "zh",
    'Timestamp' : int(timeData),
    'Version':versionData ,
}

# 获得拼接的字符串，用于签名
# 此步骤生成请求字符串。 将把上一步排序好的请求参数格式化成“参数名称”=“参数值”的形式，如对Action参数，
# 其参数名称为"Action"，参数值为"DescribeInstances"，因此格式化后就为Action=DescribeInstances。
# 注意：“参数值”为原始值而非url编码后的值。
# 然后将格式化后的各个参数用"&"拼接在一起，最终生成请求字符串。
# 此步骤生成签名原文字符串。 签名原文字符串由以下几个参数构成:
# 1) 请求方法: 支持 POST 和 GET 方式，这里使用 GET 请求，注意方法为全大写。
# 2) 请求主机:查看实例列表(DescribeInstances)的请求域名为：cvm.tencentcloudapi.com。实际的请求域名根据接口所属模块的不同而不同，详见各接口说明。
# 3) 请求路径: 当前版本云API的请求路径固定为 / 。 4) 请求字符串: 即上一步生成的请求字符串。
# 签名原文串的拼接规则为:
#   请求方法 + 请求主机 +请求路径 + ? + 请求字符串
requestStr = "%s%s%s%s%s"%(requestMethod,uriData,"/","?",dictToStr(signDictData))
print(requestStr)
# 调用签名方法，同时将结果进行url编码，官方文档描述如下：
# 生成的签名串并不能直接作为请求参数，需要对其进行 URL 编码。 注意：如果用户的请求方法是GET，则对所有请求参
# 数值均需要做URL编码。 如上一步生成的签名串为 EliP9YW3pW28FpsEdkXt/+WcGeI= ，最终得到的签名串请求参数(Signature)
# 为： EliP9YW3pW28FpsEdkXt%2f%2bWcGeI%3d ，它将用于生成最终的请求URL。
signData = urllib.parse.quote(sign(secretKey,requestStr,signMethod))

# 上述操作是实现签名，下面即进行请求
# 先建立请求参数, 此处参数只在签名时多了一个Signature
actionArgs = signDictData
actionArgs["Signature"] = signData
print(signData)
# 根据uri构建请求的url
requestUrl = "https://%s/?"%(uriData)
# 将请求的url和参数进行拼接
requestUrlWithArgs = requestUrl + dictToStr(actionArgs)
print(requestUrlWithArgs)
# 获得response
# responseData = urllib.request.urlopen(requestUrlWithArgs).read().decode("utf-8")
responseData=requests.post(requestUrl)
print(responseData.text)

# 获得到的结果形式：
#  {"Response":{"RequestId":"0fd2e5b4-0beb-4e01-906f-e63dd7dd33af","Source":"en","Target":"zh","TargetText":"\u4f60\u597d\u4e16\u754c"}}

# 对Json字符串处理
# import json
# print(json.loads(responseData)["Response"]["TargetText"])