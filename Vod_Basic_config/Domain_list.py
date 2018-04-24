# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
#分发域列表
class DomainList(unittest.TestCase):
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
        homepage.jc_peizhi()        #点击基础配置
        homepage.collapseThree1()   #点击 分发域列表
        http = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[8]').text  #获取分发域接口地址
        homepage.custom_toolbar()   #点击新增
        homepage.add_names('分发域测试')    #输入名称
        homepage.interfaceURL(http) #输入分发域接口地址
        homepage.cmsID('001')   #输入本层节点编号
        homepage.sopID('002')    #输入下层节点编号
        homepage.prioritys('3') #输入优先级
        driver.find_element_by_xpath('//*[@id="domain_form"]/div[2]/div/button[1]').click()#点击保存
        time.sleep(2)
        js = "var q=document.documentElement.scrllTop=10000"
        driver.execute_script(js)
        time.sleep(3)
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[3]').text
        try:
            assert name == '分发域测试'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Disable(self):
        """停用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_10_input()   #点击对勾
        homepage.customtoolbar2()#点击停用按钮
        try:
            assert VodSearch.get_ass_text(self) == '状态修改成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#点击确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[10]/td[5]').text
        try:
            assert state == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Enable(self):
        """启用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_10_input()   #点击对勾
        homepage.customtoolbar()#点击启用按钮
        try:
            assert VodSearch.get_ass_text(self) == '状态修改成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#点击确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[10]/td[5]').text
        try:
            assert state == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_synchronization(self):
        """同步"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.jc_peizhi()  # 点击基础配置
        # homepage.collapseThree1()  # 点击 分发域列表
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[3]').text#获取匹配名称
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[1]/input').click()   #点击对勾
        time.sleep(1)
        # homepage.table_10_input()   #点击对勾
        homepage.custom4_toolbar()  #点击同步
        try:
            assert VodSearch.get_ass_text(self) == '分发域：'+name+'，同步操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[3]').text#获取匹配名称
        # homepage.i_tables()#点击编辑
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[2]/a[1]/i').click() #点击编辑
        time.sleep(1)
        homepage.add_names('（编辑）')#编辑信息
        driver.find_element_by_xpath('//*[@id="domain_form"]/div[2]/div/button[1]').click()#点击保存
        time.sleep(5)
        test_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[3]').text
        try:
            assert test_name == name + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Template_list(self):
        """显示模板列表"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.jc_peizhi()  # 点击基础配置
        # homepage.collapseThree1()  # 点击 分发域列表
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[2]/a[3]/i').click()#点击‘显示模板列表’
        time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[8]/div/div/div/div[1]/div/div[1]/div/div/button[1]').click()  #  点击新增按钮
        time.sleep(2)
        value = driver.find_element_by_xpath('//*[@id="create_templateFileId2"]/option[1]').text  #  获取模板文件名称
        homepage.create_template_form()#点击新建
        try:
            assert VodSearch.get_ass_text(self) == '添加操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        mu_name = driver.find_element_by_xpath('//*[@id="templateTable"]/tbody/tr/td[4]').text    #  获取模板文件名称
        try:
            assert mu_name == value
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """编辑"""
        homepage.templateTable()#点击编辑
        Select(driver.find_element_by_id('edit_templateFileId2')).select_by_value('10')#选择名为‘jiangsu_yidong.ftl’的模板文件名称
        value2 = driver.find_element_by_xpath('//*[@id="edit_templateFileId2"]/option[2]').text   #  获取模板文件名称
        Select(driver.find_element_by_id('edit_isUse2')).select_by_value(
            '0')  # 选择不可用
        valueno = driver.find_element_by_xpath('//*[@id="edit_isUse2"]/option[2]').text  # 不可用
        homepage.edit_template_form()#点击保存
        try:
            assert VodSearch.get_ass_text(self) == '编辑操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        new_mu = driver.find_element_by_xpath('//*[@id="templateTable"]/tbody/tr/td[4]').text
        able = driver.find_element_by_xpath('//*[@id="templateTable"]/tbody/tr/td[8]').text
        try:
            assert new_mu == value2 and valueno == able
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """删除"""
        homepage.templateTable2()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除操作成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        text = driver.find_element_by_xpath('//*[@id="templateTable"]/tbody/tr/td').text
        try:
            assert text == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.show_domainTemplate_dialog()#点击关闭

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[2]/a[2]/i').click() #点击删除按钮
        time.sleep(1)
        # homepage.table_delete()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除分发域成功！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()#确认

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()




