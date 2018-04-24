# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface

test_name = '全局导航测试'
#全局导航
class Global(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def Oms_sign_in(self):
        VodSearch.test_Sign_in(self)
        driver = self.driver
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()  # 选择oms
        time.sleep(2)

    def test_Add_to(self):
        """添加"""
        self.Oms_sign_in()
        homepage = HomePage(self.driver)
        homepage.search_Content()#点击导航管理
        homepage.custom_add_toolbar()#点击添加
        homepage.add_names(test_name)#输入导航名称
        homepage.btnCreateGlobalNav()#点击添加

    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.navName(test_name)#输入内容
        homepage.btnSearch()#点击搜索
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            assert ass_name == test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Bj()#点击编辑
        homepage.add_names('（编辑）')#输入名称
        homepage.btnSaveGlobalNav()#点击更新
        homepage.navName(test_name+'（编辑）')  # 输入内容
        homepage.btnSearch()  # 点击搜索
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            self.assertEqual(test_name+'（编辑）',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_details(self):
        """详情"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()  # 选择oms
        # time.sleep(2)
        # homepage.search_Content()  # 点击导航管理
        homepage.dj_jiemj()  #  点击全局导航
        homepage.navName('福建联通')
        homepage.btnSearch()  #  点击搜索
        homepage.glyphicon_edit()#点击详情按钮
        """添加"""
        homepage.custom_add_toolbar()#点击添加
        test_name = '详情测试'
        homepage.add_names(test_name)#输入名称
        homepage.btnCreateNav()  #  点击添加
        Interface.name_interface(self)   #  新增详情名称接口测试
        time.sleep(2)
        homepage.detailTable()  #  点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('VOD')#下拉选择
        homepage.btnSaveNav()  #  点击更新
        Interface.Vod_interface(self)  #  选择业务类型测试  点播
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('LIVE')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.Live_interface(self)  # 选择业务类型测试  直播
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('APP')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.App_interface(self)  # 选择业务类型测试  应用
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('SETTING')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.Setting_interface(self)  # 选择业务类型测试  设置页
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('FAVOERITE')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.Favoerite_interface(self)  # 选择业务类型测试  收藏列表
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('HISTORY')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.History_interface(self)  # 选择业务类型测试  播放历史
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('ABOUT')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.About_interface(self)  # 选择业务类型测试  版本信息
        homepage.detailTable()  # 点击编辑
        Select(driver.find_element_by_id('servicetype')).select_by_value('SPECIAL_INDEX')  # 下拉选择
        homepage.btnSaveNav()  # 点击更新
        Interface.Special_index_interface(self)  # 选择业务类型测试  专题
        homepage.detailTable()  # 点击编辑
        def add_to():
            homepage.btnSelCategory()#点击选择栏目
            homepage.categoryTreeTable()#选择栏目树
            driver.find_element_by_xpath('//*[@id="btnSelectNext"]').click()#点击选择下级栏目
            time.sleep(2)
            homepage.categoryTable()#点击选择导航详情
            driver.find_element_by_xpath('//*[@id="btnSelectCategory"]').click()#点击选择栏目按钮
            time.sleep(1)
            try:
                add = driver.find_element_by_xpath('//*[@id="btnCreateNav"]').text
                if add == '添加':
                    homepage.btnCreateNav()  # 点击添加
                else:
                    homepage.btnSaveNav()  # 点击更新
            except Exception as e:
                print(e)
            Interface.CategoryCode_interface(self)  # 选择栏目，栏目树接口测试
            homepage.detailTable()  # 点击编辑
            homepage.btnSelComment()#点击选择推荐位
            homepage.selectorTable()#点击对勾
            homepage.btnSelected()#点击确认
            # homepage.btnCreateNav()#点击更新
            homepage.btnSaveNav()#点击更新
            Interface.Recommend_interface(self)
        add_to()
        ass_test = driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[2]/td[3]').text
        try:
            self.assertEqual('详情测试',ass_test)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        test_name1 = '导航详情测试'
        homepage.custom_add_toolbar()  # 点击添加
        homepage.add_names(test_name1)  # 输入名称
        Select(driver.find_element_by_id('servicetype')).select_by_value('LIVE')  # 下拉选择
        add_to()#调用封装函数的方法
        """编辑"""
        homepage.detailTable()#点击编辑
        homepage.add_names('（编辑）')#输入编辑名称
        homepage.btnSaveNav()#点击更新
        new_name = driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[2]/td[3]').text
        try:
            self.assertEqual(test_name1+'（编辑）',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        """位置上移"""
        homepage.detailTable2()#点击上移
        try:
            assert VodSearch.get_ass_text(self) == '上移成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()    # 确认
        sy_name = driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[2]/td[3]').text#详情测试
        sy_name1 = driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[3]/td[3]').text#导航详情测试（编辑）
        try:
            assert sy_name == test_name and sy_name1 == test_name1+'（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Interface.name_interface(self)  #  上移接口测试
        """删除"""
        homepage.detailTable4()#点击删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        Interface.Del_name_interface(self)  #  删除接口测试
        # homepage.detailTable4()  # 点击删除
        # driver.switch_to_alert().accept()
        # homepage.confirm_1()  # 确认
        """取消推荐位"""
        homepage.detailTable5()#点击取消推荐位
        try:
            self.assertEqual('推荐位取消成功。',VodSearch.get_ass_text(self))
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.confirm_1()#确认
        cancel = driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[2]/td[5]').text
        try:
            self.assertEqual('-',cancel)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        """取消跳转栏目"""
        homepage.detailTable6()#点击取消跳转栏目
        alert.accept()  # 点击对话框“确定”
        try:
            self.assertEqual('删除跳转栏目成功.',VodSearch.get_ass_text(self))
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.confirm_1()  # 确认
        cancel_jump = driver.find_element_by_xpath('//*[@id="detailTable"]/tbody/tr[2]/td[6]').text
        try:
            self.assertEqual('-',cancel_jump)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.detailTable4()  # 点击删除
        driver.switch_to_alert().accept()
        homepage.confirm_1()  # 确认

        """返回导航列表"""
        homepage.html_small()#点击返回导航列表
        nav = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/h2').text
        try:
            self.assertEqual('全局导航',nav)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())


    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.navName(test_name)  # 输入内容
        # homepage.btnSearch()  # 点击搜索
        homepage.dj_shangxx()  #  点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            self.assertEqual('删除成功',VodSearch.get_ass_text(self))
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.confirm_1()  # 确认
        matching = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            self.assertEqual('没有找到匹配的记录',matching)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()