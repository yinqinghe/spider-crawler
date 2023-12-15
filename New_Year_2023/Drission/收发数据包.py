from DrissionPage import SessionPage

page=SessionPage()

for i in range(1,4):

    page.get(f'https://gitee.com/explore/all?page={i}')

    links=page.eles('.title project-namespace-path')

    for link in links:
        print(link.text,link.link)