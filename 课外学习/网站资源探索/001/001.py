import requests
from bs4 import BeautifulSoup
# url='https://steamcommunity.com/sharedfiles/filedetails/?id=2581577662&searchtext='
# url='https://steamcommunity.com'
url='https://steamcommunity.com/workshop/browse/?appid=431960&browsesort=trend&section=readytouseitems&created_date_range_filter_start=0&created_date_range_filter_end=0&updated_date_range_filter_start=0&updated_date_range_filter_end=0&actualsort=trend&p=994&days=-1'
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
}
params={
    'appid': '431960',
    'requiredtags[0]': 'Girls',
    'actualsort': 'trend',
    'browsesort':' trend',
    'p': '1',
    'days': '-1',
}
proxies={'http':'http://127.0.0.1:32433','https':'https://127.0.0.1:32433'}
res=requests.get(url,headers=header,proxies=proxies)
res.encoding='utf-8'
main_page=BeautifulSoup(res.text,"html.parser")
workshopItem=main_page.find_all("div",class_="workshopItem")
w=workshopItem[0]
workshop_author_link=w.find("div",class_="workshopItemAuthorName ellipsis").find('a').get('href')
workshop_author_name=w.find("div",class_="workshopItemAuthorName ellipsis").find('a').text
data_publishedfileid=w.find("a").get("data-publishedfileid")
workshopItemPreviewImage=w.find('img').get('src')
fileRating=w.find('img',class_="fileRating").get('src')
# print(len(workshopItem))
print(workshopItem[0])
print(data_publishedfileid,workshopItemPreviewImage,workshop_author_link,workshop_author_name,fileRating)