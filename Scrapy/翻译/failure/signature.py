# Python
# -*- coding: utf-8 -*-
import hashlib, hmac, json, os, sys, time
from datetime import datetime

# 密钥参数
secret_id = "AKIDHYkrtkT3Wnq2ADID2hFpRuESYVI2fBYK"
secret_key = "hFdL5iDZnusiS0Oeoomcu2yrfXPK7zlN"

service = "tmt"
host = "tmt.tencentcloudapi.com"
endpoint = "https://" + host
region = "ap-beijing"
action = "TextTranslate"
version = "2018-03-21"
algorithm = "TC3-HMAC-SHA256"
timestamp = int(time.time())
# timestamp = 1551113065
date = datetime.utcfromtimestamp(timestamp).strftime("%Y-%m-%d")
params = {"Limit": 1, "Filters": [{"Name": "instance-name", "Values": [u"未命名"]}]}

# ************* 步骤 1：拼接规范请求串 *************
http_request_method = "POST"
canonical_uri = "/"
canonical_querystring = ""
ct = "application/json; charset=utf-8"
payload = json.dumps(params)
canonical_headers = "content-type:%s\nhost:%s\n" % (ct, host)
signed_headers = "content-type;host"
hashed_request_payload = hashlib.sha256(payload.encode("utf-8")).hexdigest()
canonical_request = (http_request_method + "\n" +
                     canonical_uri + "\n" +
                     canonical_querystring + "\n" +
                     canonical_headers + "\n" +
                     signed_headers + "\n" +
                     hashed_request_payload)
# print(canonical_request)

# ************* 步骤 2：拼接待签名字符串 *************
credential_scope = date + "/" + service + "/" + "tc3_request"
hashed_canonical_request = hashlib.sha256(canonical_request.encode("utf-8")).hexdigest()
string_to_sign = (algorithm + "\n" +
                  str(timestamp) + "\n" +
                  credential_scope + "\n" +
                  hashed_canonical_request)
# print(string_to_sign)


# ************* 步骤 3：计算签名 *************
# 计算签名摘要函数
def sign(key, msg):
    return hmac.new(key, msg.encode("utf-8"), hashlib.sha256).digest()
secret_date = sign(("TC3" + secret_key).encode("utf-8"), date)
secret_service = sign(secret_date, service)
secret_signing = sign(secret_service, "tc3_request")
signature = hmac.new(secret_signing, string_to_sign.encode("utf-8"), hashlib.sha256).hexdigest()
print(signature)

# ************* 步骤 4：拼接 Authorization *************
authorization = (algorithm + " " +
                 "Credential=" + secret_id + "/" + credential_scope + ", " +
                 "SignedHeaders=" + signed_headers + ", " +
                 "Signature=" + signature)
# print(authorization)

print('curl -X POST ' + endpoint
      + ' -H "Authorization: ' + authorization + '"'
      + ' -H "Content-Type: application/json; charset=utf-8"'
      + ' -H "Host: ' + host + '"'
      + ' -H "X-TC-Action: ' + action + '"'
      + ' -H "X-TC-Timestamp: ' + str(timestamp) + '"'
      + ' -H "X-TC-Version: ' + version + '"'
      + ' -H "X-TC-Region: ' + region + '"'
      + " -d '" + payload + "'")
# Golang
# package main
#
# import (
#     "crypto/hmac"
#     "crypto/sha256"
#     "encoding/hex"
#     "fmt"
#     "time"
# )
#
# func sha256hex(s string) string {
#     b := sha256.Sum256([]byte(s))
#     return hex.EncodeToString(b[:])
# }
#
# func hmacsha256(s, key string) string {
#     hashed := hmac.New(sha256.New, []byte(key))
#     hashed.Write([]byte(s))
#     return string(hashed.Sum(nil))
# }
#
# func main() {
#     secretId := "AKIDz8krbsJ5yKBZQpn74WFkmLPx3*******"
#     secretKey := "Gu5t9xGARNpq86cd98joQYCN3*******"
#     host := "cvm.tencentcloudapi.com"
#     algorithm := "TC3-HMAC-SHA256"
#     service := "cvm"
#     version := "2017-03-12"
#     action := "DescribeInstances"
#     region := "ap-guangzhou"
#     //var timestamp int64 = time.Now().Unix()
#     var timestamp int64 = 1551113065
#
#     // step 1: build canonical request string
#     httpRequestMethod := "POST"
#     canonicalURI := "/"
#     canonicalQueryString := ""
#     canonicalHeaders := "content-type:application/json; charset=utf-8\n" + "host:" + host + "\n"
#     signedHeaders := "content-type;host"
#     payload := `{"Limit": 1, "Filters": [{"Values": ["\u672a\u547d\u540d"], "Name": "instance-name"}]}`
#     hashedRequestPayload := sha256hex(payload)
#     canonicalRequest := fmt.Sprintf("%s\n%s\n%s\n%s\n%s\n%s",
#         httpRequestMethod,
#         canonicalURI,
#         canonicalQueryString,
#         canonicalHeaders,
#         signedHeaders,
#         hashedRequestPayload)
#     fmt.Println(canonicalRequest)
#
#     // step 2: build string to sign
#     date := time.Unix(timestamp, 0).UTC().Format("2006-01-02")
#     credentialScope := fmt.Sprintf("%s/%s/tc3_request", date, service)
#     hashedCanonicalRequest := sha256hex(canonicalRequest)
#     string2sign := fmt.Sprintf("%s\n%d\n%s\n%s",
#         algorithm,
#         timestamp,
#         credentialScope,
#         hashedCanonicalRequest)
#     fmt.Println(string2sign)
#
#     // step 3: sign string
#     secretDate := hmacsha256(date, "TC3"+secretKey)
#     secretService := hmacsha256(service, secretDate)
#     secretSigning := hmacsha256("tc3_request", secretService)
#     signature := hex.EncodeToString([]byte(hmacsha256(string2sign, secretSigning)))
#     fmt.Println(signature)
#
#     // step 4: build authorization
#     authorization := fmt.Sprintf("%s Credential=%s/%s, SignedHeaders=%s, Signature=%s",
#         algorithm,
#         secretId,
#         credentialScope,
#         signedHeaders,
#         signature)
#     fmt.Println(authorization)
#
#     curl := fmt.Sprintf(`curl -X POST https://%s\
#  -H "Authorization: %s"\
#  -H "Content-Type: application/json; charset=utf-8"\
#  -H "Host: %s" -H "X-TC-Action: %s"\
#  -H "X-TC-Timestamp: %d"\
#  -H "X-TC-Version: %s"\
#  -H "X-TC-Region: %s"\
#  -d '%s'`, host, authorization, host, action, timestamp, version, region, payload)
#     fmt.Println(curl)
# }
