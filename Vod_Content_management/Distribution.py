# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface

#分发域媒资
test_name = '大面曹天'
cp_name = '优酷媒资'

class Domain(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Program_up(self):
        """分发域媒资上线"""
        VodSearch.test_Sign_in(self)#登录
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击内容管理
        homepage.dj_fenfayu()#分发域媒资按钮
        Select(self.driver.find_element_by_id('selectDomain')).select_by_value('2100090022055992407651202') #选择“江苏移动CDN分发域”
        time.sleep(1)
        homepage.searchBtn()    #点击搜索按钮
        Select(self.driver.find_element_by_id('status')).select_by_value('2')   #选择“下线”
        time.sleep(2)
        Select(self.driver.find_element_by_id('flowStatus')).select_by_value('2000')  # 选择“处理成功”
        time.sleep(2)
        initial = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text   #获取初始节目名称
        homepage.table_input()#点击对勾
        homepage.online_1()#点击上线按钮
        try:
            self.assertEqual("上线成功", VodSearch.get_ass_text(self))
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.ffy_sx_queding()#上线确定按钮
        homepage.add_names(initial)#输入上线名称
        Select(self.driver.find_element_by_id('status')).select_by_visible_text('全部')  # 选择“全部”
        time.sleep(2)
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        try:
            assert text == initial and text1 == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Program_down(self):
        """分发域媒资下线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()#点击重置
        Select(self.driver.find_element_by_id('selectDomain')).select_by_value('2100090022055992407651202')  # 选择“江苏移动CDN分发域”
        time.sleep(1)
        Select(self.driver.find_element_by_id('status')).select_by_value('1')  # 选择“上线”
        time.sleep(2)
        initial = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始节目名称
        homepage.table_input()  # 点击对勾
        homepage.offline()  # 点击下线按钮
        try:
            self.assertEqual("下线成功", VodSearch.get_ass_text(self))
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.ffy_sx_queding()  # 下线确定按钮
        homepage.add_names(initial)  # 输入上线名称
        Select(self.driver.find_element_by_id('status')).select_by_visible_text('全部')  # 选择上下线状态“全部”
        time.sleep(3)
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        try:
            assert text == initial and text1 == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Search(self):
        """分发域媒资搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()#点击重置
        font_list = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]').text     #节目集名称
        font = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text    #节目名称
        font_code = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text    #节目集CODE
        homepage.seriesName(font_list)
        homepage.add_names(font)
        homepage.seriescode(font_code)
        homepage.searchByContentName()
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        test2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert test == font_list and test1 == font and test2 == font_code
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()

    def test_online_interface(self):
        """节目上线接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.seriesName(test_name)  #  输入节目集名称
        homepage.searchByContentName()  #  点击搜索
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        if state == '上线':
            Interface.Program_online(self)
            time.sleep(2)
        elif state == '下线':
            Interface.Program_downline(self)
            homepage.table_input()  # 点击复选
            homepage.online_1()  #  点击上线按钮
            homepage.ffy_sx_queding()  # 点击确认
            Interface.Program_online(self)
            time.sleep(2)
        else:
            homepage.get_windows_img()

    def test_downline_interface(self):
        """节目下线接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  # 获取状态
        if state == '上线':
            homepage.table_input()  #  点击复选
            homepage.offline()  # 点击下线按钮
            # homepage.ffy_sx_queding()  # 点击确定
            homepage.ffy_sx_queding()  # 点击确认
            Interface.Program_downline(self)
            time.sleep(2)
            homepage.table_input()  # 点击复选
            homepage.online_1()  # 点击上线按钮
            homepage.ffy_sx_queding()  # 点击确认
        else:
            homepage.get_windows_img()

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
