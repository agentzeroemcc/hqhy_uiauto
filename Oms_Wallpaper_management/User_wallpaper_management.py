# -*- coding:utf-8 -*-
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.Interface_test import Interface

#用户壁纸库管理
class User_wallpaper(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Upload_wallpaper(self):
        """上传壁纸"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()  #  点击壁纸管理
        homepage.collapseTwo2()  #  点击用户壁纸库管理
        driver.find_element_by_id('create_pictureurl1File').send_keys('D:\\spec.jpg')  #选择上传壁纸
        time.sleep(1)
        try:
            assert VodSearch.get_ass_text(self) == '请检查要上传的背景图!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div/div[3]/div[2]/a/span').click()  #  点击上传
        time.sleep(2)
        Interface.add_wallpaper(self)   #   新增用户壁纸接口测试

    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.ordinaryName('spec')  #  输入壁纸名称
        homepage.custom_toolbar1()  #  点击搜索
        wall_name = driver.find_element_by_xpath('//*[@id="attrImages"]/div/div/div/p').text
        # try:
        #     assert wall_name == 'spec.jpg'
        #     print('Test pass.')
        # except Exception as e:
        #     print("Test fail.", format(e))
        #     homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="attrImages"]/div/div/div/p/a/i').click()  #  点击删除
        time.sleep(2)
        driver.switch_to_alert().accept()

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()




