import base64
import time
import requests
from selenium.common import exceptions
from jsonpath import jsonpath
from selenium import webdriver


def check_beauty():
    api_key = ''
    secret_key = ''
    url = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=' + api_key + '&client_secret=' + secret_key
    get_acces_token = requests.get(url).json()
    acces_token = jsonpath(get_acces_token, '$..access_token')[0]
    with open('screenshot.png', 'rb') as f:
        base64_data = base64.b64encode(f.read())
    request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
    post_data = {
        "image": base64_data,
        "image_type": "BASE64",
        "face_field": "gender,age,beauty,gender",
        "face_type": "LIVE"
    }
    headers = {
        "Content-Type": "application/json;"
    }
    age, beauty, gender = 0, 0, 'male'
    try:
        request_url = request_url + "?access_token=" + acces_token
        response = requests.post(url=request_url, data=post_data, headers=headers)
        json_result = response.json()
        error_msg = jsonpath(json_result, '$..error_msg')[0]
        if error_msg == 'SUCCESS':
            age = jsonpath(json_result, '$..age')[0]
            beauty = jsonpath(json_result, '$..beauty')[0]
            gender = jsonpath(json_result, '$..type')[0]
        else:
            print('未识别到人脸')
            return False
        if int(age) <= 30 and int(beauty) >= 60 and gender == 'female':
            return True
        else:
            return False
    except:
        pass


class DouyinDown:
    def __init__(self):
        options = webdriver.ChromeOptions()
        self.webdriver = webdriver.Chrome(options=options)
        self.down_url = ''
        self.url_title = ''

    def get_downurl_web(self):

        driver = self.webdriver
        driver.implicitly_wait(10)
        driver.get('https://www.douyin.com/recommend')
        input('请手动登录继续，完成后输入任意键')
        while True:
            time.sleep(4)
            driver.find_element_by_xpath(
                '//*[@id="root"]/div/div[2]/div[2]/div/div/div/div[2]').screenshot(
                'screenshot.png')
            state_code = check_beauty()
            try:
                if state_code is True:
                    driver.find_element_by_xpath('//*[@id="root"]//div[2]/div/div[2]/div[1]/div[2]').click()
                    url = driver.find_element_by_xpath('//*[@id="root"]//video').get_attribute('src')
                    url_name_elenment = driver.find_elements_by_xpath('//*[@id="root"]//span/span/span/span/span')
                    url_name_group = []
                    for i in url_name_elenment:
                        url_name_group.append(i.text)
                    url_name = '_'.join(url_name_group)
                    print('下载中...')
                    self.down_url = url
                    self.url_title = url_name
                    self.down_video_web()
                elif state_code is False:
                    print('跳过')
                    pass
                driver.find_element_by_xpath('//*[@id="root"]//xg-bar[3]/div[1]/div/div/div[2]').click()
            except exceptions.StaleElementReferenceException:
                print('元素被刷新,下一个')
                driver.find_element_by_xpath('//*[@id="root"]//xg-bar[3]/div[1]/div/div/div[2]').click()
            except Exception as msg:
                print(msg)
                print('异常')
                input('请完成验证码后继续')

    def down_video_web(self):
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.107 Safari/537.36'
        }
        video_url = self.down_url
        viede_name = self.url_title
        video_content = requests.get(video_url, headers=headers).content
        with open(viede_name + '.mp4', 'wb') as data:
            data.write(video_content)
            print('下载成功')


if __name__ == '__main__':
    DouyinDown().get_downurl_web()