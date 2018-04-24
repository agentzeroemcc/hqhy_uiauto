# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from selenium.webdriver.support.ui import Select
from Oms_Navigation_management.Global_navigation import Global

# 权限管理
test_name = '权限管理测试'
class Permission(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Newly_build(self):
        """新建"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.recommend()  # 点击用户权限
        homepage.dj_fenfayu()  #  点击权限管理
        homepage.custom_new_toolbar()  #  点击新建
        homepage.authName(test_name)  #  输入权限名称
        driver.find_element_by_xpath('//*[@id="myForm"]/div[3]/div/input').send_keys('测试专属')
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="myForm"]/div[4]/div/textarea').send_keys('/navigation/update')
        time.sleep(1)
        homepage.opt_btn()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '添加成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定

    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.NsearchName(test_name)  #  输入权限名称
        homepage.searchButton()  #  点击搜索
        jur_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[2]').text  #  获取权限名称
        oms_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[3]').text  #  获取权限名称
        describe = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[4]').text  #  获取权限名称
        try:
            assert jur_name == test_name and oms_name == 'OMS' and describe == '测试专属'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/span[2]').click()  #  点击编辑
        homepage.sleep(2)
        homepage.clear_authName()  #清空权限名称
        homepage.authName(test_name + '（编辑）')  #输入编辑
        homepage.opt_btn()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '修改成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        homepage.NsearchName(test_name)  #  输入权限名称
        homepage.searchButton()  #  点击搜索
        edit_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[2]').text
        try:
            assert edit_name == test_name + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[1]/span[3]').click()  #  点击删除按钮
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功删除1个权限'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        homepage.NsearchName(test_name + '（编辑）')  # 输入权限名称
        homepage.searchButton()  # 点击搜索

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="searchForm"]/div[2]/button[2]').click()  #  点击重置
        homepage.sleep(2)
        per_name = driver.find_element_by_xpath('//*[@id="searchName"]').text  #  获取权限名称
        try:
            assert per_name == ''
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








