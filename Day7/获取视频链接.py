import requests
url="https://www.zhenbuka3.com/"
url1="https://pcc.mmiyue.com/hls/16e131aa7511b35388f9594a66ef8192423409e2e8a7f2d9015179c72da21ad1860a04f03e0112ea00d9aa59136d826b"
a="https://pcc.mmiyue.com/hls/16e131aa7511b35388f9594a66ef8192423409e2e8a7f2d9015179c72da21ad1860a04f03e0112ea00d9aa59136d826b"
aaa="https://pcc.mmiyue.com/hls/file/ts/1e53ba59b207aeae02fad120c56d1f006c5765e5bf0adfac53848c27747886a2c804a60714aa9c45fbce63597e76654295a4a76e1b9816fb400f0ee9789608e062ba0951292215d3ad61a928a77b08d7b9c8eac2497ceffa82809eba5b441e43a183783cfd68281ddce78801d55962c3edd3188766f48cca12236cd9"
# videoStatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.06261522881814141"
aa="https://pcc.mmiyue.com/hls/file/ts/1e53ba59b207aeae02fad120c56d1f006c5765e5bf0adfac53848c27747886a2c804a60714aa9c45fbce63597e76654295a4a76e1b9816fb400f0ee9789608e062ba0951292215d3ad61a928a77b08d7b9c8eac2497ceffa82809eba5b441e43a18f7f6ffd3c784b8bea880e82593090bc881a863cf48cca12236cde13"
bbb="https://lf9-static.bytednsdoc.com/obj/web.business.image/202112255d0da811ff455569416f8643"
ccc="https://pcc.mmiyue.com/hls/file/ts/1e53ba59b207aeae02fad120c56d1f006c5765e5bf0adfac53848c27747886a2c804a60714aa9c45fbce63597e76654295a4a76e1b9816fb400f0ee9789608e062ba0951292215d3ad61a928a77b08d7b9c8eac2497ceffa82809eba5b441e43a1842d6ea7687a4adeec8c0cd25932c9eb8b1a8a6af48cca12236cdd"

ddd="https://lf9-static.bytednsdoc.com/obj/web.business.image/202112255d0d9c0cf606567f47aab15b"
eee="https://pcc.mmiyue.com/hls/play/1851bc52bf57a3a30eff997d906d1d5c6d5335b1b902d8fa05d0873a7f3ac6eada5abe1849a8965bf48b371e25207818d9e9f276458f41ad1b115cb520895fba38ac4903373d42daef3df47fe13b1e8bed99"
ggg="https://good-vip.mmiyue.com/zhenbuka2/player/index.php?video_id=4a99Fc_JoFuTg9ziRsNU80U_CDIgpKaeYmkufSTvNF-866pswCT98FsyWMZ7pp0ae7Le5ipR_mJFiJTQlUOWcQeIkd3z"

fff="https://pcc.mmiyue.com/hls/file/ts/1e53ba59b207aeae02fad120c56d1f006c5765e5bf0adfac53848c27747886a2c804a60714aa9c45fbce63597e76654295a4a76e1b9816fb400f0ee9789608e062ba0951292215d3ad61a928a77b08d7b9c8eac2497ceffa82809eba5b441e43a1d7246eaf3c284f88ea8b0fdd5936c7bbd21d876df48cca12236cde"
headers={
    "Referer": url1,
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36"
}
resp=requests.get(a,headers=headers)
print(resp.text)
# with open("a.mp4",mode="wb") as f:
#     f.write(requests.get(eee).content)
resp.close()