# -*- coding:utf-8 -*-
import unittest,time,random
import os
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
test_name = '自动化推荐位管理'
edit_name = test_name + '（编辑）'
#推荐位管理
class Recommend_M(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_New_add(self):
        """新增"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击导航管理
        homepage.collapseOnes()#点击推荐位管理
        homepage.add_recomm()#新增
        homepage.add_names(test_name)#输入名称
        Select(driver.find_element_by_id('recommendtemplatecode')).select_by_value('1100073160311170000135787')#下拉选择推荐
        homepage.btnCreates()#添加

    def test_Search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.recommendName(test_name)#输入搜索
        homepage.btnRecommendSearch()#点击搜索
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text#获取文本
        try:
            self.assertEqual(test_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Status(self):#状态改变
        """状态改变"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()#点击复选框
        homepage.shutdown()#点击停用
        homepage.confirm_1()  # 点击确定
        ass_stop = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text#获取文本内容
        try:
            self.assertEqual('停用', ass_stop)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.table_Input()#点击复选框
        homepage.startup()#点击启用
        homepage.confirm_1()#点击确定
        ass_start = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text#获取文本内容
        try:
            self.assertEqual('启用', ass_start)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Bj()#点击编辑
        homepage.clear_names()#清除名称
        homepage.add_names(edit_name)#输入名称
        Select(driver.find_element_by_id('recommendtemplatecode')).select_by_value('1100073160318150000953555')#下拉选择专题
        homepage.btnSaves()  # 更新
        homepage.recommendName(edit_name)  # 输入搜索
        homepage.btnRecommendSearch()  # 点击搜索
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text#获取文本
        try:
            self.assertEqual(edit_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Details(self):
        """详情"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.glyphicon_edit()#点击详情
        driver.refresh()#刷新界面
        time.sleep(4)

    def get_svg(self):
        driver = self.driver
        svgelem = driver.find_element_by_xpath('//*[@id="layoutBrowse"]/*[name()="svg"]/*[name()="rect"][1]')
        action = ActionChains(driver)
        action.click(svgelem).perform()  # 点击1号位

    def test_New_search(self):
        """详情新增搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('SEARCH')#下拉选择搜索
        test2_name = '搜索'
        homepage.showname(test2_name)  #  输入显示名称
        homepage.add_names(test2_name)#输入名称
        picture_path = os.path.abspath('..') + "\\picture\\1.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        time.sleep(2)
        homepage.upLoadbtn()#点击上传按钮
        time.sleep(2)
        homepage.btnCreates()#点击添加
        ass_search = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test2_name == ass_name and ass_search == '搜索'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_collection(self):
        """详情新增收藏"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('FAVOERITE')  # 下拉选择收藏列表
        test3_name = '收藏列表'
        homepage.showname(test3_name)  # 输入显示名称
        homepage.add_names(test3_name)
        picture_path = os.path.abspath('..') + "\\picture\\2.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()
        ass_collection = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text#获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test3_name == ass_name and ass_collection == '收藏列表'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_history(self):
        """详情新增播放历史"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('HISTORY')  # 下拉选择播放历史
        test4_name = '播放历史'
        homepage.showname(test4_name)  # 输入显示名称
        homepage.add_names(test4_name)
        picture_path = os.path.abspath('..') + "\\picture\\3.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()
        ass_history = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test4_name == ass_name and ass_history == '播放历史'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_center(self):
        """详情新增个人中心"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('CENTER')  # 下拉选择个人中心
        test5_name = '个人中心'
        homepage.showname(test5_name)  # 输入显示名称
        homepage.add_names(test5_name)
        picture_path = os.path.abspath('..') + "\\picture\\4.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()
        ass_center = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test5_name == ass_name and ass_center == '个人中心'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_Setting(self):
        """详情新增设置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('SETTING')  # 下拉选择搜索
        test6_name = '设置页'
        homepage.showname(test6_name)  # 输入显示名称
        homepage.add_names(test6_name)#输入名称
        picture_path = os.path.abspath('..') + "\\picture\\5.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()#点击添加
        ass_setting = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test6_name == ass_name and ass_setting == '设置页'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_vod_Package(self):
        """详情新增点播产品包"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击导航管理
        # homepage.collapseOnes()  # 点击推荐位管理
        # homepage.recommendName(edit_name)  # 输入名称
        # homepage.recommendName(Keys.ENTER)
        # homepage.glyphicon_edit()  #  点击详情
        # time.sleep(3)
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('VOD')  # 下拉选择点播
        Select(driver.find_element_by_id('assetType')).select_by_value('2') #下拉框选择产品包
        driver.find_element_by_xpath('//*[@id="productAllSelector"]').click()#点击选择产品(包)
        # driver.find_element_by_xpath('//*[@id="product_selector"]/div/div/div[2]/div[1]/div[1]/div/button').click()
        test7_name = '动漫-益智（全优酷）'
        homepage.allKeyword(test7_name)#输入名称
        homepage.btnAllKeywordSearch()#点击搜索
        homepage.selectorTable()#选择产品包
        time.sleep(4)
        homepage.btnAllSelected()#点击确认
        # homepage.product_play_info()#点击关闭
        picture_path = os.path.abspath('..') + "\\picture\\6.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()#点击添加
        ass_package = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text#获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test7_name == ass_name and ass_package == '点播'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_Vod_Product(self):
        """详情新增点播产品"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('VOD')  # 下拉选择点播
        Select(driver.find_element_by_id('assetType')).select_by_value('1')  # 下拉框选择产品
        driver.find_element_by_xpath('//*[@id="productAllSelector"]').click()  # 点击选择产品(包)
        time.sleep(3)
        test8_name = '虹色时光'
        homepage.allKeyword(test8_name)#输入名称
        # picture_path = os.path.abspath('..') + "\\picture\\6.jpg"
        # driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.btnAllKeywordSearch()#点击搜索
        homepage.selectorTable()  # 选择产品
        homepage.btnAllSelected()  # 点击确认
        # homepage.product_play_info()  # 点击关闭
        picture_path = os.path.abspath('..') + "\\picture\\7.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()  # 点击添加
        ass_product = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert test8_name == ass_name and ass_product == '点播'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_Special(self):
        """详情新增点播专题"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('VOD')  # 下拉选择点播
        Select(driver.find_element_by_id('assetType')).select_by_value('4')  # 下拉框选择专题汇总
        homepage.catSelector()#点击选择栏目
        # tree_name = driver.find_element_by_xpath('//*[@id="categoryTreeTable"]/tbody/tr[1]/td[2]').text
        homepage.categoryTreeTable()#选择栏目树  (AAS自动化测试（勿动）)
        homepage.btnSelectNext()  #点击选择下级栏目
        homepage.categoryTable()#选择栏目
        homepage.btnSelectCategory()#点击选择栏目按钮
        picture_path = os.path.abspath('..') + "\\picture\\7.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        time.sleep(2)
        homepage.btnCreates()# 点击添加
        ass_product = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        # ass_product = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        # ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # 获取文本
        try:
            assert ass_name == 'AAS自动化测试（勿动）' and ass_product == '点播'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_New_Column(self):
        """详情新增点播栏目"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击导航管理
        # homepage.collapseOnes()  # 点击推荐位 管理
        # homepage.recommendName(edit_name)  # 输入搜索
        # homepage.btnRecommendSearch()  # 点击搜索
        # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[2]/i').click()  #  点击详情
        # time.sleep(10)
        self.get_svg()
        homepage.add_recomm()  # 点击新增
        Select(driver.find_element_by_id('serviceType')).select_by_value('VOD')  # 下拉选择点播
        Select(driver.find_element_by_id('assetType')).select_by_value('3')#下拉选择栏目
        homepage.catSelector()#点击选择栏目
        homepage.categoryTreeTable()  # 选择栏目树
        homepage.btnSelectNext()  # 点击选择下级栏目
        homepage.categoryTable()  # 选择栏目
        homepage.btnSelectCategory()  # 点击选择栏目按钮
        picture_path = os.path.abspath('..') + "\\picture\\7.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnCreates()  # 点击添加
        ass_product = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert ass_name == 'AAS自动化测试（勿动）' and ass_product == '点播'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Child_state(self):
        """具体推荐位状态改变"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        time.sleep(5)
        # homepage.table_input0()#选择所有
        # homepage.shutdown()  # 点击停用
        # homepage.button_1()#点击确认按钮
        homepage.table_input0()  # 选择所有
        homepage.startup()#点击启用
        homepage.button_1()  # 点击确认按钮
        ass_start = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  # 获取文本内容
        try:
            self.assertEqual('启用', ass_start)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Child_edit(self):
        """具体推荐位编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        time.sleep(5)
        homepage.table_2()#点击编辑
        Select(driver.find_element_by_id('serviceType')).select_by_value('GAME')  # 下拉选择游戏
        homepage.clear_names()  # 清除名称
        test9_name = '游戏'
        homepage.add_names(test9_name)  # 输入名称
        # homepage.pictureDeletebtn()  # 删除图片
        picture_path = os.path.abspath('..') + "\\picture\\7.jpg"
        driver.find_element_by_id('posterFile').send_keys(picture_path)  # 上传图片
        homepage.upLoadbtn()  # 点击上传按钮
        homepage.btnSaves()  # 点击添加
        ass_edit = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text  # 获取文本
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert ass_name == test9_name and ass_edit == '游戏'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Child_delete(self):
        """具体推荐位删除节目集"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.get_svg()
        time.sleep(5)
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        homepage.delete_an()#点击删除按钮
        alert = driver.switch_to_alert()#定位弹出对话框
        alert.accept()#点击对话框“确定”按钮
        homepage.button_1()#点击确认按钮
        homepage.searchDetailbtn(ass_name1)  # 输入名称
        homepage.searchDetailbtn(Keys.ENTER)  # 点击回车键
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text  # 获取文本
        try:
            assert ass_name2 == '没有找到匹配的记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.searchDetailbtnc()#清除名称

    def test_Child_search(self):
        """具体推荐位搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        test4_name = '播放历史'
        homepage.searchDetailbtn(test4_name)#输入名称
        homepage.searchDetailbtn(Keys.ENTER)#点击回车键
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            assert ass_name == test4_name
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.searchDetailbtnc()#清除名称

    def test_Move(self):
        """移动"""
        homepage = HomePage(self.driver)
        driver = self.driver

        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()#点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()#选择oms
        # time.sleep(2)
        # homepage.search_Content()  # 点击导航管理
        # homepage.collapseOnes()  # 点击推荐位管理
        # homepage.recommendName(edit_name)  # 输入名称
        # homepage.btnRecommendSearch()  # 点击搜索
        # homepage.glyphicon_edit()  # 点击详情

        self.get_svg()
        time.sleep(5)
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text  # 获取文本
        homepage.table_input1()  # 点击复选框
        homepage.moveTo()  # 点击移动
        Select(driver.find_element_by_id('move_to_idx')).select_by_value('5')#选择推荐位号
        time.sleep(2)
        homepage.btnMoveTo()  # 点击移动
        homepage.button_1()  # 点击确认
        svgelem = driver.find_element_by_xpath('//*[@id="layoutBrowse"]/*[name()="svg"]/*[name()="rect"][5]')
        action = ActionChains(driver)
        action.click(svgelem).perform()  # 点击5号位
        time.sleep(5)
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  # 获取文本
        try:
            self.assertEqual(ass_name1, ass_name2)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Top(self):
        """置顶"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()#点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()#选择oms
        # time.sleep(2)
        # homepage.search_Content()  # 点击导航管理
        # homepage.collapseOnes()  # 点击推荐位管理
        # homepage.recommendName(edit_name)  # 输入名称
        # homepage.btnRecommendSearch()  # 点击搜索
        # homepage.glyphicon_edit()  # 点击详情
        self.get_svg()
        time.sleep(5)
        ass_status = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]').text # 获取文本
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text  # 获取文本
        try:
            self.assertEqual(ass_status, '启用')
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        # homepage.table_input1()#点击复选框
        # homepage.topBtn()#点击置顶按钮
        homepage.tab_Deta()#点击置顶按钮
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # 获取文本
        try:
            self.assertEqual(ass_name1, ass_name2)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Upmove(self):
        """位置上移"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()#点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()#选择oms
        # time.sleep(2)
        # homepage.search_Content()  # 点击导航管理
        # homepage.collapseOnes()  # 点击推荐位管理
        # homepage.recommendName(edit_name)  # 输入名称
        # homepage.btnRecommendSearch()  # 点击搜索
        # homepage.glyphicon_edit()  # 点击详情
        self.get_svg()
        time.sleep(5)
        ass_status = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]').text  # 获取文本
        try:
            self.assertEqual(ass_status, '启用')
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text#获取文本内容
        homepage.upMovebtn()  # 点击移动
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # 获取文本
        try:
            self.assertEqual(ass_name1, ass_name2)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Recommendation(self):
        """返回推荐位列表"""
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/h2/small/a').click()

    def test_Delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.recommendName(edit_name)  # 输入搜索
        homepage.btnRecommendSearch()  # 点击搜索
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  # 获取文本
        try:
            self.assertEqual(edit_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.table_Input()#点击复选框
        homepage.remove()#点击删除
        alert = driver.switch_to_alert() #定位弹出对话框
        alert.accept()#点击对话框“确定”
        homepage.confirm_1()#点击确定

    def Newly_added(self):
        homepage = HomePage(self.driver)
        homepage.add_recomm()  # 点击新增
        homepage.productAllSelector()  # 点击选择产品（包）
        homepage.allKeyword('文雀 高清')  # 点击选择产品（包）
        homepage.allKeyword(Keys.ENTER)  # 回车
        homepage.selectorTabl()  # 点击复选
        homepage.btnAllSelected()  # 点击确认
        # homepage.product_play_info()  # 点击关闭
        homepage.btnCreates()  # 点击添加
        homepage.table_input1()  # 点击复选
        homepage.startup()  # 点击启用
        homepage.button_1()  # 点击确认

    def synchron_ES(self):
        homepage = HomePage(self.driver)
        homepage.collapseOnes()  # 点击推荐位 管理
        homepage.sync_data()  #  点击同步到ES
        homepage.confirm_1()  #  确认
        homepage.recommendName('推荐位自动化测试')  # 输入搜索内容
        homepage.recommendName(Keys.ENTER)
        homepage.glyphicon_edit()  #点击编辑

    def test_Recommended_bit_interface(self):
        """推荐位接口测试"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击导航管理
        homepage.collapseOnes()  # 点击推荐位 管理
        homepage.recommendName('推荐位自动化测试')  # 输入搜索内容
        homepage.btnRecommendSearch()  # 点击搜索
        homepage.glyphicon_edit()  # 点击详情
        def click_four():
            svgelem = driver.find_element_by_xpath('//*[@id="layoutBrowse"]/*[name()="svg"]/*[name()="image"][4]')
            action = ActionChains(driver)
            action.click(svgelem).perform()  # 点击4号位
        click_four()
        self.Newly_added()
        self.synchron_ES()
        Interface.Newly_added_interface(self)    #   推荐位新增启用接口
        """位置上移"""
        click_four()
        homepage.upMovebtn()  #  点击位置上移
        self.synchron_ES()
        Interface.delete_inter(self)  #  位置上移接口测试
        click_four()
        """移动"""
        homepage.table_input()  #  点击复选
        homepage.moveTo()   #  点击移动
        Select(driver.find_element_by_id('move_to_idx')).select_by_value('9')
        homepage.btnMoveTo()   #   点击移动
        homepage.button_1()   #   点击确认
        self.synchron_ES()
        Interface.btnMoveTo_interface(self)  #   移动接口测试
        """置顶"""
        def click_nine():
            svgelem = driver.find_element_by_xpath('//*[@id="layoutBrowse"]/*[name()="svg"]/*[name()="image"][9]')
            action = ActionChains(driver)
            action.click(svgelem).perform()  # 点击9号位
        click_nine()
        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        # driver.execute_script("window.scrollBy(0,5000)")
        # time.sleep(1)
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[2]/a[2]/i').click()  #  点击置顶
        time.sleep(2)
        self.synchron_ES()
        Interface.Top_interface(self)   #  置顶接口
        click_nine()
        """停用"""
        homepage.table_input()   #   点击1复选
        homepage.table_input1()   #   点击2复选
        homepage.shutdown()   #   点击停用
        homepage.button_1()   #   点击确认
        self.synchron_ES()
        Interface.Shutdown_interface(self)  #  停用接口测试
        click_nine()
        homepage.table_input0()  #z点击所有复选
        # try:
        #     inputs = driver.find_elements_by_name('btSelectItem')
        #     for input in inputs:
        #         if input.get_attribute('type') == 'checkbox':
        #             input.click()
        # except Exception as e:
        #     print(e)
        # time.sleep(2)
        homepage.startup()    #    点击启用
        homepage.button_1()    #    点击确认
        homepage.searchDetailbtn('神探夏洛克')  #  输入搜索名称
        homepage.table_Input()  #  点击复选
        homepage.moveTo()  #  点击移动
        Select(driver.find_element_by_id('move_to_idx')).select_by_value('4')
        homepage.btnMoveTo()  # 点击移动
        homepage.button_1()  # 点击确认
        homepage.searchDetailbtnc()  # 清空搜索框
        homepage.searchDetailbtn(Keys.ENTER)
        homepage.upMovebtn()  # 点击位置上移
        click_four()  # 点击4号位
        # homepage.searchDetailbtnc()   #   清空搜索框
        homepage.searchDetailbtn('文雀')  # 输入搜索名称
        """编辑"""
        homepage.dj_shangxx()    #  点击编辑
        homepage.add_names('（编辑）')   #   添加编辑
        homepage.btnSaves()   #   添加更新
        homepage.upMovebtn()  # 点击位置上移
        self.synchron_ES()
        Interface.Edit_inter(self)    #编辑接口测试
        click_four()
        """删除"""
        homepage.delete_an()  #  点击删除
        driver.switch_to.alert.accept()
        homepage.button_1()  #  确认
        self.synchron_ES()
        Interface.delete_inter(self)   #  删除接口测试
        # time.sleep(2)

    def test_Recommended_JsEpg5(self):
        """江苏移动EPG5.0接口测试"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击导航管理
        homepage.collapseOnes()  # 点击推荐位 管理
        homepage.recommendName('江苏移动EPG5.0-精选')  # 输入推荐位名称
        homepage.recommendName(Keys.ENTER)  #
        homepage.glyphicon_edit()    #    点击详情
        svgelem = driver.find_element_by_xpath('//*[@id="layout_epg5_0_0"]')
        action = ActionChains(driver)
        action.click(svgelem).perform()  # 点击1号位
        self.Newly_added()
        Interface.JsEpg5_add(self)      #   新增接口
        """位置上移"""
        homepage.upMovebtn()  # 点击位置上移
        homepage.button_1()  #  确认
        Interface.JsEpg5_Move(self)  #  位置上移接口
        """移动"""
        homepage.table_input()  # 点击复选
        homepage.moveTo()  # 点击移动
        Select(driver.find_element_by_id('move_to_idx')).select_by_value('4')
        homepage.btnMoveTo()  # 点击移动
        homepage.button_1()  # 点击确认
        Interface.Moveto_four(self)  # 移动接口测试
        """置顶"""
        svgelem = driver.find_element_by_xpath('//*[@id="layout_epg5_0_3"]')
        action = ActionChains(driver)
        action.click(svgelem).perform()  # 点击4号位
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[2]/a[2]/i').click()  # 点击置顶
        time.sleep(2)
        homepage.button_1()   #  点击确定
        Interface.Moveto_top(self)  # 置顶接口
        """停用"""
        homepage.table_input()  # 点击1复选
        homepage.shutdown()  # 点击停用
        homepage.button_1()  # 点击确认
        Interface.Moveto_four(self)  # 停用接口测试
        homepage.table_input1()  #  点击2复选
        homepage.startup()  # 点击启用
        homepage.button_1()  # 点击确认
        homepage.table_input1()  # 点击2复选
        homepage.moveTo()  # 点击移动
        Select(driver.find_element_by_id('move_to_idx')).select_by_value('1')
        homepage.btnMoveTo()  # 点击移动
        homepage.button_1()  # 点击确认
        svgelem = driver.find_element_by_xpath('//*[@id="layout_epg5_0_0"]')
        action = ActionChains(driver)
        action.click(svgelem).perform()  # 点击1号位
        homepage.search_detail_showName('文雀')  # 输入搜索名称
        """编辑"""
        homepage.dj_shangxx()  # 点击编辑
        homepage.add_names('（编辑）')  # 添加编辑
        homepage.btnSaves()  # 添加更新
        homepage.upMovebtn()  # 点击位置上移
        homepage.button_1()  # 确认
        Interface.JsEpg5_edit(self)  # 编辑接口测试
        """删除"""
        homepage.delete_an()  # 点击删除
        driver.switch_to.alert.accept()
        homepage.button_1()  # 确认
        Interface.JsEpg5_Move(self)  # 删除接口测试
        time.sleep(2)

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()
