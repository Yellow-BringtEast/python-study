from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
from PIL import Image
from lxml import etree
from typing import TypeVar

import time
import random
import requests
import json

# 无头模式
chrome_option = Options()
chrome_option.headless = True
chrome_option.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/103.0.5060.114 Safari/537.36")
# 解决无头模式滑块图片截图不全的问题
chrome_option.add_argument("-window-size=1920,1080")
chrome_option.add_argument("--start-maximized")

driver = webdriver.Chrome(options=chrome_option)

# 登录及搜索地址
LOGIN_URL = 'https://www.tianyancha.com/'
SEARCH_URL = 'https://www.tianyancha.com/search?key='

# 账号信息
ACCOUNT = ''
PWD = ''

Json = TypeVar('Json')


class GetCookies:
    """
    使用selenium自动登录天眼查，获取cookies
    """

    def __init__(self, account: str = ACCOUNT, pwd: str = PWD, is_headless: bool = True) -> None:
        """
        初始化参数
        :param account: 天眼查账号
        :param pwd: 天眼查密码
        :param is_headless: 是否启用无头模式
        """
        self.account = account
        self.pwd = pwd

        if (is_headless == False):
            global driver
            driver = webdriver.Chrome()

    @staticmethod
    def compare_images(image_be, image_af, i: int, j: int, threshold: int = 60) -> bool:
        """
        判断两张图片相同位置的像素之间是否存相同
        :param image_be: 图片一
        :param image_af: 图片二
        :param i: 行
        :param j: 列
        :param threshold: 像素差异的阈值，低于阈值不认为存在差异
        :return: 是否相同
        """

        # 获取两种图片相同位置的像素的RGB值
        pixel_be = image_be.load()[i, j]
        pixel_af = image_af.load()[i, j]

        # 判断两个像素之间是否相同，差异低于阈值视为相同
        if all([abs(pixel_be[m] - pixel_af[m]) < threshold for m in range(3)]):
            return True
        else:
            return False

    def get_cookies(self) -> dict:
        """
        登录天眼查，获取cookies
        :return: cookies
        """
        # 打开页面
        driver.get(LOGIN_URL)

        driver.maximize_window()

        # 点击登录按钮
        time.sleep(random.random() * 2.5)
        login_bnt = driver.find_element(By.CLASS_NAME, 'treasure_nav-link__7ErdH')
        login_bnt.click()

        # 切换登录方式
        time.sleep(random.random() * 2.5)
        login_change = driver.find_element(By.CLASS_NAME, 'login-toggle')
        login_change.click()

        # 切换至密码登录
        time.sleep(random.random() * 2.5)
        login_pwd = driver.find_element(By.CLASS_NAME, 'title-password')
        login_pwd.click()

        # 输入账号
        time.sleep(random.random() * 2.5)
        input_account = driver.find_element(By.XPATH,
                                            '//*[@id="J_Modal_Container"]/div/div/div[2]/div/'
                                            'div[2]/div/div/div[3]/div[2]/div[1]/input')
        input_account.send_keys(self.account)

        # 输入密码
        time.sleep(random.random() * 2.5)
        input_pwd = driver.find_element(By.XPATH,
                                        '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]'
                                        '/div/div/div[3]/div[2]/div[2]/input')
        input_pwd.send_keys(self.pwd)

        # 登录
        time.sleep(3)
        login = driver.find_element(By.XPATH,
                                    '//*[@id="J_Modal_Container"]/div/div/div[2]/div/div[2]/div/'
                                    'div/div[3]/div[2]/button')
        login.click()

        # 处理滑块验证码
        # 获取不带缺口的验证码图片
        time.sleep(5)
        img = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[1]/div[2]/div[1]')
        location = img.location
        size = img.size

        # 得到图片坐标
        top, bottom, left, right = location['y'], location['y'] + size['height'], location['x'], \
                                   location['x'] + size['width']

        # 截取滑块验证码完整图片
        screen_shot = driver.get_screenshot_as_png()
        screen_shot = Image.open(BytesIO(screen_shot))
        img_be = screen_shot.crop((int(left), int(top), int(right), int(bottom)))
        # img_be.save('./be.png')

        # 点击滑块，获取带缺口的验证码图片
        time.sleep(random.random() * 2.5)
        slider = driver.find_element(By.XPATH, '/html/body/div[4]/div[2]/div[2]/div[2]/div[2]')
        ActionChains(driver).click_and_hold(slider).perform()
        time.sleep(3)

        # 截取滑块验证码完整图片
        screen_shot = driver.get_screenshot_as_png()
        screen_shot = Image.open(BytesIO(screen_shot))
        img_af = screen_shot.crop((int(left), int(top), int(right), int(bottom)))
        # img_af.save('./af.png')

        # 对比滑块图片像素差异，获取滑块滑动距离
        # 从滑块右侧开始逐一对比寻找缺口
        left = 57
        has_find = False

        for i in range(left, img_be.size[0]):
            if has_find:
                break
            for j in range(img_be.size[1]):
                if not self.compare_images(img_be, img_af, i, j):
                    left = i
                    has_find = True
                    break

        # 滑块移动距离
        move = left - 9

        # 移动滑块，完成登录
        ActionChains(driver).move_by_offset(move, 0).perform()
        ActionChains(driver).pause(3).perform()
        ActionChains(driver).release().perform()

        # 获取cookies
        time.sleep(4)
        cookies_list = driver.get_cookies()
        cookies_dict = {}
        for cookie in cookies_list:
            cookies_dict[cookie['name']] = cookie['value']

        with open('./cookies.txt', 'w') as f:
            f.write(str(cookies_dict))

        return cookies_dict

    def get_cookies_dict(self) -> dict:
        """
        出现错误时进行重试，保证获取到的cookie有效
        :return: cookies
        """
        while True:
            try:
                cookies_dict = self.get_cookies()
                if 'tyc-user-info' in cookies_dict.keys():
                    driver.close()
                    print('登录成功！')
                    break
                else:
                    driver.refresh()
                    print('登录失败，正在重试！')
            except Exception as e:
                driver.refresh()
                print(e)
        return cookies_dict


