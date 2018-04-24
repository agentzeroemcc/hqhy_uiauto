# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch

#分发域绑定
class Distribution(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_New_service(self):
        """新增业务分组"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()      #点击业务分组
        homepage.collapseOnes() #点击’分发域绑定‘按钮
        Select(driver.find_element_by_id('allServiceGroup')).select_by_value('1100122106018099388980003')  #  选择业务分组  KS配置预览自动化测试（勿动）
        time.sleep(1)
        homepage.custom_toolbar()       #点击新增
        value = driver.find_element_by_xpath('//*[@id="domaincode"]/option[9]').text
        Select(driver.find_element_by_id('domaincode')).select_by_value('2100090106019242386300101')  #  分发域测试（测试勿动）
        homepage.domain_form()  #点击绑定
        try:
            assert VodSearch.get_ass_text(self) == '绑定成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()   #确认
        text_center = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            assert text_center == value
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.custom_toolbar()  # 点击新增
        value1 = driver.find_element_by_xpath('//*[@id="domaincode"]/option[5]').text
        Select(driver.find_element_by_id('domaincode')).select_by_value('2100090023831778866170007')  #  山东移动CDN分发域
        homepage.domain_form()  # 点击绑定
        try:
            assert VodSearch.get_ass_text(self) == '绑定成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()  # 确认
        text_center1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert text_center1 == value1
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Priority_up(self):
        """优先级上移"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.servicegrouping()  # 点击业务分组
        # homepage.collapseOnes()  # 点击’分发域绑定‘按钮
        # Select(driver.find_element_by_id('allServiceGroup')).select_by_value('1100122106019578867330134')
        # time.sleep(1)
        domain = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#山东
        domain1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text#测试
        encoding = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]').text
        homepage.tab_Deta()#点击上移按钮
        try:
            assert VodSearch.get_ass_text(self) == '分发域：' + encoding + ',优先级已经上移完毕。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()   #确认
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#测试
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        try:
            assert text == domain1 and text1 == domain
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Unbound(self):
        """解除绑定"""
        homepage = HomePage(self.driver)
        driver = self.driver
        try:
            checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
            for checkbox in checkboxes:
                checkbox.click()
        except Exception as e:
            print(e)
        time.sleep(2)
        homepage.customtoolbar()#点击解除绑定
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        time.sleep(3)
        try:
            assert VodSearch.get_ass_text(self) == '解除绑定成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认
        matching = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert matching == '没有找到匹配的记录'
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
