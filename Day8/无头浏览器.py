from selenium.webdriver import Chrome
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.chrome.options import Options
import time


opt=Options()
opt.add_argument("--headless")
opt.add_argument("--disable-gpu")
web=Chrome(options=opt)

web.get("https://ys.endata.cn/BoxOffice/Overseas")

time.sleep(2)
# sel_el=web.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/ul')
# sel=Select(sel_el)
# for i in range(len(sel.options)):
#     sel.select_by_index(i)
#     time.sleep(2)
#     table=web.find_element(By.XPATH,'//*[@id="app"]/section/main/div/div[1]/div/section/section/section/div[1]/div[3]/table')
#     print(table.text)
#     print("=====================================")
#
# print("运行完毕。 ")
# web.close()

print(web.page_source)