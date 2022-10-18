import time
from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
d = DesiredCapabilities.CHROME
d['goog:loggingPrefs'] = {'browser': 'ALL'}
options=webdriver.ChromeOptions()
driver = webdriver.Chrome(desired_capabilities=d,chrome_options=options)

# driver.get('http://www.baidu.com')
driver.get(url='http://127.0.0.1:8080/web%E4%BD%9C%E4%B8%9A4/toutiao%20.html')

# driver.set_window_size(800, 700)  # 设置浏览器的宽和高，以便出现滚动条


# time.sleep(10)
# js = 'window.scrollTo(100,400);'  # 设置浏览器窗口滚动条的水牌位置和垂直位置
max_time='1637201727723'
js="""
	function get_signature(max_time){
				var i={url:"https://www.toutiao.com/api/pc/list/user/feed?category=pc_profile_ugc&token=MS4wLjABAAAAZ4Hwu5YDysuwNnR85W69NIETIiucQctQRaxwxXneD18&max_behot_time="+max_time+"&aid=24&app_name=toutiao_web"}
				var a=window.byted_acrawler;
				console.log("是滴哦v考虑");
				console.log(a);
				console.log(i);
				var r=a.sign;
				console.log(r);
				console.log(r.call(a,i));
				console.log(i.url+'&_signature='+r.call(a,i))
				return r.call(a,i);
			}

            var max_time='%d';

			console.log(get_signature(max_time));
			"""%(int(max_time))
# print(js)
# print(driver.get_log("browser"))
# # time.sleep(10)
#
# print(driver.get_log("browser"))
driver.execute_script(js)  # 调用/执行js语句的方法
list=driver.get_log("browser")
print(list)
print(len(list))
print(list[9]['message'])
# print(driver.get_log("browser")[5])
url=list[9]['message'].split('"')[1]
print(url)
# driver.quit()
