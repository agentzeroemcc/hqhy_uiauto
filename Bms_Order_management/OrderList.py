# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 订单管理  订单列表
class Orderlist(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Orderlist(self):
        """
        进入订单列表
        """
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[2]/a').click()  # 选择bms
        time.sleep(2)
        homepage.busines_com()  # 点击订单管理
        time.sleep(1)
        homepage.collapseOnes()  # 点击订单列表
        time.sleep(1)


        """ 新增 """

        homepage.Click_add5()  # 点击新增
        time.sleep(1)
        Select(driver.find_element_by_id('agentVendorCode_New')).select_by_value('1100101022055956197370017')  # 选择渠道名称：江苏移动
        time.sleep(3)
        Select(driver.find_element_by_id('serviceComboCode_New')).select_by_value('1100121022149038548320021')  # 选择业务组合：江苏移动
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="externalUserId_New"]').send_keys('123456789')  # 输入三方用户标识
        time.sleep(2)
        Select(driver.find_element_by_id('policyCode_New')).select_by_value('1200190023893812396740001')  # 选择渠道策略   江苏移动4K专区29.9
        time.sleep(3)
        homepage.Click_search4()  # 点击选择产品（包）
        time.sleep(1)
        homepage.Click_search5()  # 点击选择产品（包）复选框
        time.sleep(1)
        homepage.Click_confirm2()  # 点击确认选择
        time.sleep(1)
        homepage.Click_generate()  # 点击生成工单
        time.sleep(1)

        name1 = driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/div').text
        try:
            assert name1 == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.Click_confirm3()  # 点击确认
        time.sleep(1)

        '''搜索'''

        driver.find_element_by_xpath('//*[@id="searchBtn"]').click()  # 点击搜索按钮
        time.sleep(2)
        homepage.Type_tripartite('123456789')  # 輸入三访用户
        time.sleep(2)
        Select(driver.find_element_by_id('agentVendorCode')).select_by_value(
            '1100101022055956197370017')  # 选择渠道名称：江苏移动
        time.sleep(2)
        Select(driver.find_element_by_id('status')).select_by_value(
            '1')  # 选择订单类型：订购
        time.sleep(2)
        Select(driver.find_element_by_id('createType')).select_by_value(
            '0')  # 选择创建类型：线上
        time.sleep(2)
        Select(driver.find_element_by_id('vendorPolicyCode')).select_by_value(
            '1200190106010757925250001')  # 选择渠道策略：环球影视（包月）
        time.sleep(2)
        Select(driver.find_element_by_id('createMode')).select_by_value(
            '1')  # 选择创建方式：人工
        time.sleep(2)
        Select(driver.find_element_by_id('payType')).select_by_value(
            '0')  # 选择支付方式：话费扣费
        time.sleep(2)
        Select(driver.find_element_by_id('orderType')).select_by_value(
            '0')  # 选择订单状态：生效
        time.sleep(2)
        Select(driver.find_element_by_id('orderType')).select_by_value(
            '0')  # 选择订单状态：生效
        time.sleep(2)

        # 备注：不加延迟时，系统报错
        driver.find_element_by_xpath('//*[@id="createTimeStart"]').click()  # 点击创建时间
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/table/tfoot/tr/th').click()  # 点击（今天）
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="effectTimeStart"]').click()  # 点击生效时间
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[7]/div[3]/table/tfoot/tr/th').click()  # 点击（今天）
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="updateTimeEnd"]').click()  # 点击更新时间
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[12]/div[3]/table/tbody/tr[4]/td[6]').click()  # 点击时间点
        # time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchByName"]').click()  # 点击搜索按钮
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchByName"]').click()  # 点击搜索按钮
        time.sleep(2)

        name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[17]').text
        try:
            assert name2 == '人工'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''
        编辑
        '''
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]/a/i').click()  # 点击编辑
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="description"]').send_keys('AZ测试')  # 输入编辑内容
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="updateOrder"]').click()  # 点击修改订单
        time.sleep(2)
        name3 = driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/div').text
        try:
            assert name3 == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.Click_confirm3()  # 点击确认

        name4 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[23]').text
        try:
            assert name4 == 'AZ测试'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''重置'''

        driver.find_element_by_xpath('//*[@id="searchReset"]').click()  # 点击重置
        time.sleep(2)

        name5 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[17]').text
        try:
            assert name5 == '0	'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        """导出"""

        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/input').click()  # 点击第一条记录复选框
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="exportOrder_btn"]').click()  # 点击导出
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="fileName"]').send_keys('AZ测试')  # 输入名称
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="exportOrder"]').click()  # 点击导出
        time.sleep(2)

        name7 = driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/div').text
        try:
            assert name7 == '操作成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        homepage.Click_confirm3()  # 点击确定

        driver.find_element_by_xpath('//*[@id="collapseOne"]/div/ul/li[5]/a').click()  # 点击导出列表
        time.sleep(2)

        name7 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        try:
            assert name7 == 'AZ测试'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/input').click()  # 点击第一个复选框
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="delete_btn"]').click()  # 点击删除
        time.sleep(2)
        alert = driver.switch_to_alert()  # 定位弹出对话框
        time.sleep(2)
        alert.accept()  # 点击对话框“确定”
        time.sleep(3)


        '''删除'''

        homepage.collapseOnes()  # 点击订单列表
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[1]/input').click()  # 点击第一条记录复选框
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="deleteOrder_btn"]').click()  # 点击删除
        time.sleep(2)
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”

        name6 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[23]').text
        try:
            assert name6 == ''
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_business_order(self):
        """营业厅订购"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[2]/a').click()  # 选择bms
        time.sleep(2)
        homepage.busines_com()  # 点击订单管理
        homepage.collapseOnes()  # 点击订单列表
        homepage.searchBtn()  #  点击搜索
        homepage.Type_tripartite('13167568664')  #  输入三方用户
        homepage.searchByName()  #  搜索
        threeid = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text





    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
