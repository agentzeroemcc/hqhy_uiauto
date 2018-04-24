# -*- coding:utf-8 -*-
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.Interface_test import Interface
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
wallpaper_name = 'The price tag library test'
#价签壁纸库管理
class Price_tag(unittest.TestCase,Interface):
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
        homepage.servicegrouping()  #  点击壁纸管理
        homepage.collapseTwo3()   #    点击价签壁纸库管理
        homepage.add_recomm()   #    点击新增
        homepage.add_names(wallpaper_name)   #    输入壁纸名称
        driver.find_element_by_xpath('//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/button').click()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/div/ul/li[14]/a/span[1]').click()  #  点击福建联通
        time.sleep(1)
        driver.find_element_by_id('pictureFile').send_keys('D:\\prac.jpg')  # 上传图片
        time.sleep(2)
        homepage.btnCreates()   #  点击添加
        # bomb = driver.switch_to_alert().text
        # logger.info(bomb)
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        try:
            assert new_name == wallpaper_name
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        Interface.price_tag_recommend(self)


    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.business_edit()   #   点击编辑
        homepage.add_names('(edit)')  #  编辑名称
        driver.find_element_by_xpath('//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/button').click()
        time.sleep(1)
        driver.find_element_by_xpath(
            '//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/div/ul/li[8]/a/span[1]').click()  # 点击江苏移动
        time.sleep(1)
        homepage.btnSaves()   #   点击更新
        edit_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        try:
            assert edit_name == wallpaper_name + '(edit)'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Business_selection(self):
        """业务组合选择"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('serviceComboCodes')).select_by_value('1100121022149038548320021')  #  选择江苏移动
        time.sleep(2)
        combination = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        logger.info(combination)
        try:
            assert combination == '江苏移动,'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('serviceComboCodes')).select_by_value('1100121106017421817790045')  # 选择江苏移动EPG5.0
        time.sleep(2)
        JSYD_comb = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        try:
            assert JSYD_comb == '江苏移动EPG5.0,'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('serviceComboCodes')).select_by_visible_text('--全部--')  # 选择全部
        time.sleep(1)
        homepage.bound_ser()   #   点击删除
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '数据成功删除。'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.button_1()   #  确认
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        try:
            assert name != wallpaper_name
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




