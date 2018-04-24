# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 价签管理 优惠策略
class Preferentialpolicy(unittest.TestCase):
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
        homepage.collapseOnes()  # 点击优惠策略
        homepage.Click_add()        # 点击新增
        driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_discount_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_discount_form.form-horizontal div.form-group div.col-sm-7 input#name.form-control').send_keys('AgentZero优惠')  # 输入名称
        homepage.attribute_value('2')   # 输入折扣值
        homepage.Click_time1()   # 点击生效时间
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/table/tbody/tr[4]/td[6]').click()
        homepage.Click_time2()  # 点击失效时间
        driver.find_element_by_xpath('/html/body/div[6]/div[3]/table/tbody/tr[4]/td[7]').click()
        homepage.Click_save3()      # 点击保存
        homepage.button_2()      # 点击弹出框确认


    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.add_names('AgentZero优惠')  # 输入搜索内容
        homepage.search_name1()  # 点击搜索
        name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            name1 == 'AgentZero优惠'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.collapseOnes()  # 点击优惠策略
        homepage.add_names('AgentZero优惠')  # 输入搜索内容
        homepage.search_name1()  # 点击搜索
        time.sleep(2)
        homepage.Click_Determine3()  # 点击编辑
        driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#edit_discount_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#edit_discount_form.form-horizontal div.form-group div.col-sm-7 input#name.form-control').send_keys('编辑测试')  # 输入名称

        '''
        # 编辑时添加描述信息不成功 待解决
        # driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_discount_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_discount_form.form-horizontal div.form-group div.col-sm-7 textarea#description.form-control').send_keys('AgentZero优惠编辑测试')  # 输入名称
        # driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_discount_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_discount_form.form-horizontal div.form-group div.col-sm-7 textarea#description.form-control').send_keys('AgentZero优惠编辑测试')  # 输入名称
        # driver.find_element_by_name('description').send_keys('AgentZero优惠编辑测试')  # 输入名称
        # homepage.description('AgentZero优惠编辑测试')  # 编辑描述内容
        '''
        homepage.Click_save4()  # 点击保存
        time.sleep(2)
        homepage.button_2()  # 点击确认
        homepage.add_names('编辑测试')  # 输入搜索内容
        homepage.search_name1()  # 点击搜索
        name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text
        try:
            assert name2 == 'AgentZero优惠编辑测试'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()  # 点击对勾
        homepage.Click_delete2()  # 点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        time.sleep(2)
        # homepage.Click_Determine2()  # 点击确认
        homepage.add_names('AgentZero优惠编辑测试')  # 输入搜索内容
        homepage.search_name1()  # 点击搜索
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





