# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
#推荐池管理
class Recommend(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Recomm_pool(self):
        """新增"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.recommend()    #点击推荐池管理
        homepage.add_recomm()       #点击新增
        # r_name = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr[1]/td[2]').text
        r_name = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr[6]/td[2]').text   #获取名称
        homepage.NsearchName(r_name)   #  输入名称
        homepage.btnSearch()   #  点击搜索
        homepage.productTable()     #d点击复选
        homepage.btnAppend()        #点击添加
        try:
            assert VodSearch.get_ass_text(self) == '添加成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #点击确认
        add_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        try:
            assert add_name == r_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Recomm_search(self):
        """搜索"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.recommend()  # 点击推荐池管理
        """类型搜索"""
        for asset in range(1,4):
            Select(driver.find_element_by_id('assetType')).select_by_value(str(asset))  #  选择 产品
            homepage.btnPoolSearch()   #  点击搜索
            for prod in range(1,11):
                prodtype = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(prod)+']/td[5]').text  #  获取产品类型
                try:
                    assert prodtype == '产品' or prodtype == '产品包' or prodtype == '栏目'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
        driver.refresh()
        """内容类型"""
        contentlist = ['电影', '综艺', '动漫','电视剧']
        for content in contentlist:
            Select(driver.find_element_by_id('contentType')).select_by_visible_text(content)  #  选择 产品
            homepage.btnPoolSearch()   #  点击搜索
            for prod in range(1,11):
                prodtype = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr['+str(prod)+']/td[6]').text  #  获取产品类型
                try:
                    assert prodtype == '电影' or prodtype == '综艺' or prodtype == '动漫' or prodtype == '电视剧'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
        driver.refresh()
        """CP搜索"""
        cplist = ['YOUKU', 'WLXZ']
        for cp in cplist:
            Select(driver.find_element_by_id('cp')).select_by_value(cp)  # 选择 产品
            homepage.btnPoolSearch()  # 点击搜索
            for prod in range(1, 11):
                prodtype = driver.find_element_by_xpath(
                    '//*[@id="table"]/tbody/tr[' + str(prod) + ']/td[7]').text  # 获取产品类型
                try:
                    assert prodtype == '优酷（合作伙伴）' or prodtype == '网络下载'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
        driver.refresh()
        """内容搜索"""
        content = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        homepage.poolSearchName(content)       #输入搜索内容
        homepage.poolSearchName(Keys.ENTER)       #回车确认
        search_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            assert search_name == content
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Editorial_recomm(self):
        """编辑推荐内容"""
        homepage = HomePage(self.driver)
        driver = self.driver
        search_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        homepage.table_Bj()     #点击编辑按钮
        homepage.add_names('（编辑）')#添加内容
        homepage.frmRecommendItemDoc()      #点击更新
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert new_name == search_name + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Delete_recomm(self):
        """删除推荐"""
        homepage = HomePage(self.driver)
        driver = self.driver
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.edit_product()     #点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        homepage.poolSearchName(name)   #输入搜索名称
        homepage.poolSearchName(Keys.ENTER)   #回车
        record = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert record == '没有找到匹配的记录'
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


