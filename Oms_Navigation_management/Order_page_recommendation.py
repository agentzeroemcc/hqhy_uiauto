# -*- coding:utf-8 -*-
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
ass_name = '文雀 高清'

#订购页面推荐
class Order(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_New_add(self):
        """添加"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击导航管理
        driver.find_element_by_xpath('/html/body/div[3]/div/div[1]/div/div[2]/div[2]/div/ul/li[2]/a').click()#点击关联推荐
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/h2/div/button/span[2]/span').click()   #  点击下拉
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/h2/div/div/ul/li[2]/a/span[1]').click()  # 点击订购页面推荐
        time.sleep(1)
        homepage.ToolOpenspan()  # 点击下拉
        homepage.Openinputcom('KS业务组合')  # 输入名称
        homepage.Openinputcom(Keys.ENTER)  # 回车
        homepage.manualToolbar()  #   点击添加
        homepage.productAllSelector()  # 点击选择产品（包）
        homepage.allKeyword(ass_name)  # 输入产品包名称
        homepage.allKeyword(Keys.ENTER)  # 回车
        homepage.selectorTabl()  # 点击复选
        homepage.btnAllSelected()  # 点击确认
        # homepage.product_play_info()  # 点击关闭
        homepage.opt_btn()  # 点击保存
        homepage.button_2()  # 点击确认
        test_name = driver.find_element_by_xpath('//*[@id="customId_2"]/td[3]').text     #  获取第3行name
        num_name = driver.find_element_by_xpath('//*[@id="customId_2"]/td[2]').text     #  获取第3行序号
        try:
            assert test_name == ass_name and num_name == '3'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.Order_recommend(self)  #  新添加关联推荐接口


    def test_top(self):
        """置顶"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.execute_script("window.scrollBy(0,3000)")
        # time.sleep(1)
        # driver.execute_script("window.scrollBy(0,5000)")
        # time.sleep(1)
        driver.find_element_by_xpath('//*[@id="customId_2"]/td[1]/input').click()  #  点击3行复选
        time.sleep(1)
        # js = "var q=document.body.scrollTop=0"
        # driver.execute_script(js)
        # time.sleep(2)
        driver.find_element_by_xpath('//*[@id="manualToolbar"]/button[4]').click()  #  点击置顶按钮
        time.sleep(1)
        test_name = driver.find_element_by_xpath('//*[@id="customId_0"]/td[3]').text  #  获取序号1的名称
        try:
            assert test_name == ass_name
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.Order_top(self)   #   置顶接口测试

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="customId_0"]/td[1]/input').click()  #  点击1复选
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="manualToolbar"]/button[2]').click()  # 点击编辑
        time.sleep(1)
        js = "document.getElementsByClassName('modal fadein in')[0].scrollTop=0"
        driver.execute_script(js)
        time.sleep(2)
        homepage.add_names('（编辑）')  #  添加名称
        homepage.opt_btn()   #  点击保存
        homepage.button_2()   #  点击确认
        edit_name = driver.find_element_by_xpath('//*[@id="customId_0"]/td[3]').text  # 获取序号1的名称
        try:
            assert edit_name == ass_name + '（编辑）'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.Order_edit(self)   #   编辑接口测试

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        homepage.customId_0()   #   点击复选
        homepage.manualToolbar3()   #   点击删除
        try:
            assert VodSearch.get_ass_text(self) == '删除成功！'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()   #  点击确认
        Interface.Order_delete(self)    #    删除接口测试

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()


