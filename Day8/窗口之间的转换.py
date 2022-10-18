from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
web=Chrome()
web.get("https://www.lagou.com/")
web.find_element(By.XPATH,'//*[@id="changeCityBox"]/ul/li[2]/a').click()
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="search_input"]').send_keys("python",Keys.ENTER)
time.sleep(1)
web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[1]/div[1]/div[1]/div[1]/a').click()
web.switch_to.window(web.window_handles[-1])
job_detail=web.find_element(By.XPATH,'//*[@id="job_detail"]/dd[2]/div').text
print(job_detail)
# web.close()
#
# web.switch_to.window(web.window_handles[0])
print(web.find_element(By.XPATH,'//*[@id="jobList"]/div[1]/div[5]/div[1]/div[1]/div[1]/a').text)