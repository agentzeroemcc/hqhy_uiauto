# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Oms_Navigation_management.Global_navigation import Global

#终端列表
class List_terminal(unittest.TestCase):
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
        homepage.dj_chanpguanl()  # 点击终端管理
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value(
            '1100121023874101446610014')  # --选择业务组合--   福建联通
        time.sleep(2)
        mac_addres = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]').text  #  获取MAC地址
        Terminal_rule = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  #  获取终端规则
        homepage.searchBtn()  #  点击搜索
        homepage.intomac(mac_addres)  #  输入MAC
        homepage.searchDiv_lable()  #  点击终端规则
        homepage.searchDiv_lable_input(Terminal_rule)  #  输入终端规则
        homepage.searchDiv_lable_input(Keys.ENTER)  #
        homepage.searchByName()  #  点击搜索
        after_mac = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[1]').text  #  获取搜索后的MAC地址
        after_Terminal = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  #  获取搜索后的apk版本
        try:
            assert after_mac == mac_addres and after_Terminal == Terminal_rule
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
        # apk = driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/button/span[1]').text
        try:
            assert mac == ''
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Advanced_search(self):
        """高级搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        mac_addres = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]').text  # 获取MAC地址
        homepage.searchMore()  #  点击高级搜索
        homepage.search_mac(mac_addres)  #  输入MAC
        Select(driver.find_element_by_id('search_vendorCode')).select_by_value('1100041160113100000031864')  # --选择终端厂商：  国广东方网络(北京)有限公司
        time.sleep(1)
        Select(driver.find_element_by_id('search_typeCode')).select_by_value(
            '1100104023147339779990003')  # --选择终端型号：  E950
        time.sleep(1)
        Select(driver.find_element_by_id('search_chipVendorCode')).select_by_value(
            '1100103023147340778390004')  # --选择芯片厂商：  优酷创维终端mstar
        time.sleep(1)
        Select(driver.find_element_by_id('search_deviceRuleCode')).select_by_value(
            '1100107106019399191717571')  # --选择终端规则：  mac文件绑定测试
        time.sleep(1)
        Select(driver.find_element_by_id('search_status')).select_by_value(
            '1')  # --选择状态： 未激活
        time.sleep(1)
        homepage.dj_sous()  #  点击搜索
        after_mac = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[1]').text  # 获取搜索后的MAC地址
        try:
            assert after_mac == mac_addres
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