# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Oms_Navigation_management.Global_navigation import Global

#升级详情
class Upgrade_detail(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_search(self):
        """搜索"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.busines_com()  # 点击业务组合
        homepage.collapseThrees()  #  点击升级详情
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value(
            '1100121023874101446610014')  # --选择业务组合--   福建联通
        mac_addres = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  #  获取MAC地址
        apk_edition = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[9]').text  #  获取APK版本
        homepage.searchBtn()  #  点击搜索
        homepage.intomac(mac_addres)  #  输入MAC
        homepage.apkVersionSeq(apk_edition)  #  输入apk
        homepage.searchByName()  #  点击搜索
        after_mac = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  #  获取搜索后的MAC地址
        after_apk = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text  #  获取搜索后的apk版本
        try:
            assert after_mac == mac_addres and after_apk == apk_edition
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()  #  点击重置
        mac = driver.find_element_by_xpath('//*[@id="mac"]').text
        apk = driver.find_element_by_xpath('//*[@id="apkVersionSeq"]').text
        try:
            assert mac == '' and apk == ''
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
