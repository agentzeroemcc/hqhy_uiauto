# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

# 渠道商列表
class Agentvendor(unittest.TestCase):
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
        homepage.jc_peizhi()  # 点击基础配置
        homepage.custom_toolbar()  # 点击新增
        self.test_name = 'AgentZero测试'
        homepage.add_names(self.test_name)#输入渠道商名称
        test_name2 = 'AZ'
        homepage.AgentvendorAB(test_name2)#输入渠道商缩写
        homepage.sure()#点击确定
        homepage.confirm_1()#点击确定


    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.test_name = 'AgentZero测试'
        homepage.NsearchName(self.test_name)  # 输入内容
        homepage.searchByName()  # 点击搜索
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert ass_name == self.test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.test_name = 'AgentZero测试'
        homepage.send_submit_btn()  # 点击编辑
        homepage.add_names('编辑')  # 输入名称
        homepage.sure()  # 点击确定
        try:
            assert VodSearch.get_ass_text(self) == '添加操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        homepage.NsearchName('编辑')  # 输入内容
        homepage.searchByName()  # 点击搜索
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            self.assertEqual(self.test_name+'编辑',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.glyphicon_edit()
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        matching = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert matching == '没有找到匹配的记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()



