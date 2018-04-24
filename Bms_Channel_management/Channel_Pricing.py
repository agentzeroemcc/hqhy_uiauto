# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 渠道管理  渠道定价
class Channelpricing(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_channel(self):
        """
        进入渠道定价模块
        """
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[2]/a').click()  # 选择bms
        time.sleep(2)
        homepage.search_Content()  # 点击渠道管理
        time.sleep(1)
        homepage.collapseOnes()   # 点击渠道定价
        time.sleep(1)
        Select(driver.find_element_by_id('agentVendorCode')).select_by_value('1100101022055956197370017')   # 选择渠道：江苏移动
        time.sleep(1)
        Select(driver.find_element_by_id('serviceComboCode')).select_by_value('1100121106016768608590023')   # 选择业务组合：AgentZero业务组合
        time.sleep(1)

        '''产品包批量定价'''

        homepage.Click_box1()   # 点击AgentZero栏目树复选框
        homepage.Click_prod()   # 点击产品包批量定价
        Select(driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#bind_vendorPolicy_package_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#bind_vendorPolicy_package_form.form-horizontal div.form-group div.col-sm-7.form-group select#level.form-control')).select_by_value('4')  # 选择优先级为高
        homepage.Click_whole()  # 点击渠道恶略-包时段复选框
        homepage.Click_confirm()   # 点击确认
        homepage.ffy_sx_queding()   # 点击弹出确认
        name1 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td[7]').text
        try:
            name1 == '高'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''产品定价'''

        homepage.bindProduct()  # 点击产品定价
        time.sleep(1)
        homepage.chooseProduct()  # 点击选择产品
        time.sleep(1)
        homepage.Click_prod1()  # 点击选择第一个产品复选框
        time.sleep(1)
        homepage.prd_add()  # 点击产品-右箭头
        time.sleep(1)
        homepage.Click_Determine4()  # 点击确认
        time.sleep(1)
        homepage.Click_dan()  # 点击单选
        time.sleep(1)
        homepage.Click_Determine5()  # 点击确认
        time.sleep(1)

        name2 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        try:
            name2 == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.ffy_sx_queding()  # 点击弹出框确认
        time.sleep(1)

        name3 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr[1]/td[4]').text
        try:
            name3 == '尊严殖民地'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        # '''附加属性'''
        #
        # # 商品附加属性不能删除？？？
        # homepage.Click_attribute()  # 点击附加属性
        # homepage.Click_Plus()  # 点击+号
        # Select(driver.find_element_by_class('form-control')).select_by_value('free_program_number')   # 选择free_program_number
        # homepage.Type_no('9')  # 输入免费期数
        # homepage.Click_nike()  # 点击对勾
        # homepage.Click_fork()  # 点击叉号

        # 未做断言

        '''渠道定价'''

        homepage.Click_channel()  # 点击渠道定价综艺
        time.sleep(1)
        Select(driver.find_element_by_css_selector(
            'html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#bind_vendorPolicy_package_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#bind_vendorPolicy_package_form.form-horizontal div.form-group div.col-sm-7.form-group select#level.form-control')).select_by_value(
            '4')  # 选择优先级为高
        time.sleep(2)
        homepage.Click_whole()  # 点击渠道恶略-包时段复选框
        time.sleep(1)
        homepage.Click_confirm()  # 点击确认
        time.sleep(1)

        name4 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        try:
            name4 == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.ffy_sx_queding()  # 点击弹出框确认
        time.sleep(1)

        name5 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr[1]/td[4]').text
        try:
            name5 == 'AgentZero综艺'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        """选择电视剧下面的子栏目"""

        homepage.Click_add3()  # 点击电视剧加号图标
        time.sleep(1)
        homepage.Click_add4()  # 点击电视剧子栏目加号图标
        time.sleep(1)
        homepage.Click_channel2()  # 点击电视剧子栏目渠道定价
        time.sleep(1)
        Select(driver.find_element_by_css_selector(
            'html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#bind_vendorPolicy_package_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#bind_vendorPolicy_package_form.form-horizontal div.form-group div.col-sm-7.form-group select#level.form-control')).select_by_value(
            '2')  # 选择优先级为中
        time.sleep(1)
        homepage.Click_whole()  # 点击渠道恶略-包时段复选框
        time.sleep(1)
        homepage.Click_confirm()  # 点击确认
        time.sleep(1)
        homepage.ffy_sx_queding()  # 点击弹出确认
        time.sleep(1)
        name6 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr[3]/td[7]').text
        try:
            name6 == '中'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''搜索'''

        # 商品类型 价签等级 渠道定价策略 未做测试

        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        homepage.Type_prod('尊严殖民地')  # 输入商品名称
        time.sleep(3)
        driver.find_element_by_id('agentVendorSearchByName').click()
        time.sleep(1)
        name7 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td[4]').text
        try:
            name7 == '尊严殖民地'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''编辑'''

        homepage.Click_edit3()  # 点击编辑
        # driver.find_element_by_id('level').send_keys('4') # 选择优先级为较高
        homepage.Click_vod()  # 点击单片点播10元
        homepage.Click_Determine5()  # 点击确定

        name8 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        try:
            name8 == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.ffy_sx_queding()  # 点击弹出框确定

        name9 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td[9]').text
        try:
            name9 == '单片点播10元--点播-4小时-1000.00元'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''同步'''

        time.sleep(2)
        homepage.Click_synchronization()  # 点击同步
        time.sleep(2)
        name10 = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        try:
            name10 == '更新AgentZero综艺成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.ffy_sx_queding()  # 点击弹出框确定
        time.sleep(2)

        """删除"""

        homepage.Click_delete4()  # 点击删除图标
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”

        name11 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td').text
        try:
            name11 == '没有找到匹配的记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_delete(self):

        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="agentVendorAssetNameInput"]').clear()  # 清除商品名称
        time.sleep(2)
        driver.find_element_by_id('agentVendorSearchByName').click()  # 点击搜索
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/thead/tr/th[1]/div[1]/input').click()  # 点击全选的复选框
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="deleteBind"]').click()  # 点击批量删除
        time.sleep(2)
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”

        name12 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td').text
        try:
            name12 == '没有找到匹配的记录'
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
