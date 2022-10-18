
import requests

url="https://www.pearvideo.com/video_1749325"
contId=url.split("_")[1]
videoStatus=f"https://www.pearvideo.com/videoStatus.jsp?contId={contId}&mrd=0.06261522881814141"
headers={
    "Referer": url
}

resp=requests.get(videoStatus,headers=headers)
# print(resp.text)
dic=resp.json()
srcUrl=dic['videoInfo']['videos']['srcUrl']
systemTime=dic['systemTime']
srcUrl=srcUrl.replace(systemTime,f"cont-{contId}")

print(srcUrl)
with open("a.mp4",mode="wb") as f:
    f.write(requests.get(srcUrl).content)
# print(resp.headers)
resp.close()