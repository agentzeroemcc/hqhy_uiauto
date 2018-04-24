# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

# 系统属性组管理
class System_attribute_group(unittest.TestCase):
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
        homepage.system_attribute_group()  # 点击系统属性组管理
        homepage.add_recomm()  # 点击新增
        self.test_name = 'AgentZero测试'
        homepage.add_names(self.test_name)  # 输入属性组名称
        self.test_name2 = 'Just see  see'
        homepage.remarks(self.test_name2)  # 输入备注信息
        homepage.newly_build1()  # 点击新建
        try:
            assert VodSearch.get_ass_text(self) == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[10]/td[2]').text
        try:
            self.assertEqual(self.test_name, new_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
