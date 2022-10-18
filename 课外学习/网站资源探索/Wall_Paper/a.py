import requests
from bs4 import BeautifulSoup
header={
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.51 Safari/537.36',
    # 'Host': 'steamcommunity.com',
    # 'Referer': 'https://steamcommunity.com/workshop/browse/?appid=431960&browsesort=trend&section=readytouseitems&created_date_range_filter_start=0&created_date_range_filter_end=0&updated_date_range_filter_start=0&updated_date_range_filter_end=0&actualsort=trend&p=1&numperpage=30&days=365',
    # 'Cookie': 'sessionid=f2d495769439280c1bd68c04; timezoneOffset=28800,0; recentlyVisitedAppHubs=431960; _ga=GA1.2.889584037.1648710876; steamCountry=HK%7C32c7091d56eb442f59c701c5b2adf806; _gid=GA1.2.398753368.1648982353; workshopNumPerPage=30; app_impressions=431960@2_9_100013_|431960@2_100100_100101_100103|431960@2_9_100013_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_100101_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_100101_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_100101_100103|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_|431960@2_100100_230_; _gat_app=1',
}
url='https://steamcommunity.com/workshop/browse/?appid=431960&searchtext=&childpublishedfileid=0' \
    '&browsesort=totaluniquesubscribers&section=readytouseitems&requiredtags%5B%5D=Application' \
    '&requiredtags%5B%5D=Mature&created_date_range_filter_start=0&created_date_range_filter_end=0' \
    '&updated_date_range_filter_start=0&updated_date_range_filter_end=0'
res = requests.get(url, headers=header)
# print(res.request.url)
res.encoding = 'utf-8'
main_page = BeautifulSoup(res.text, "html.parser")
workshopItem = main_page.find_all("div", class_="workshopItem")
arry = []
i = 0
for w in workshopItem:
    arry.append([])
    workshopItemTitle = w.find("div", class_="workshopItemTitle").text
    workshop_author_link = w.find("div", class_="workshopItemAuthorName ellipsis").find('a').get('href')
    workshop_author_name = w.find("div", class_="workshopItemAuthorName ellipsis").find('a').text
    data_publishedfileid = w.find("a").get("data-publishedfileid")
    workshopItemPreviewImage = w.find('img').get('src')
    fileRating = w.find('img', class_="fileRating").get('src')
    fileRating_num = fileRating.split('/')[-1]
    fileRating_star = fileRating_num.split('.')[0]
    # print(len(workshopItem))
    arry[i].append(workshopItemTitle)
    arry[i].append(workshop_author_name)
    arry[i].append(data_publishedfileid)
    arry[i].append(workshop_author_link)
    arry[i].append(workshopItemPreviewImage)
    arry[i].append(fileRating_star)
    i = i + 1
    # print(data_publishedfileid,workshopItemPreviewImage,workshop_author_link,workshop_author_name,fileRating_num)
print(arry)