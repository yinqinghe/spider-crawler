import json
import re

import requests
# url='https://edith.xiaohongshu.com/api/sns/v1/note/feed?note_id=625fef2400000000010250f5&page=1&num=5&fetch_mode=1&source=explore&ads_track_id=onlineswing_VIDEOEND_6243dce1000000002103dcfc%402a12jq4lkf6m8f1ifylop'
# url='https://edith.xiaohongshu.com/api/sns/v4/note/user/posted?user_id=61b3344b0000000010005b21&sub_tag_id=&cursor=623842eb000000002103bd82&num=10&use_cursor=true&pin_note_id=&pin_note_ids='
# url='https://edith.xiaohongshu.com/api/sns/v4/note/user/posted?user_id=592e64aa50c4b41fb8ad69f6&sub_tag_id=&cursor=62375036000000000102727b&num=10&use_cursor=true&pin_note_id=&pin_note_ids='
# url='https://edith.xiaohongshu.com/api/sns/v1/note/feed?note_id=624030a5000000000102dd1f&page=1&num=5&fetch_mode=1&source=profile.userview&ads_track_id='
# url='https://edith.xiaohongshu.com/api/sns/v1/note/feed?note_id=623da62d000000002103d707&page=1&num=5&fetch_mode=1&source=profile.userview&ads_track_id='
url='https://edith.xiaohongshu.com/api/sns/v1/note/feed?note_id=623c351d0000000021036f08&page=1&num=5&fetch_mode=1&source=profile.userview&ads_track_id='

header = {
    # 'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36',
    'xy-platform-info': 'platform=android&build=6950211&deviceId=6cd560b4-452c-3396-ba95-115c1e814f40',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe0xG1IbD9/c+qCLOlKGmTtFa+lG43AHeeFURaxEltC1mLY1SJ38+uIMz8Mp1ct+g/M7FQxPEGDbZe783S82guQwgv0KJjoRZhmhgDOvhmK1',
    'X-B3-TraceId': '7d7d56513a1f0700',
    'xy-common-params': 'deviceId=6cd560b4-452c-3396-ba95-115c1e814f40&identifier_flag=0&tz=Asia%2FShanghai&fid=16511951041016d5ea44928775774e45ff57b1d8efe3&app_id=ECFAAF01&device_fingerprint1=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&uis=light&launch_id=1651195315&project_id=ECFAAF&device_fingerprint=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&versionName=6.95.0&platform=android&sid=session.1651197973080859091103&t=1651198023&build=6950211&x_trace_page_current=explore_feed&lang=zh-Hans&channel=YingYongBao',
}
header1={
    'xy-platform-info': 'platform=android&build=6950211&deviceId=6cd560b4-452c-3396-ba95-115c1e814f40',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe0xG1IbD9/c+qCLOlKGmTtFa+lG43AHeeFURaxEltC1mLY1SJ38+uIMz8Mp1ct+g/M7FQxPEGDbZe783S82guQCYbkfGTmpSdDsylWl1U2a',
    'xy-common-params': 'deviceId=6cd560b4-452c-3396-ba95-115c1e814f40&identifier_flag=0&tz=Asia%2FShanghai&fid=16511951041016d5ea44928775774e45ff57b1d8efe3&app_id=ECFAAF01&device_fingerprint1=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&uis=light&launch_id=1651195315&project_id=ECFAAF&device_fingerprint=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&versionName=6.95.0&platform=android&sid=session.1651197973080859091103&t=1651198550&build=6950211&x_trace_page_current=user_page&lang=zh-Hans&channel=YingYongBao',

}
header2={
    'xy-platform-info': 'platform=android&build=6950211&deviceId=6cd560b4-452c-3396-ba95-115c1e814f40',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe0xG1IbD9/c+qCLOlKGmTtFa+lG43AHeeFURaxEltC1mLY1SJ38+uIMz8Mp1ct+g/M7FQxPEGDbZe783S82guTU2sSrLcNBdSnyU8QwyHwZ',
    'xy-common-params': 'deviceId=6cd560b4-452c-3396-ba95-115c1e814f40&identifier_flag=0&tz=Asia%2FShanghai&fid=16511951041016d5ea44928775774e45ff57b1d8efe3&app_id=ECFAAF01&device_fingerprint1=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&uis=light&launch_id=1651195315&project_id=ECFAAF&device_fingerprint=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&versionName=6.95.0&platform=android&sid=session.1651197973080859091103&t=1651198804&build=6950211&x_trace_page_current=note_detail_r10&lang=zh-Hans&channel=YingYongBao',

}
header3={
    'xy-platform-info': 'platform=android&build=6950211&deviceId=6cd560b4-452c-3396-ba95-115c1e814f40',
    'shield': 'XYAAAAAQAAAAEAAABTAAAAUzUWEe0xG1IbD9/c+qCLOlKGmTtFa+lG43AHeeFURaxEltC1mLY1SJ38+uIMz8Mp1ct+g/M7FQxPEGDbZe783S82guQmwZg3t6hoNAZVD75y9NrK',
    'xy-common-params': 'deviceId=6cd560b4-452c-3396-ba95-115c1e814f40&identifier_flag=0&tz=Asia%2FShanghai&fid=16511951041016d5ea44928775774e45ff57b1d8efe3&app_id=ECFAAF01&device_fingerprint1=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&uis=light&launch_id=1651195315&project_id=ECFAAF&device_fingerprint=202204290918284d30fa7773d01fcd8581c614ddea693801271eb788e1b438&versionName=6.95.0&platform=android&sid=session.1651197973080859091103&t=1651199461&build=6950211&x_trace_page_current=note_detail_r10&lang=zh-Hans&channel=YingYongBao',

}
res=requests.get(url,headers=header3).json()
# js=re.compile('__jsonp101650446812484(?P<datasrc>.*?)')
# res=js.search(res)
print(res)
# print(list)
# print(len(list))
