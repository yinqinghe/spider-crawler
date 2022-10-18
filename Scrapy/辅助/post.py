from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = {'browser': 'ALL'}

driver = webdriver.Chrome(desired_capabilities=d)
driver.maximize_window()
driver.get(url='http://127.0.0.1:8080/web%E4%BD%9C%E4%B8%9A4/toutiao%20.html')

print(driver.get_log("browser"))