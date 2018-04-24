# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from selenium.webdriver.support.ui import Select
from Oms_Navigation_management.Global_navigation import Global


# 角色管理
test_name = 'AgentZero测试'
class Role_manage(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Add_to(self):
        """新建"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.recommend()  # 点击用户权限
        homepage.collapseOnes()  # 点击角色管理
        homepage.newly_added()  # 点击新建
        homepage.type_role1(test_name)  # 输入角色名称
        homepage.preservation4()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '添加成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确认



    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.type_role2(test_name)  # 输入内容
        homepage.click_search()  # 点击搜索

        ass_name1 = driver.find_element_by_xpath('//*[@id="role_table"]/tbody/tr/td[3]').text
        try:
            assert ass_name1 == test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()


    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.click_edit2()  # 点击编辑
        homepage.type_role1('编辑')  # 输入名称
        homepage.preservation4()  # 点击保存
        homepage.confirm_1()  # 点击确定
        new_name = driver.find_element_by_xpath('//*[@id="role_table"]/tbody/tr/td[3]').text
        try:
            self.assertEqual(test_name+'编辑',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_distribution(self):
        """分配权限"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.click_distribution()  # 点击分配权限
        dis_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr[1]/td[2]').text  #  获取权限名称
        homepage.type_role2(dis_name)  # 输入名称
        homepage.click_search()  # 点击搜索
        new_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[2]').text
        try:
            self.assertEqual(dis_name,new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        driver.find_element_by_xpath('//*[@id="1"]').click()  #  点击复选
        time.sleep(2)
        add = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div/span').text  #
        try:
            self.assertEqual('添加成功',add)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        driver.find_element_by_xpath('//*[@id="1"]').click()  # 点击复选
        time.sleep(2)
        delete = driver.find_element_by_xpath( '/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/div/div[2]/div/span').text  #
        try:
            self.assertEqual('删除成功', delete)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())


    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.collapseOnes()  # 点击角色管理
        homepage.type_role2(test_name)  # 输入名称
        homepage.click_search()  # 点击搜索
        homepage.click_del2()  #  点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        sub_name = driver.find_element_by_xpath('//*[@id="role_table"]/tbody/tr/td').text
        try:
            self.assertEqual('没有找到匹配的记录', sub_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.reset_table()  # 点击重置
        input_name = driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/label[2]/input[1]').text
        logon_name = driver.find_element_by_xpath('//*[@id="role_table"]/tbody/tr[1]/td[3]').text
        # logger.info('aaa--%s,bbb--%s' % input_name % logon_name)
        try:
            assert input_name == '' and logon_name == '超级管理员'
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