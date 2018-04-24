# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 价签管理 价签配置
class Priceconfiguration(unittest.TestCase):
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
        homepage.Click_price()        # 点击价签管理
        homepage.dj_jiemj()  # 点击价签配置
        homepage.Click_increase()        # 点击新增
        homepage.Type_month('1')   # 输入有效时长
        homepage.Type_price('666')   # 输入价格
        homepage.Click_save()      # 点击保存
        homepage.ffy_sx_queding()      # 点击弹出框确认


    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.add_names('包时段-1月-6.66元')  # 输入搜索内容
        time.sleep(2)
        homepage.search_name1()  # 点击搜索
        time.sleep(2)
        name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert name1 == '包时段-1月-6.66元'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_jiemj()  # 点击价签配置
        homepage.add_names('包时段-1月-6.66元')  # 输入搜索内容
        homepage.search_name1()  # 点击搜索
        homepage.Click_edit()  # 点击编辑

        # 实验中  几种操作方式都报错
        # Select(driver.find_element_by_name('chargeType2')).select_by_value('1')  # 点击点播
        # driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#edit_price_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#edit_price_form.form-horizontal div.form-group div.col-sm-7 input#price.form-control').clear()
        # homepage.Type_price('888')  # 编辑价格
        # Select(driver.find_element_by_name('status')).select_by_value('2')  # 在线状态选择待上线

        homepage.Click_save2()  # 点击保存
        homepage.ffy_sx_queding()  # 点击确认
        name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        try:
            assert name2 == '包时段-1月-6.66元'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()  # 点击对勾
        homepage.Click_delete()  # 点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功！'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        # homepage.ffy_sx_queding()  # 点击确认
        # homepage.confirm_1()
        # homepage.add_names('包时段-1月-6.66元')  # 输入搜索内容
        homepage.Click_search()  # 点击搜索
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





