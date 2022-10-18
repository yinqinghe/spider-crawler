from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

web=Chrome()
web.get("https://www.lagou.com/")
web.switch_to.frame("contentFrame")
time.sleep(1)
el=web.find_element(By.XPATH,'/html/body/div[10]/div[1]/div[2]/div[2]/div[1]/div/ul/li[1]/a')
el.click()
web.find_element(By.XPATH,'/html/body/div[7]/div[1]/div[1]/div[1]/form/input[1]').send_keys("python",Keys.ENTER)
time.sleep(1)
li_list=web.find_elements(By.XPATH,"/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div")
for li in li_list:
    job_name=li.find_element(By.XPATH,'./div[1]/div[1]/div[1]/a').text
    #/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]
    #/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[1]/div[1]/a
    #/html/body/div[1]/div[2]/div/div[2]/div[3]/div/div[1]/div[1]/div[1]/div[2]/div[1]/a
    job_price=li.find_element(By.XPATH,'./div[1]/div[1]/div[2]/span').text
    company_name=li.find_element(By.XPATH,'./div[1]/div[2]/div[1]/a').text
    print(job_price,job_name,company_name)