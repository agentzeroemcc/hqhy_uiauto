# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger
from framework.Interface_test import Interface

logger = Logger(logger="BrowserEngine").getlog()
wallpaper = 'Wallpaper testing'
#运营壁纸管理
class Operating(unittest.TestCase,Interface):
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
        i = -1
        while i<=1:
            i += 1
            homepage.add_recomm()  #  点击新增
            homepage.add_names(wallpaper+str(i))  #  输入壁纸名称
            homepage.frmRecommendDoc_button()  #  点击业务组合
            homepage.frmRecommendDoc_span()  #  选择业务组合     AgentZero业务组合
            homepage.frmRecommendDoc_button()  # 点击业务组合
            Select(driver.find_element_by_name('orderStatus')).select_by_value(str(i))   #   下拉选择
            driver.find_element_by_id('pictureFile').send_keys('D:\\'+str(i)+'.jpg')
            time.sleep(2)
            homepage.btnCreates()  #  添加

    def public(self):
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.clear_specialName()   #  清空
        homepage.specialName(wallpaper)  # 输入壁纸名称
        homepage.custom_toolbar1()  # 点击搜索
        self.test_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取名称
        self.belong = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[6]').text  # 获取所属页面（全部页面）

    def test_search(self):
        """搜索"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.servicegrouping()  # 点击壁纸管理
        Select(driver.find_element_by_id('orderStatus')).select_by_value('0')  # 下拉选择全部页面
        self.public()
        try:
            assert self.test_name == wallpaper+'0' and self.belong == '全部页面'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.Page_recommend(self)   #  选择页面类型--全部页面接口
        Select(driver.find_element_by_id('orderStatus')).select_by_value('1')  # 下拉选择全部页面
        self.public()
        try:
            assert self.test_name == wallpaper + '1' and self.belong == '订购页面'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(3)
        Interface.Page_recommend1(self)   #  选择页面类型--订购页面接口
        Select(driver.find_element_by_id('orderStatus')).select_by_value('2')  # 下拉选择全部页面
        self.public()
        try:
            assert self.test_name == wallpaper + '2' and self.belong == '开机logo'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        Interface.Page_recommend2(self)   #  选择页面类型--开机log接口

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.terminal_edit()  #  点击编辑
        homepage.add_names('（编辑）')  #  添加编辑
        driver.find_element_by_xpath('//*[@id="disOpenTime"]/div/span/i').click()  #  点击选择开始时间
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/table/tfoot/tr/th').click()  #  点击今天
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="disCloseTime"]/div/span/i').click()  # 点击选择结束时间
        time.sleep(1)
        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/table/tfoot/tr/th').click()  # 点击今天
        time.sleep(1)
        Select(driver.find_element_by_id('status')).select_by_value('1')  # 下拉状态启用
        homepage.btnSaves()  #  点击更新
        edit_test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        get = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text
        uptime = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text
        downtime = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[9]').text
        try:
            assert edit_test == wallpaper + '2（编辑）' and get == '全部页面' and uptime != '' and downtime != '' and state == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()


    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        del_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        homepage.bound_ser()  #  点击删除
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '数据成功删除。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()  #  确认
        homepage.specialName(del_name)  #  输入名称
        homepage.custom_toolbar1()  #  点击搜索
        matching = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert matching == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.clear_specialName()  # 清空
        homepage.custom_toolbar1()  # 点击搜索
        homepage.table_input()
        homepage.table_input1()
        homepage.remove()  #  点击删除按钮
        driver.switch_to_alert().accept()
        homepage.button_2()  # 确认

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()






