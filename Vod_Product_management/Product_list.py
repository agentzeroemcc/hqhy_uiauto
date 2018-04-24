# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch

ks_name = 'KS产品包测试（勿动）'
#产品列表
class List(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Search(self):
        """搜索"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_chanpguanl()  # 产品管理
        homepage.collapseOne()  #产品列表
        initial_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        one_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # 一级分类
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text       #CP名称
        homepage.searchBtn()    #搜索按钮
        homepage.add_names(initial_name)
        driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/button').click() #点击一级分类下拉
        driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/div/div/input').send_keys(one_name)#输入一级分类名称
        driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/div/div/input').send_keys(Keys.ENTER)#回车
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[5]/div/button').click()  # 点击CP下拉
        driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[5]/div/div/div/input').send_keys(cp_name)  # 输入cp名称
        driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[5]/div/div/div/input').send_keys(Keys.ENTER)
        time.sleep(2)
        homepage.searchByName()  # 点击搜索
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        type = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        type1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert test == initial_name and type == one_name and type1 == cp_name
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()
        test = driver.find_element_by_xpath('//*[@id="name"]').text
        select = driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/button/span[1]').text
        selects = driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[5]/div/button/span[1]').text
        try:
            assert test == '' and select == '全部' and selects == '全部'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Online_status(self):
        """在线状态"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.dj_chanpguanl()
        Select(driver.find_element_by_id('isLine')).select_by_value('0')# 在线状态下拉框并选择待上线
        time.sleep(2)
        On_line = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text
        try:
            assert On_line == '待上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_value('2')#选择下线
        time.sleep(2)
        Offline = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text
        try:
            assert Offline == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_value('1')#上线
        time.sleep(2)
        Go_online = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[6]').text
        try:
            assert Go_online == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(2)

    # def test_Es(self):
    #     """ES同步"""
    #     homepage = HomePage(self.driver)
    #     driver = self.driver
    #     homepage.send_submit_btn()      #ES同步按钮

    def test_Edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.edit_product() #点击编辑
        homepage.product_name('（编辑测试）')#添加
        homepage.edit_product_form()#点击保存
        try:
            assert VodSearch.get_ass_text(self) == '更新操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()    #确认按钮
        get_text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.add_names(get_text)
        homepage.searchByName()
        asst = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            assert asst == get_text
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.glyphicon_edit()       #点击编辑
        homepage.product_name_clear()  # 删除‘编辑测试’
        homepage.product_name(old_name)  # 添加
        homepage.edit_product_form()  # 点击保存
        homepage.confirm_1()  # 点击确认
        homepage.searchReset()  # 重置

    def test_Add_package(self):
        """加入产品包"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.add_names('办公室笑花 2015')  #  输入名称
        homepage.add_names(Keys.ENTER)  #  回车
        # cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  #  获取第一行产品列表名称
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  #  获取第一行产品列表名称
        homepage.table_input()      #点击复选
        driver.find_element_by_xpath('//*[@id="batchAddPkgs"]').click()     #点击加入产品包
        time.sleep(2)
        homepage.s_PkgName(ks_name)
        homepage.s_BtnSearch()  #搜索按钮
        ass1 = driver.find_element_by_xpath('//*[@id="UnbindPkgTable"]/tbody/tr/td[2]').text
        try:
            assert ass1 == ks_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.unbindPkgTable()#点击复选
        homepage.add_package_dialog() #导入
        space1 = driver.find_element_by_xpath('//*[@id="SelPkgTable"]/tbody/tr/td[2]').text
        try:
            assert space1 == ass1
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.btnSaves()      #点击确认
        try:
            assert VodSearch.get_ass_text(self) == '产品已经加入产品包中'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()    #确认按钮
        homepage.coLLapseTwo()    #  点击产品包列表
        homepage.searchBtn()    #  点击搜索
        homepage.add_names(ks_name)   #  输入产品包名称
        homepage.add_names(Keys.ENTER)
        homepage.glyphicon_edit()  #  点击编辑
        homepage.chooseProduct()  #  点击选择产品
        homepage.selectedProductName(cp_name)  #  输入已选产品
        homepage.selectedProductName(Keys.ENTER)
        selected_name = driver.find_element_by_xpath('//*[@id="selectedProductTable"]/tbody/tr/td[2]').text   #  获取已选产品名称
        try:
            assert selected_name == cp_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.click_duig()  #  点击复选
        homepage.prd_Remove()  #  向左移除
        homepage.btnSaves()  #  点击确认
        homepage.edit_package_form()  #  点击保存
        homepage.confirm_1()  #  点击确认

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()





