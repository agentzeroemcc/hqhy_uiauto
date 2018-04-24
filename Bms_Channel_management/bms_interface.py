# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface


"""bms_interface测试"""

class bmsInterface(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_bms(self):

        """bms_interface:get接口"""

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
        Select(driver.find_element_by_id('serviceComboCode')).select_by_value('1100121022149038548320021')  # 选择业务组合：江苏移动
        time.sleep(3)

        """接口：获取产品包价签"""

        homepage.Click_add3()   # 点击AgentZero综艺加号
        homepage.Click_add4()   # 点击AgentZero综艺加号
        homepage.Click_box3()   # 点击Az20180312az复选框
        homepage.Click_prod()   # 点击产品包批量定价
        Select(driver.find_element_by_css_selector('html body.modal-open div#main.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#bind_vendorPolicy_package_dialog.modal.fade.in div.modal-dialog.modal-lg div.modal-content div.modal-body form#bind_vendorPolicy_package_form.form-horizontal div.form-group div.col-sm-7.form-group select#level.form-control'
                                                   )).select_by_value('4')  # 选择优先级为高
        homepage.Click_box4()  # 点击渠道恶略-包时段复选框
        homepage.Click_confirm()   # 点击确认
        homepage.ffy_sx_queding()   # 点击弹出确认

        time.sleep(5)
        Interface.bms_api_getPackagePrice(self)   # 添加价签后调用接口
        time.sleep(2)

        """接口：获取产品价签"""

        homepage.bindProduct()  # 点击产品定价
        time.sleep(1)
        homepage.chooseProduct()  # 点击选择产品
        time.sleep(1)
        homepage.cp_mingchen('超体AZ')  # 输入产品名称：超体AZ
        time.sleep(1)
        homepage.Click_search6()  # 点击搜索
        time.sleep(1)
        homepage.dj_duig()  # 选择超体
        time.sleep(1)
        homepage.prd_add()  # 选择向右箭头
        time.sleep(1)
        homepage.Click_Determine4()  # 点击确认
        time.sleep(1)
        homepage.Click_vod()  # 点击价签：单片点播10元
        time.sleep(1)
        homepage.Click_Determine5()  # 点击确定
        time.sleep(1)
        homepage.ffy_sx_queding()  # 点击确定
        time.sleep(1)

        Interface.bms_api_getProductPrice(self)  # 调用接口
        time.sleep(3)

        """接口：获取业务分组下的所有包时段价签"""

        Interface.bms_api_getPackagesPrices(self)  # 调用接口
        time.sleep(3)

        """接口：查询特定用户已订购产品"""

        homepage.busines_com()  # 点击订单管理
        time.sleep(1)
        homepage.collapseOnes()  # 点击订单列表
        time.sleep(1)

        """ 新增 """

        homepage.Click_add5()  # 点击新增
        time.sleep(1)
        Select(driver.find_element_by_id('agentVendorCode_New')).select_by_value(
            '1100101022055956197370017')  # 选择渠道名称：江苏移动
        time.sleep(3)
        Select(driver.find_element_by_id('serviceComboCode_New')).select_by_value(
            '1100121022149038548320021')  # 选择业务组合：江苏移动
        time.sleep(3)
        driver.find_element_by_xpath('//*[@id="externalUserId_New"]').send_keys('18583250213')  # 输入三方用户标识
        time.sleep(2)
        Select(driver.find_element_by_id('policyCode_New')).select_by_value('1200190106014295928660015')  # 选择渠道策略：agentzero渠道定价
        time.sleep(3)
        homepage.Click_search4()  # 点击选择产品（包）
        time.sleep(1)
        homepage.Click_search5()  # 点击选择产品（包）复选框
        time.sleep(1)
        homepage.Click_confirm2()  # 点击确认选择
        time.sleep(1)
        homepage.Click_generate()  # 点击生成工单
        time.sleep(1)

        homepage.Click_confirm3()  # 点击确认
        time.sleep(1)

        '''搜索'''

        driver.find_element_by_xpath('//*[@id="searchBtn"]').click()  # 点击搜索按钮
        time.sleep(2)
        homepage.Type_tripartite('18583250213')  # 輸入三方用户
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchByName"]').click()  # 点击搜索按钮
        time.sleep(2)

        """接口：查询特定用户已订购产品"""

        Interface.bms_api_getOrderList(self)
        time.sleep(2)

        '''删除'''

        homepage.table_Input()  # 点击搜索记录的复选框
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="deleteOrder_btn"]').click()  # 点击删除
        time.sleep(2)
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        time.sleep(3)

        '''渠道定价删除'''

        homepage.search_Content()  # 点击渠道管理
        time.sleep(1)
        homepage.collapseOnes()  # 点击渠道定价
        time.sleep(1)
        Select(driver.find_element_by_id('agentVendorCode')).select_by_value('1100101022055956197370017')  # 选择渠道：江苏移动
        time.sleep(1)
        Select(driver.find_element_by_id('serviceComboCode')).select_by_value(
            '1100121022149038548320021')  # 选择业务组合：江苏移动
        time.sleep(3)
        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        homepage.Click_box6()  # 点击删除复选框
        time.sleep(3)
        homepage.Click_delete5()  # 点击批量删除
        time.sleep(3)
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        time.sleep(3)


    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
