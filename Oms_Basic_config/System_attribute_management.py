# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

# 系统属性管理
class System_attribute(unittest.TestCase):
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
        homepage.system_attribute()  # 点击系统属性管理
        homepage.custom_toolbar()  # 点击新增
        self.test_name = 'AgentZero属性测试'
        homepage.add_names(self.test_name)  # 输入属性名称
        test_name2 = '测试'
        homepage.chinese_name(test_name2)  # 输入中文名称
        test_name3 = 'guttv'
        homepage.attribute_value(test_name3)  # 输入属性值
        homepage.newly_build()  # 点击新建
        homepage.confirm_1()  # 点击确定


    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.test_name = 'AgentZero属性测试'
        homepage.search1()  # 点击搜索
        homepage.property_name1(self.test_name)  # 输入内容
        homepage.searchByName()  # 点击搜索
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert ass_name1 == self.test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.clear_Property_name1()  # 清除搜索内容
        homepage.searchMore()  # 点击高级搜索
        homepage.property_name2(self.test_name)  # 输入内容
        homepage.dj_sous()  # 点击搜索

        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert ass_name2 == self.test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()


    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Bj()  # 点击编辑
        homepage.clear_edit_name1()  #  清除内容
        homepage.edit_name1('HQHY')  # 输入名称
        homepage.preservation3()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '编辑操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确认
        # new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[47]/td[6]').text
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[6]').text
        old_name = 'HQHY'
        try:
            self.assertEqual(old_name,new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())


    def test_synchronization(self):
        """同步"""
        homepage = HomePage(self.driver)
        driver = self.driver
        att_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  #  获取属性名称
        homepage.table_Input()  # 点击测试记录按钮
        homepage.custom4_toolbar()  # 点击同步
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            # assert VodSearch.get_ass_text(self) == '属性名称：' + att_name + ' ，同步操作成功!  '
            assert VodSearch.get_ass_text(self) == '属性名称：AgentZero属性测试，同步操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定


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