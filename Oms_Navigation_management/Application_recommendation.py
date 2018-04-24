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
app_name = '文雀 高清'

#打开应用推荐
class Appication(unittest.TestCase,Interface):
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
        driver.find_element_by_css_selector('div.panel:nth-child(2) > div:nth-child(2) > div:nth-child(1) > ul:nth-child(1) > li:nth-child(1) > a:nth-child(1)').click()  #点击应用推荐
        time.sleep(1)
        # homepage.dj_jiemj()  # 点击打开应用推荐
        homepage.ToolbarmanualOpen()  #点击下拉
        homepage.manualOpenToolbarinput('KS业务组合')  #输入名称
        homepage.manualOpenToolbarinput(Keys.ENTER)  #输入名称
        time.sleep(1)
        homepage.manualOpenToolbar()  # 点击添加
        homepage.productAllSelector()  # 点击选择产品（包）
        homepage.allKeyword(app_name)  # 输入产品包名称
        homepage.allKeyword(Keys.ENTER)  # 回车
        homepage.selectorTabl()  # 点击复选
        homepage.btnAllSelected()  # 点击确认
        # homepage.product_play_info()  # 点击关闭
        # driver.find_element_by_xpath('//*[@id="combo_div"]/div/div/button/span[2]/span').click()   #  点击绑定业务组合
        # homepage.combo_div_input('福建联通')
        # homepage.combo_div_input(Keys.ENTER)     #输入名称并回车
        homepage.opt_btn()  #   点击保存
        try:
            assert VodSearch.get_ass_text(self) == '保存成功'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()  # 点击确认

    def test_search_app(self):
        """搜索应用推荐"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.input_search_test(app_name)   #  输入搜索名称
        test_name = driver.find_element_by_xpath('//*[@id="customId_0"]/td[3]').text
        try:
            assert test_name == app_name
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()


    def test_app_edit(self):
        """应用推荐编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.customId_0()    #  点击复选
        homepage.manualOpenToolbar_butt()   #  点击编辑
        homepage.add_names('（编辑）')   #    输入编辑
        homepage.opt_btn()   #  点击保存
        homepage.button_2()  # 点击确认
        test_name = driver.find_element_by_xpath('//*[@id="customId_0"]/td[3]').text
        try:
            assert test_name == app_name + '（编辑）'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.clear_input_search()  # 清空搜索
        homepage.input_search_test(Keys.ENTER)
        Interface.edit_app(self)    #    应用推荐编辑接口

    def test_top(self):
        """置顶"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.clear_input_search()   #  清空搜索
        # driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[3]/div[1]/div[2]/button/i').click()  #  点击刷新
        # time.sleep(2)
        # name = driver.find_element_by_xpath('//*[@id="customId_2"]/td[3]').text
        homepage.customId_2()  #  点击复选
        homepage.manualOpenToolbar4()  #  点击置顶
        test_name = driver.find_element_by_xpath('//*[@id="customId_0"]/td[3]').text
        try:
            assert test_name == app_name
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.add_app(self)  # 应用推荐添加接口测试

    def test_bottom(self):
        """置底"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.clear_input_search()  #  清空搜索
        homepage.customId_0()  #  点击复选
        homepage.manualOpenToolbar5()  #  点击置底
        test_name = driver.find_element_by_xpath('//*[@id="customId_2"]/td[3]').text
        try:
            assert test_name == app_name + '（编辑）'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()


    def test_del_app(self):
        """删除应用推荐"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.input_search_test(app_name)  # 输入搜索名称
        homepage.customId_0()  # 点击复选
        homepage.manualOpenToolbar_butt3()  # 点击删除
        try:
            assert VodSearch.get_ass_text(self) == '删除成功！'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()  # 点击确认
        record = driver.find_element_by_xpath('//*[@id="open_recommendbox_table"]/tbody/tr/td').text
        try:
            assert record == '没有找到匹配的记录'
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.del_app(self)   #  删除接口测试

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()







