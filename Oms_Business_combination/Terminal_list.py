# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

#终端列表
class TerninalList(unittest.TestCase):
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
        homepage.collapseTwo2()  #  点击终端列表
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value( '1100121023874101446610014')  # --选择业务组合--   福建联通
        mac_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  #  获取MAC地址
        homepage.searchBtn()  #  点击搜索
        homepage.intomac(mac_name)  #  输入MAC地址
        homepage.searchByName()  #  点击搜索
        search_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  #  获取搜索后的名称
        try:
            assert search_name == mac_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_enable_disable(self):
        """启用/停用"""
        driver = self.driver
        homepage = HomePage(self.driver)
        """停用"""
        homepage.terminal_edit()  #  点击  停用/启用
        driver.switch_to_alert().accept()  #  锁定弹出框选择确定
        try:
            assert VodSearch.get_ass_text(self) == '终端停用成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[12]').text  #  获取状态
        try:
            assert state == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """启用"""
        homepage.terminal_edit()  # 点击  停用/启用
        driver.switch_to_alert().accept()  # 锁定弹出框选择确定
        try:
            assert VodSearch.get_ass_text(self) == '终端启用成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        state1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[12]').text  #  获取状态
        try:
            assert state1 == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Handoff_service(self):
        """切换业务组合"""
        homepage = HomePage(self.driver)
        driver = self.driver
        edit_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取名称
        homepage.unbound_edit()  #  点击切换业务组合
        driver.switch_to_alert().accept()
        Select(driver.find_element_by_xpath('//*[@id="change_servicecombo_form"]/div[1]/div/select')).select_by_value('1100121106014108498720071')  # 选择业务组合  KS业务组合测试（勿动！）
        homepage.change_servicecombo_form()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '切换业务组合成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value( '1100121106014108498720071')  # 选择业务组合  KS业务组合测试（勿动！）
        handoff_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取切换后的名称
        try:
            assert handoff_name == edit_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Unbound(self):
        """解除绑定"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.unbound_edit1()  #  点击解除绑定
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '解除绑定成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        pipei = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert pipei == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()  #  重置
        mac_name = driver.find_element_by_xpath('//*[@id="mac"]').text  #获取MAC地址输入框
        try:
            assert mac_name == ''
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
