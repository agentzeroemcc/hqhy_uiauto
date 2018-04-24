# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from selenium.webdriver.support.ui import Select
from Oms_Navigation_management.Global_navigation import Global


# api地址管理
class api_addres(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Add_to(self):
        """新增"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.jc_peizhi()  # 点击基础配置
        homepage.api_address()  # 点击api地址管理
        homepage.newly_added()  # 点击新增
        Select(driver.find_element_by_name('serviceComboCode')).select_by_value('1100121022001790197750001')  # 选择山东移动
        time.sleep(1)
        self.test_name = 'AgentZero测试'
        homepage.add_names(self.test_name)  # 输入API名称
        test_name2 = 'contextConfigLocation666'
        homepage.attribute_value(test_name2)  # 输入API地址
        homepage.preservation4()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '新增成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        api_name = driver.find_element_by_xpath('//*[@id="apiurl_table"]/tbody/tr[4]/td[4]').text  #  获取api名称
        api_add = driver.find_element_by_xpath('//*[@id="apiurl_table"]/tbody/tr[4]/td[5]').text   #  获取api地址
        try:
            assert api_name == self.test_name and api_add == test_name2
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()


    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.test_name = 'AgentZero测试'
        homepage.edit()  # 点击编辑
        homepage.add_names('编辑')  # 输入名称
        homepage.preservation4()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '修改成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定

        new_name = driver.find_element_by_xpath('//*[@id="apiurl_table"]/tbody/tr[4]/td[4]').text
        try:
            self.assertEqual(self.test_name+'编辑',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.delete2()
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '成功删除1条记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()