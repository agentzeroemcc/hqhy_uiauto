# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from Vod_Content_management.EpisodesList import VodSearch
from selenium.webdriver.support.ui import Select
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger

logger = Logger(logger="BasePage").getlog()
test_name1 = 'AgentZero'
# 用户管理
class Consumer(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Add_to(self):
        """新增"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.recommend()  # 点击用户权限
        homepage.dj_jiemj()  # 点击用户管理
        homepage.newly_added()  # 点击新建
        driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#user_edit.modal.fadein.in div.modal-dialog div.modal-content div.modal-body form#myForm.form-horizontal div.form-group div.col-sm-8.col-xs-2 input#loginName.form-control').send_keys(test_name1)
        # homepage.login_name1(test_name1)  # 输入登录名
        test_name2 = 'KANjian123'
        homepage.login_pwd(test_name2)  # 输入登录密码
        homepage.login_pwd_2(test_name2)  # 输入确认密码
        test_name3 = test_name1+'测试'
        homepage.edit_name2(test_name3)  # 输入名称
        Select(driver.find_element_by_id('roleId')).select_by_value('4')  # 选择用户角色
        homepage.binding()  # 点击绑定业务组合
        homepage.select_all()  # 点击select_all
        # homepage.telephone1()  # 点击联系电话框
        # time.sleep(1)
        test_name4 = '18583250213'
        homepage.telephone2(test_name4)  # 输入联系电话
        homepage.preservation4()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '添加成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定


    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.test_name = test_name1
        homepage.inputname(self.test_name)  # 输入内容
        homepage.click_search()  # 点击搜索

        ass_name1 = driver.find_element_by_xpath('//*[@id="user_table"]/tbody/tr/td[3]').text
        try:
            assert ass_name1 == self.test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()


    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        self.test_name = test_name1+'测试'
        homepage.click_edit()  # 点击编辑
        homepage.edit_name2('编辑')  # 输入名称
        homepage.preservation4()  # 点击保存
        try:
            assert VodSearch.get_ass_text(self) == '修改成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定

        new_name = driver.find_element_by_xpath('//*[@id="user_table"]/tbody/tr/td[6]').text
        try:
            self.assertEqual(test_name1+'测试编辑',new_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_see(self):
        """查看用户"""
        homepage = HomePage(self.driver)
        driver = self.driver
        driver.find_element_by_xpath('//*[@id="user_table"]/tbody/tr/td[2]/a[2]/i').click()
        time.sleep(2)
        see_name = driver.find_element_by_xpath('//*[@id="userModalLabel"]').text
        try:
            assert see_name == '查看用户'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        driver.find_element_by_xpath('//*[@id="myForm"]/div[9]/button[2]').click()   #  点击关闭
        time.sleep(1)

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.click_del()
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '删除成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 点击确定
        matching = driver.find_element_by_xpath('//*[@id="user_table"]/tbody/tr/td').text
        try:
            assert matching == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.reset_table()   #   点击重置
        input_name = driver.find_element_by_xpath('//*[@id="searchForm"]/div[1]/label[2]/input').text
        logon_name = driver.find_element_by_xpath('//*[@id="user_table"]/tbody/tr[1]/td[3]').text
        try:
            assert input_name == '' and logon_name == 'admin'
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