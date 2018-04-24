# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

#终端绑定
class Terninal(unittest.TestCase):
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
        homepage.busines_com()  #  点击业务组合
        homepage.collapseTwo()  #  点击终端绑定
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value('1100121023874101446610014')  # 选择业务组合  福建联通
        time.sleep(2)
        homepage.add_recomm()  #  d点击新增
        test_name = '终端绑定测试'
        driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_devicerule_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_devicerule_form.form-horizontal div.form-group div.col-sm-7 input#name.form-control').send_keys(test_name)
        # homepage.add_names(test_name)  #  输入测试名称
        homepage.mac_type2()  #  选择添加方式   mac段添加
        homepage.startMac('00:12:22:33:44:55')  #  起始mac段
        homepage.endMac('00:12:22:33:44:56')  #  结束mac段
        Select(driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#create_devicerule_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#create_devicerule_form.form-horizontal div.form-group div.col-sm-7 select.form-control')).select_by_value('2')  # 选择状态  停用
        time.sleep(1)
        Select(driver.find_element_by_name('deviceVendorCode')).select_by_value('1100106022057338241700004')  # 选择终端厂商  优酷-创维
        time.sleep(1)
        Select(driver.find_element_by_name('deviceTypeCode')).select_by_value('1100039160113150000031906')  # 选择终端型号  TNL-5200
        time.sleep(1)
        Select(driver.find_element_by_name('deviceChipVendorCode')).select_by_value('1100036160113150000031907')  # 选择芯片厂商  海思3716c
        time.sleep(1)
        Select(driver.find_element_by_name('partnerType')).select_by_value('1')  # 选择归属方  youku
        time.sleep(1)
        homepage.create_devicerule_form()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '添加成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        """搜索"""
        homepage.searchBtn()  #  点击搜索
        homepage.add_names(test_name)  #  输入名称
        homepage.searchByName()  #  开始搜索
        seach_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        try:
            assert seach_name == test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Enable_disable(self):
        """启用/停用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()  #  点击复选框
        homepage.startbutton()  #  点击启用
        alert = driver.switch_to_alert()
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '启用操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[11]').text
        try:
            assert state == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """停用"""
        homepage.table_Input()  # 点击复选框
        homepage.stopbutton()  #  点击停用
        alert = driver.switch_to_alert()
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '停用操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        state1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[11]').text
        try:
            assert state1 == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.terminal_edit()  #  点击编辑
        driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#edit_devicerule_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#edit_devicerule_form.form-horizontal div.form-group div.col-sm-7 input#edit_name.form-control').send_keys('（编辑）')   #  名称添加
        homepage.edit_devicerule_form()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '修改成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        edit_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text  #  获取编辑名称
        try:
            assert edit_name == '终端绑定测试（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Handoff_service(self):
        """切换业务组合"""
        homepage = HomePage(self.driver)
        driver = self.driver
        edit_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text  # 获取名称
        homepage.handoff_ser()  #  点击切换业务组合
        driver.switch_to_alert().accept()  #  锁定弹出框点击确定
        Select(driver.find_element_by_xpath('//*[@id="change_servicecombo_form"]/div[1]/div/select')).select_by_value(
            '1100121106014108498720071')  # 选择业务组合  KS业务组合测试（勿动！）
        time.sleep(1)
        homepage.change_servicecombo_form()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '切换业务组合成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value('1100121106014108498720071')  #  选择业务组合  KS业务组合测试（勿动！）
        time.sleep(1)
        handoff_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text  #  获取切换后的名称
        try:
            assert handoff_name == edit_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Unbound(self):
        """解除绑定"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.unbound_edit()  #  点击解除绑定
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '解除绑定操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        pipei = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert pipei == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()  #  点击重置
        name = driver.find_element_by_xpath('//*[@id="name"]').text
        try:
            assert name == ''
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



