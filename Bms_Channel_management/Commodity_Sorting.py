# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch

# 渠道管理  渠道定价
class CommoditySorting(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_commodity(self):
        """
        进入商品定价排序
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
        driver.find_element_by_xpath('//*[@id="collapseOne"]/div/ul/li[3]/a').click()  # 点击商品定价排序
        time.sleep(1)
        Select(driver.find_element_by_id('agentVendorCode')).select_by_value('1100101022055956197370017')   # 选择渠道：江苏移动
        time.sleep(1)
        Select(driver.find_element_by_id('serviceComboCode')).select_by_value('1100121106016768608590023')   # 选择业务组合：AgentZero业务组合
        time.sleep(1)


        '''两个下拉框：价签类型 价签等级'''

        Select(driver.find_element_by_id('vendorPolicyCode')).select_by_value('1200190106010758793700003')  # 选择单片点播5元
        time.sleep(1)

        name2 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td').text
        try:
            name2 == '没有找到匹配的记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        Select(driver.find_element_by_id('vendorPolicyCode')).select_by_visible_text('--全部--')  # 选择全部
        time.sleep(3)

        name3 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td[3]').text
        try:
            name3 == 'AgentZero综艺	'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        Select(driver.find_element_by_id('assetPriceLevel')).select_by_value('0')  # 选择价签等级为低
        time.sleep(3)

        name4 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td').text
        try:
            name4 == '没有找到匹配的记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        Select(driver.find_element_by_id('assetPriceLevel')).select_by_visible_text('--请选择价签等级--')  # 选择价签等级为低
        time.sleep(1)

        name5 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td[3]').text
        try:
            name5 == 'AgentZero综艺	'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''搜索'''

        homepage.Type_prod2('AgentZero综艺')  # 輸入商品名稱
        homepage.searchByName()  # 点击搜索按钮
        name1 = driver.find_element_by_xpath('//*[@id="policyAssetsTable"]/tbody/tr/td[3]').text
        try:
            name1 == 'AgentZero综艺	'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

        '''上移 下移未做'''

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
