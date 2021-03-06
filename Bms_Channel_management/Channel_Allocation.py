# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 渠道管理  渠道策略配置
class Channelallocation(unittest.TestCase):
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
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[2]/a').click()  # 选择bms
        time.sleep(2)
        homepage.search_Content()        # 点击渠道管理
        homepage.dj_jiemj()   # 点击渠道策略配置
        homepage.Click_add2()        # 点击新增
        Select(driver.find_element_by_id('agentVendorCode')).select_by_value('1100101022055956197370017-江苏移动')   # 选择渠道商名称
        homepage.Type_party('AgentZero')   # 输入三方计费代码
        driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_vendorPolicy_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_vendorPolicy_form.form-horizontal div.form-group label.col-sm-7 input#policyName.form-control').send_keys('AgentZero')  # 输入渠道定价策略
        homepage.Type_content('AgentZero')   # 输入显示名称
        homepage.Type_discount('6')   # 输入折扣取值
        Select(driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_vendorPolicy_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_vendorPolicy_form.form-horizontal div#status_div.form-group label.col-sm-7 select#status.form-control')).select_by_value('1')  # 选择启用
        homepage.Tlick_save5()  # 点击保存
        homepage.ffy_sx_queding()  # 点击确认


    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchBtn()  # 点击搜索
        homepage.Type_channel1('AgentZero')  # 输入搜索内容
        homepage.searchByName()  # 点击搜索
        name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text
        try:
            name1 == 'AgentZero'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.Click_edit1()  # 点击编辑
        Select(driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#edit_vendorPolicy_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#edit_vendorPolicy_form.form-horizontal div#status_div.form-group label.col-sm-7 select#status.form-control')).select_by_value('2')  # 编辑改为停用
        homepage.Tlick_save6()  # 点击保存
        homepage.ffy_sx_queding()  # 点击确认
        name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[13]').text
        try:
            assert name2 == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()  # 点击对勾
        homepage.Click_delete3()  # 点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        homepage.searchByName()  # 点击搜索
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text    # 没有找到匹配的记录
        try:
            assert text == '没有找到匹配的记录'
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
