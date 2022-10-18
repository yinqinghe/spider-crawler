import requests
from lxml import etree
import re
from moviepy.editor import *
import os

if __name__ == '__main__':

    url_ = input("请输入播放页面的url:")

    headers_ = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "referer": "https://space.bilibili.com/517327498/dynamic?spm_id_from=444.41.list.card_avatar.click"
    }

    response_ = requests.get(url_,headers=headers_)

    str_data = response_.text  # 视频主页的html代码，类型是字符串

    # 使用xpath语法解析html代码，得到想要的url
    html_obj = etree.HTML(str_data)

    # 获取视频的名称
    res_ = html_obj.xpath("//title/text()")[0]
    title_ = re.findall(r"(.*?)_哔哩哔哩_bilibili",res_)[0]
    # 影响视频合成的特殊字符处理
    title_ = title_.replace(" ","")
    title_ = title_.replace("&","")
    title_ = title_.replace("/","")

    # 使用xpath语法获取数据，取到的数据为列表，索引[0]取值去除里面的字符串，即包含视频音频的url文件
    url_list_str = html_obj.xpath("//script[contains(text(),'window.__playinfo__')]/text()")[0]

    video_url = re.findall(r'"video":\[{"id":\d+,"baseUrl":"(.*?)"',url_list_str)[0]
    audio_url = re.findall(r'"audio":\[{"id":\d+,"baseUrl":"(.*?)"',url_list_str)[0]

    # 设置拥有一个动态变化跳转referer和headers
    headers_ = {
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36",
        "referer": url_
    }

    response_video = requests.get(video_url,headers=headers_,stream=True)
    bytes_video = response_video.content
    response_audio = requests.get(audio_url,headers=headers_,stream=True)
    bytes_audio = response_audio.content

    # 获取文件的大小  单位为kb
    video_size = int(int(response_video.headers['content-length'])/1024)
    audio_size = int(int(response_audio.headers['content-length'])/1024)

    with open(f"{title_}!.mp4", "wb") as f:
        f.write(bytes_video)
        print(f"纯视频文件下载完毕，大小为：{video_size}KB,{int(video_size/1024)}MB")
    with open(f"{title_}!.mp3", "wb") as f:
        f.write(bytes_audio)
        print(f"纯音频文件下载完毕，大小为：{audio_size}KB,{int(audio_size / 1024)}MB")

    ffmpeg_tools.ffmpeg_merge_video_audio(f'{title_}!.mp4', f'{title_}!.mp3', f'{title_}.mp4')
    print("视频合成成功！")
    # 显示合成文件的大小
    res_ = int(os.stat(f'{title_}.mp4').st_size/1024)
    print(f"{title_}视频文件下载完毕，大小为：{res_}KB,{int(res_ / 1024)}MB")

    os.remove(f"{title_}!.mp4")
    os.remove(f"{title_}!.mp3")