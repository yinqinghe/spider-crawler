from DrissionPage import ChromiumPage,ChromiumOptions,WebPage
from DrissionPage.easy_set import set_proxy

Op=ChromiumOptions().set_paths(local_port=4567)
# Op.set_proxy('http://127.0.0.1:10809')
set_proxy('http://127.0.0.1:10809')
# set_proxy('')
# page=ChromiumPage()
page=ChromiumPage(addr_driver_opts=Op)
# page=WebPage(driver_or_options=Op)

page.get('https://www.google.com')