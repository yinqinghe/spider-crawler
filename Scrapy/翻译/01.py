import time

import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import pymysql

#创建连接
conn=pymysql.connect(host='127.0.0.1',port=3306,user='root',password='123456',database='sun',charset='utf8')
#创建游标
cursor=conn.cursor(pymysql.cursors.DictCursor)
option=Options()

option.add_argument('--disable-blink-features=AutomationControlled')
driver=webdriver.Chrome(options=option)
driver.get("https://fanyi.qq.com/")
for i in range(8, 9):  # 176    100
    num = i * 10

    sql_query_id = f"select title from nanico where id between {1+num} and {10+num}"
    cursor.execute(sql_query_id)
    result = cursor.fetchall()  # 接收查询到的结果
    print(result)
    time.sleep(3)
    ii=0
    try:
        for r in result:
            ii=ii+1
            driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[1]/textarea').send_keys(r['title'],Keys.ENTER)
            time.sleep(1)
            text=driver.find_element_by_xpath(f'/html/body/div[2]/div[2]/div[2]/div[2]/div[2]/span[{ii*2}]').text
            j=i*10+ii
            print(j)
            sql_add = f"update nanico set CN_title='{text}' where id={j}"

            cursor.execute(sql_add)
            print(text)
        # driver.find_element_by_xpath('/html/body/div[2]/div[2]/div[2]/div[1]/div[2]').click()
        driver.refresh()

        # 提交  不然无法保存
        conn.commit()
        time.sleep(4)
    except selenium.common.exceptions.NoSuchElementException:
        print("ffzasdsd")
        time.sleep(2)
        # driver.switch_to.frame('tcaptcha_iframe')
        # # btn=driver.find_element_by_xpath('//*[@id="tcaptcha_drag_thumb"]')
        # # ActionChains(driver).drag_and_drop_by_offset(btn,220,0).perform()
        # slider=WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.ID,'tcaptcha_drag_thumb')))
        # distance=220
        # actions=webdriver.ActionChains(driver)
        #
        # actions.click_and_hold(slider)
        # actions.pause(0.2)
        # actions.move_by_offset(distance+5,0)
        # actions.pause(0.2)
        # actions.move_by_offset(-10,0)
        # actions.pause(0.2)
        # print('111')
        # actions.perform()
        # print('222')
        time.sleep(2)


        # driver.find_element_by_xpath('//*[@id="captcha_close"]').click()
        # driver.refresh()
        # time.sleep(25)


#提交  不然无法保存
conn.commit()

#关闭游标
cursor.close()
#关闭连接
conn.close()