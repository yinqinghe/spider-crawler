# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Item,Field

class OldlearnItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
class PIPIXIA_USERS(Item):
    id_str=Field()
    name=Field()
    followers_count=Field()
    followings_count=Field()
    like_count=Field()
    description=Field()

class PIPIXIA(Item):
    vedio=Field()
    create_time=Field()
    title=Field()
    nowtime=Field()
    share_url=Field()
class MainPage(Item):
    link=Field()
    title=Field()
    pic=Field()
    price=Field()

class BaiduPage(Item):
    title=Field()
    link=Field()
    nowtime=Field()

class Wechat_account(Item):
    title=Field()
    link=Field()
    create_time=Field()
    aid=Field()
    update_time=Field()
    nowtime=Field()

class Pics(Item):
    imgsrc=Field()
    imgname=Field()
    title=Field()
class toutiao(Item):
    link = Field()
    title = Field()
    abstract = Field()
    publish_time = Field()
    read_count = Field()
    comment_count = Field()
    nowtime=Field()
    createtime=Field()

class Baijiahao(Item):
    title=Field()
    link=Field()
    createtime=Field()
    subtitle=Field()
    article_id=Field()
    publishtime=Field()
    updatetime=Field()
    dynamic_ctime=Field()
    itemtype=Field()
    type=Field()
    nowtime=Field()
class Picslink(Item):
    # imgsrc=Field()
    # imgname=Field()
    nowtime=Field()
    title=Field()
    link1=Field()
    link2=Field()
    link3=Field()
    link4=Field()
    link5=Field()
    link6=Field()
    link7=Field()
    link8=Field()
    link9=Field()
    link10=Field()
    link11=Field()
    link12=Field()
    link13=Field()
    link14=Field()
    link15=Field()
    link16=Field()
    link17=Field()
    link18=Field()
    link19=Field()
    link20=Field()
    link21=Field()
    link22=Field()
    link23=Field()
    link24=Field()
    link25=Field()
    link26=Field()
    link27=Field()
    link28=Field()
    link29=Field()
    link30=Field()
    link31=Field()
    link32=Field()
    link33=Field()
    link34=Field()
    link35=Field()
    link36=Field()
    link37=Field()
    link38=Field()
    link39=Field()
    link40=Field()
    link41=Field()
    link42=Field()
    link43=Field()
    link44=Field()
    link45=Field()
    link46=Field()
    link47=Field()
    link48=Field()
    link49=Field()
    link50=Field()
    link51=Field()
    link52=Field()
    link53=Field()
    link54=Field()
    link55=Field()
    link56=Field()
    link57=Field()
    link58=Field()
    link59=Field()
    link60=Field()






