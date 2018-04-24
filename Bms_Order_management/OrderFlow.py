# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 订单管理  订购流水
class OrderFlow(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_orderflow(self):
        """
        进入订购流水
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
        driver.find_element_by_xpath('//*[@id="collapseOne"]/div/ul/li[4]/a').click()  # 点击订购流水
        time.sleep(3)

        """导出"""

        driver.find_element_by_xpath('//*[@id="exportFlow_btn"]').click()  # 点击导出
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="fileName"]').send_keys('AZ测试')  # 输入名称
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="exportFlow"]').click()  # 点击导出
        time.sleep(2)
        driver.find_element_by_css_selector('.btn-success').click()  # 点击确定
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="collapseOne"]/div/ul/li[5]/a').click()  # 点击导出列表
        time.sleep(2)

        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        try:
            assert name == 'AZ测试'
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

        '''搜索'''

        driver.find_element_by_xpath('//*[@id="collapseOne"]/div/ul/li[4]/a').click()  # 点击订购流水
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="searchBtn"]').click()  # 点击搜索按钮
        time.sleep(2)
        Select(driver.find_element_by_id('agentVendorCode')).select_by_value(
            '1100101022055956197370017')  # 选择渠道名称：江苏移动
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="externalUserId"]').send_keys('71975089827409')  # 输入三方用户
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="assetName"]').send_keys('电视剧-追播美剧-付费-江苏移动')  # 输入商品名称
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="code"]').send_keys('1200182106010671673550058')  # 输入流水标识
        time.sleep(2)
        Select(driver.find_element_by_id('chargeType')).select_by_value(
            '0')  # 选择付费类型：包月
        time.sleep(2)
        Select(driver.find_element_by_id('status')).select_by_value(
            '1')  # 选择订单类型：订购
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchByName"]').click()  # 点击订购流水
        time.sleep(3)


        name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert name2 == '电视剧-追播美剧-付费-江苏移动		'
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
