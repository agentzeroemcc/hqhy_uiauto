# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch

injec = '注入域测试'
#注入域列表
class InjectionList(unittest.TestCase):
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
        homepage.add_recomm()#点击新增按钮
        address = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[4]/td[6]').text
        homepage.add_names(injec)#输入名称
        homepage.interfaceURL(address)#输入接口地址
        rand = random.randint(100, 10000)
        homepage.cmsID(rand)#输入上层节点编号
        homepage.sopID(rand)#输入本层节点编号
        homepage.domaininjection_form()#点击确定
        try:
            assert VodSearch.get_ass_text(self) == '操作成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert name == injec
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.send_submit_btn()#点击编辑
        homepage.add_names('（编辑）')#加入编辑
        homepage.domaininjection_form()#确认
        try:
            assert VodSearch.get_ass_text(self) == '操作成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()  # 确认
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert new_name == injec + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.edit_product()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认
        new_names = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert new_names != injec + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Task_query(self):
        """任务查询"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.jc_peizhi()  # 点击基础配置
        homepage.collapseThree()#点击任务查询
        Select(driver.find_element_by_id('taskStatus')).select_by_value('已请求')
        time.sleep(2)
        text = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr/td').text
        texts = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[4]').text
        try:
            assert text == '没有找到匹配的记录' or texts == '已请求'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('taskStatus')).select_by_value('处理中')
        time.sleep(2)
        text1 = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr/td').text
        text2 = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr/td[6]').text
        try:
            assert text1 == '没有找到匹配的记录' or text2 == '处理中'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('taskStatus')).select_by_value('已处理')
        time.sleep(2)
        statu = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[4]').text
        try:
            assert statu == '已处理'
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



