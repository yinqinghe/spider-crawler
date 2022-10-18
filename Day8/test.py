# from selenium.webdriver import Chrome
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# import time
#
# web=Chrome()
# web.get("https://weibo.com/u/6448920093?tabtype=album&uid=6448920093&index=0")
# time.sleep(7)
# # web.find_element(By.XPATH,'/html/body/div[0]/div[0]/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/div/div/div/div[1]/div/div/div/div').click()
# el=web.find_element(By.XPATH,'/html/body/div[0]/div[0]/div[1]/div[1]/div/div/div[1]/div[1]/div[2]/div/div').text

import os
for x in os.listdir(r'D:\Pics\抖音采集工具x64\'):
    if os.path.isdir(x):
        print(x)