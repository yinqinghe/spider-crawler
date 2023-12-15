from DrissionPage import WebPage


page=WebPage()

page.get('https://gitee.com/explore')

page('#q').input('DrissionPage')

page('t:button@tx():搜索').click(wait_loading=True)

page.change_mode()

items=page('#hits-list').eles('.item')

for item in items:
    print(item('.title').text)
    print(item('.desc').text)
    print(item)