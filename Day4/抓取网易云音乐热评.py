from Crypto.Cipher import AES
from base64 import b64encode
import json
import requests

url="https://music.163.com/weapi/comment/resource/comments/get?csrf_token="

data={
    "csrf_token": "",
    "cursor": "-1",
    "offset": "0",
    "orderType": "1",
    "pageNo": "2",
    "pageSize": "20",
    "rid": "R_SO_4_1325905146",
    "threadId": "R_SO_4_1325905146"
}
f="00e0b509f6259df8642dbc35662901477df22677ec152b5ff68ace615bb7b725152b3ab17a876aea8a5aa76d2e417629ec4ee341f56135fccf695280104e0312ecbda92557c93870114af6c9d05c4f7f0c3685b7a46bee255932575cce10b424d813cfe4875d3e82047b97ddef52741d546b8e289dc6935b3ece0462db0a22b8e7"
g="0CoJUm6Qyw8W8jud"
e="010001"
i="PNI4TKTruOUcEr4j"

def get_encSecKey():
    return "b294e62925643eeb50247530a0c8b00a80ed70cbc7ca566f83b60367d116795069c8def760f376c2fe394fbb7be2e3f39a436d49a80c77c5f651eb0231cd0ed69119751d8dc5a360582729ca21c54d1bd9519faac62f5e125a5476fff2c9aa80a67c424cae20b104e4a8759414dd2a9529a920c89d8d65d2942d98b6f824abab"

def get_params(data):
    first=enc_params(data,g)
    second=enc_params(first,i)
    return second

def to_16(data):
    pad=16-len(data)%16
    data+=chr(pad)*pad
    return data
def enc_params(data,key):
    iv="0102030405060708"
    data=to_16(data)
    aes=AES.new(key=key.encode("utf-8"),IV=iv.encode('utf-8'),mode=AES.MODE_CBC)
    bs=aes.encrypt(data.encode("utf-8"))
    return str(b64encode(bs),"utf-8")

"""
  function a(a) {
        var d, e, b = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789", c = "";
        for (d = 0; a > d; d += 1)
            e = Math.random() * b.length,
            e = Math.floor(e),
            c += b.charAt(e);
        return c    #生成一个16位的随机数
    }
    function b(a, b) {
        var c = CryptoJS.enc.Utf8.parse(b)
          , d = CryptoJS.enc.Utf8.parse("0102030405060708")
          , e = CryptoJS.enc.Utf8.parse(a)
          , f = CryptoJS.AES.encrypt(e, c, {
            iv: d,
            mode: CryptoJS.mode.CBC
        });
        return f.toString()
    }
    function c(a, b, c) {
        var d, e;
        return setMaxDigits(131),
        d = new RSAKeyPair(b,"",c),
        e = encryptedString(d, a)
    }
    function d(d, e, f, g) {
        var h = {}
          , i = a(16);
        return h.encText = b(d, g),
        h.encText = b(h.encText, i),
        h.encSecKey = c(i, e, f),
        h
    }"""

resp=requests.post(url,data={
    "params":get_params(json.dumps(data)),
    "encSecKey":get_encSecKey()
})
print(resp.json())
resp.close()