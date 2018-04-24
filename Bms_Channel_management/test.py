# -*- coding:utf-8 -*-
from appium import webdriver
import configparser     #处理ini文件
import os.path
import urllib.request,re,json
from framework.logger import Logger
from pageobjects.cibn_homepage import HomePage

# logger = Logger(logger="BrowserEngine").getlog()
# package_price_URL = 'http://10.3.1.107:8801/bms_api/order!getOrderList?serviceComboCode=1100121022149038548320021&userCode=1300110106015287504110012'
# get_url = urllib.request.urlopen(package_price_URL).read()
# Code = get_url.decode('utf-8')
# ret = json.loads(Code)
# prod = ret["resultBody"]['rows'][0]['policyName']#coding=utf-8
from appium import webdriver
# print(prod)

# path1 = os.path.abspath('.')  # 获取当前脚本所在的路径
# path2 = os.path.abspath('..')  # 获取当前脚本所在路径的上一级路径
# print(path1)
# print(path2)
#
# # homepage.servicegrouping()
# path = os.path.abspath('..') + "\\All_pictures\\2.jpg"
# print(path)
# # driver.find_element_by_id('pictureFile').send_keys(path)

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['platformVersion'] = '6.0'
desired_caps['deviceName'] = 'Android Emulator'
desired_caps['appPackage'] = 'com.android.calculator2'
desired_caps['appActivity'] = '.Calculator'

driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.find_element_by_name("1").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("delete").click()

driver.find_element_by_name("9").click()

driver.find_element_by_name("5").click()

driver.find_element_by_name("+").click()

driver.find_element_by_name("6").click()

driver.find_element_by_name("=").click()

driver.quit()