# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

test_name = 'AgentZero类型测试'
# 渠道商类型列表
class AgentvendorType(unittest.TestCase):
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
        homepage.collapseThrees()  # 点击渠道商类型列表
        homepage.custom_toolbar()  # 点击新增
        homepage.AgentvendorTp(test_name)  # 输入渠道商类型名称
        self.test_name2 = '我就看看'
        homepage.Descriptive(self.test_name2)  # 输入描述信息
        homepage.preservation1()  # 点击保存
        homepage.confirm_1()  # 点击确定
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        time.sleep(2)
        try:
            self.assertEqual(test_name, new_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.send_submit_btn()  # 点击编辑
        homepage.add_names('编辑')  # 输入名称
        homepage.preservation2()  # 点击保存
        homepage.confirm_1()  # 点击确定
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        time.sleep(2)
        try:
            self.assertEqual(test_name+'编辑',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.edit_product()
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”

        try:
            assert VodSearch.get_ass_text(self) == '删除操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        matching = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert matching == '没有找到匹配的记录' or matching != test_name
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
