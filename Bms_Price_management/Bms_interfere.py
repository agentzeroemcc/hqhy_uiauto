# -*- coding:utf-8 -*-
import configparser     #处理ini文件
import os.path
import urllib.request,re,json
from framework.logger import Logger
from pageobjects.cibn_homepage import HomePage
# from Vod_Product_management.Product_pack_list import Product

logger = Logger(logger="BrowserEngine").getlog()


class Interface(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    def vod_api_browser(self):
        homepage = HomePage(self.driver)
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        vod_api_url = config.get("testServer", "vod_api_URL")
        logger.info("The test server url is: %s" % vod_api_url)
        get_url = urllib.request.urlopen(vod_api_url).read()
        Code = get_url.decode('utf-8')
        ret = json.loads(Code)
        device_id = ret["retCode"]
        if device_id == '00000000':
            prod = re.findall('.*?"productName":"(.*?)"', Code)
            join = ''.join(prod)
            try:
                assert join == '大面曹天'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()