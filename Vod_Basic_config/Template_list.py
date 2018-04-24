# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch

#模板列表
class Template(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Newly_added(self):
        """新增"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.jc_peizhi()   #点击基础配置
        homepage.collapseThrees()#点击模板列表
        homepage.custom_toolbar()#点击新增
        homepage.add_names('001')
        homepage.templateName('HQHY')
        homepage.templateFileSubmit()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '新增模板成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert text == '001'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.edit_table()#点击编辑
        homepage.add_names('（编辑）')#输入名称
        Select(driver.find_element_by_id('isUse')).select_by_value('1')
        homepage.templateFileSubmit()#点击保存
        try:
            assert VodSearch.get_ass_text(self) == '更新模板成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        try:
            assert name == test+'（编辑）' and state == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_input()#点击对勾
        homepage.deleteTemplateFileBtn()#点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '已删除[1]条,删除失败[0]条'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
