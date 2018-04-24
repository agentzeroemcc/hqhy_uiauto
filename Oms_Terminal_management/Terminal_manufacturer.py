# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

#终端厂商列表
class Manufacturer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Newly_added(self):
        """新增"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_chanpguanl()  # 点击终端管理
        homepage.collapseOne()  #  点击终端厂商列表
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  #  获取名称
        describe = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  #  获取描述
        homepage.custom_toolbar()  #  点击新增
        homepage.create_vendor_form(name + '（测试）')  #  输入终端厂商名称
        Select(driver.find_element_by_name('status')).select_by_value('2')   #  状态选择停用
        homepage.create_vendor_form_textarea(describe)  #  输入描述
        homepage.create_vendor_form_button()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '添加操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认

    def test_search(self):
        """搜索"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_chanpguanl()  # 点击终端管理
        homepage.collapseOne()  # 点击终端厂商列表
        homepage.search_name('创佳')  #  输入厂商名称
        homepage.searchByName()  #  点击搜索
        search_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  #  获取匹配名称
        try:
            assert search_name == '创佳'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  # 获取匹配名称
        describe = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text  # 获取描述
        homepage.dj_edits()  #  点击编辑
        homepage.clear_names()  #  清除名称
        homepage.add_names(name + '（编辑）')  #  输入名称
        Select(driver.find_element_by_id('status')).select_by_value('1')  # 状态选择启用
        homepage.clear_description()  #  清除描述
        homepage.description(describe + '（编辑）')  #  输入描述
        homepage.edit_vendor_form()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '编辑操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        edit_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  # 获取编辑后的名称
        edit_state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取编辑后状态
        edit_describe = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text  # 获取编辑后描述
        try:
            assert edit_name == name + '（编辑）' and edit_state == '启用' and edit_describe == describe + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.dj_edits()  # 点击编辑
        homepage.clear_names()  # 清除名称
        homepage.add_names(name)  # 输入名称
        homepage.clear_description()  # 清除描述
        homepage.description(describe)  # 输入描述
        homepage.edit_vendor_form()  # 点击保存
        homepage.confirm_1()  # 确认


    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