class GetCompanyInfo:
    """
    根据企业名称，获取企业注册地址，注册资本等信息
    """

    def __init__(self, cookies_dict, company_name: str = None):
        """
        初始化参数
        :param company_name: 公司名称
        :param cookies_dict: cookies
        """
        self.company_name = company_name
        self.cookies = cookies_dict
        self.headers = {
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                          'Chrome/103.0.5060.114 Safari/537.36',
            'authority': 'www.tianyancha.com',
            'method': 'GET',
            'path': f'/search?key={self.company_name}'.encode('utf-8'),
            'scheme': 'https',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,'
                      '*/*;q=0.8,application/signed-exchange;v=b3;q=0.9 '
        }

    def get_company_url(self) -> str:
        """
        根据企业名称获取企业天眼查地址
        :return: 企业天眼查地址
        """
        # 搜索公司信息的地址
        url = SEARCH_URL + self.company_name
        headers = self.headers

        # 获取企业天眼查地址
        re = requests.get(url=url, headers=headers, cookies=self.cookies)
        html = etree.HTML(re.text)
        company_url = html.xpath('//*[@class="index_alink__zcia5 link-click"]/@href')[0]

        return company_url

    def get_company_info(self, company_url=None) -> Json:
        """
        爬取企业天眼查地址中的有关信息
        :param company_url: 企业天眼查地址
        :return: 企业有关工商信息json
        """
        # 企业天眼查地址
        if company_url is None:
            company_url = self.get_company_url()

        headers = self.headers
        headers['path'] = f"/company/{company_url.split('/')[-1]}".encode('utf-8')

        re = requests.get(url=company_url, headers=headers, cookies=self.cookies)
        html = etree.HTML(re.text)

        company_info = html.xpath('//*[@id="__NEXT_DATA__"]/text()')[0]
        company_info_json = json.loads(company_info)

        # 获取企业各类信息
        data = company_info_json['props']['pageProps']['dehydratedState']['queries'][0]['state']['data']['data']

        return data


if __name__ == '__main__':
    # 自动登录获取cookies
    cookies = GetCookies(ACCOUNT, PWD, is_headless=False).get_cookies_dict()

    # 获取企业信息
    com_data = GetCompanyInfo(cookies, '上海蔚来汽车').get_company_info()
    print(com_data)
