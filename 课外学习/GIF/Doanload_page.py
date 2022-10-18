import requests
from bs4 import BeautifulSoup
url='https://www.sex.com/gifs/milf/'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
}

proxies={'http':'http://127.0.0.1:32433','https':'https://127.0.0.1:32433'}
def Download_page_GIF(p):
    params = {
        'page': f'{p}',
    }

    res=requests.get(url,params=params)
    res.encoding='utf-8'

    main_page = BeautifulSoup(res.text, "html.parser")
    image = main_page.find_all("img", class_="image")
    # print(image[0])
    print(len(image))
    for i in image:
        data_src=i.get("data-src")
        print(data_src)

Download_page_GIF(46)