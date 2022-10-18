from 下载数据 import Download_page
from 保存到数据库 import SQL_opration
#https://steamcommunity.com/workshop/browse/?appid=431960&browsesort=lastupdated&section=readytouseitems
# &requiredtags%5B0%5D=Scene&requiredtags%5B1%5D=Mature&created_date_range_filter_start=0&created_date_range_filter_end=0
# &updated_date_range_filter_start=0&updated_date_range_filter_end=0&actualsort=lastupdated&p=1

#https://steamcommunity.com/workshop/browse/?appid=431960&searchtext=&childpublishedfileid=0
# &browsesort=totaluniquesubscribers&section=readytouseitems&requiredtags%5B0%5D=Web&requiredtags%5B1%5D=Mature
# &created_date_range_filter_start=0&created_date_range_filter_end=0&updated_date_range_filter_start=0&updated_date_range_filter_end=0
# &actualsort=totaluniquesubscribers&p=3

#https://steamcommunity.com/workshop/browse/?appid=431960&searchtext=&childpublishedfileid=0
# &browsesort=trend&section=readytouseitems&requiredtags%5B%5D=Music&requiredtags%5B%5D=Scene
# &requiredtags%5B%5D=Everyone&created_date_range_filter_start=0&created_date_range_filter_end=0
# &updated_date_range_filter_start=0&updated_date_range_filter_end=0

#requiredtags%5B0%5D=Music&requiredtags%5B1%5D=Scene&requiredtags%5B2%5D=Everyone
#requiredtags%5B0%5D=Music&requiredtags%5B1%5D=Scene&requiredtags%5B2%5D=Everyone
def main(i):
    params = {
        'appid': '431960',
        'searchtext' :' ',
        'childpublishedfileid' : '0',
        # 'browsesort': 'totaluniquesubscribers',
        # 'browsesort': 'trend',
        # 'browsesort': 'mostrecent',
        'browsesort': 'lastupdated',

        'section': 'readytouseitems',
        # 'requiredtags[0]': 'Abstract',
        # 'requiredtags[0]': 'Animal',
        # 'requiredtags[0]': 'Anime',     #193258  ,110700
        # 'requiredtags[0]': 'Cartoon',
        # 'requiredtags[0]': 'CGI',
        # 'requiredtags[0]': 'Cyberpunk',
        # 'requiredtags[0]': 'Fantasy',
        # 'requiredtags[0]': 'Game',       #145751,92634
        # 'requiredtags[0]': 'Girls',
        # 'requiredtags[0]': 'Guys',
        # 'requiredtags[0]': 'Landscape',
        # 'requiredtags[0]': 'Medieval',
        # 'requiredtags[0]': 'Memes',
        # 'requiredtags[0]': 'MMD',
        # 'requiredtags[0]': 'Music',
        # 'requiredtags[0]': 'Nature',
        # 'requiredtags[0]': 'Pixel art',
        # 'requiredtags[0]': 'Relaxing',
        # 'requiredtags[0]': 'Retro',
        # 'requiredtags[0]': 'Sci-Fi',
        # 'requiredtags[0]': 'Sports',
        # 'requiredtags[0]': 'Technology',
        # 'requiredtags[0]': 'Television',
        # 'requiredtags[0]': 'Vehicle',
        'requiredtags[0]': 'Unspecified',

        'requiredtags[1]': 'scene',
        # 'requiredtags[0]': 'Video',
        # 'requiredtags[0]': 'Application',
        # 'requiredtags[0]': 'web',
        'requiredtags[2]': 'Everyone',
        'created_date_range_filter_start': '0',
        'created_date_range_filter_end': ' 0',
        'updated_date_range_filter_start': '0',
        'updated_date_range_filter_end': '0',

        # ' actualsort': 'totaluniquesubscribers',
        # ' actualsort': 'trend',
        # ' actualsort': 'mostrecent',
        ' actualsort': 'lastupdated',
        'p': f'{i}',
        'days' : '-1',
        # 'numperpage': '60',
    }
    arr=Download_page(params)
    SQL_opration(arr)
    print(f"第{i}页")
    # print(arr)
    print(len(arr))
# main(1)


