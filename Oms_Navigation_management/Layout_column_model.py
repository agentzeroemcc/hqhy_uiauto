# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

test_name = 'A自动化测试品字'
edit_name = test_name+'（编辑）'
#布局列模式
class Layout(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_New_add(self):
        """新增"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击导航管理
        driver.find_element_by_xpath('//*[@id="collapseOne"]/div/ul/li[4]/a').click()  #  点击布局列模式
        time.sleep(2)
        homepage.add_recomm()#点击新增
        homepage.add_names(test_name)#输入列名称
        Select(driver.find_element_by_id('status')).select_by_value('1')  # 下拉选择选择启用
        Select(driver.find_element_by_id('parttern')).select_by_value('31')  # 下拉选择选择品字
        homepage.btnCreates()#点击添加按钮
        homepage.doubleclickbtn()  # 点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本
        try:
            self.assertEqual(test_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Status(self):#状态改变
        """状态改变"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_input()#点击复选框
        homepage.shutdown()#点击停用
        homepage.confirm_1()#点击确认
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text#获取文本
        try:
            self.assertEqual('停用', ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.table_input()  # 点击复选框
        homepage.startup()  # 点击启用
        homepage.confirm_1()  # 点击确认
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text  # 获取文本
        try:
            self.assertEqual('启用', ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.send_submit_btn()#点击编辑、
        homepage.clear_names()#清除文字
        homepage.add_names(edit_name)#输入名称
        Select(driver.find_element_by_id('parttern')).select_by_value('32')  # 下拉选择选择倒品字
        homepage.btnSaves()#点击更新按钮
        homepage.doubleclickbtn()  # 点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本内容
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text#获取文本内容
        try:
            assert ass_name == edit_name and ass_name2 == '倒品字'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Delete(self):
        """删除推布局列"""
        homepage = HomePage(self.driver)
        driver = self.driver
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本内容
        homepage.edit_product()#点击删除按钮
        homepage.confirm_1()#点击确认按钮
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本内容
        try:
            assert ass_name != ass_name1
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Delete_batch(self):
        """批量删除布局列"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.add_recomm()  # 点击新增
        homepage.add_names('Aa'+test_name)  # 输入列名称
        Select(driver.find_element_by_id('status')).select_by_value('1')  # 下拉选择选择启用
        Select(driver.find_element_by_id('parttern')).select_by_value('31')  # 下拉选择选择品字
        homepage.btnCreates()  # 点击添加按钮
        homepage.add_recomm()  # 点击新增
        homepage.add_names('Ab'+test_name)  # 输入列名称
        Select(driver.find_element_by_id('status')).select_by_value('1')  # 下拉选择选择启用
        Select(driver.find_element_by_id('parttern')).select_by_value('32')  # 下拉选择选择倒品字
        homepage.btnCreates()  # 点击添加按钮
        homepage.doubleclickbtn()  # 点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取文本
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text  # 获取文本
        try:
            assert 'Aa'+test_name == ass_name and 'Ab'+test_name == ass_name1
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.table_input()#点击复选框
        homepage.table_input1()#点击复选框
        homepage.remove()#点击删除
        homepage.confirm_1()#点击确认按钮
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取文本
        ass_name3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text  # 获取文本
        try:
            assert ass_name != ass_name2 and ass_name1 != ass_name3
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        driver.quit()

    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     :return:
    #     """
    #     cls.driver.quit()
