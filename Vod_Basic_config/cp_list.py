# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch

cp = '环球合一CP'
#cp列表
class cpList(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Newly_added(self):
        """新增"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.jc_peizhi()   #点击基础配置
        homepage.cp_collapseThree()#点击cp列表
        homepage.toolbar()#点击新增
        homepage.frmCP(cp)#输入cp名称
        rand = random.randint(100, 10000)
        homepage.frmCP_code(rand)#输入cp编码
        homepage.startDate()#点击起始日期
        driver.execute_script("window.scrollBy(0,300)")
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[4]/div[3]/table/tfoot/tr/th').click()
        time.sleep(1)
        homepage.emdDate()#点击截止日期
        driver.find_element_by_xpath('/html/body/div[5]/div[3]/table/tfoot/tr/th').click()
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        homepage.btnAdds()#点击新增
        homepage.cp_collapseThree()  # 点击cp列表

    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.cpNames(cp)#输入cp名称
        homepage.btnSearch()#点击搜索
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert name == cp
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Enable(self):
        """启用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()#点击对勾
        homepage.btnUps()#点击启用
        try:
            assert VodSearch.get_ass_text(self) == '状态修改成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#点击确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        try:
            assert state == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Disable(self):
        """停用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()  # 点击对勾
        homepage.btnDowns()  # 点击停用
        try:
            assert VodSearch.get_ass_text(self) == '状态修改成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()  # 点击确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        try:
            assert state == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_edits()#点击编辑按钮
        homepage.frmCP('（编辑）')
        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        homepage.btnUpdates()#点击保存
        homepage.cp_collapseThree()  # 点击cp列表
        homepage.cpNames(cp+'（编辑）')  # 输入cp名称
        homepage.btnSearch()  # 点击搜索
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert new_name == cp+'（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_Input()  # 点击对勾
        homepage.custom_delete()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#点击确认
        col = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert col == '没有找到匹配的记录'
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