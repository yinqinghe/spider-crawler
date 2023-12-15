from DrissionPage import ChromiumPage

page=ChromiumPage()
page.get('https://gitee.com/login')

ele=page.ele('#user_login')

ele.input('你的账户')

page.ele('#user_password').input('你的密码')

page.ele('@value=登 录').click()