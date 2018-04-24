# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()

#消息服务器列表
class Message_server(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Newly_added(self):
        """新增"""
        Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.column_M()  # 点击消息管理
        homepage.OnecollapseOne()  #  点击“消息服务器列表”
        # http = driver.find_element_by_xpath('//*[@id="sock_code6"]').text  #  获取URL
        http = driver.find_element_by_xpath('//*[@id="sock_code7"]').text  #  获取URL
        node_n = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[1]/td[4]').text  #  获取节点名称
        homepage.custom_new_toolbar() #  点击新增
        homepage.add_url(http)  #  输入URL
        homepage.node_name('test-' + node_n)  #  输入节点名称
        homepage.secret_key('2d2cfaa4-bf42-47b8-b6b8-2a64bcdd31e0')   #   输入密钥
        homepage.opt_btn()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '新增成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        """搜索"""
        homepage.search_name('test-' + node_n)  #  输入节点名称
        node_test = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr/td[4]').text  # 获取要匹配的节点名称
        try:
            assert node_test == 'test-' + node_n
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        local_test = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr/td[4]').text
        homepage.table_msg_server()  #  点击编辑
        homepage.node_name('-edit')  #  输入编辑名称
        homepage.opt_btn()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '修改成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        node_name = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr/td[4]').text  #  获取节点名称
        logger.info('aaaaaaaaaa%s'%node_name)
        try:
            assert node_name == local_test + '-edit'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Start_stop(self):
        """启用/停用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.msg_server_table()  #  点击停用
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功停用1个节点'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#确认
        judge = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr/td[12]/span').text
        try:
            assert judge == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """启用"""
        homepage.msg_server_table()  #  点击启用
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功启用1个节点'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        judge1 = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr/td[12]/span').text
        try:
            assert judge1 == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_batch_stop(self):
        """批量停用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.reset_table()  #  点击重置
        Select(driver.find_element_by_id('serach_status')).select_by_value('0')  # 状态：启用
        time.sleep(1)
        node_n = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[1]/td[4]').text  #  获取节点名称
        node_n1 = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[2]/td[4]').text  #  获取节点名称
        homepage.msg_server_table_input()  #  点击复选
        homepage.msg_server_table_input1()  #  点击复选
        homepage.stop_custom_toolbar()  #  点击停用
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功停用2个节点'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        Select(driver.find_element_by_id('serach_status')).select_by_visible_text('全部')  # 状态：全部
        homepage.search_name(node_n)  #  输入节点名称
        def judge():
            state = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[1]/td[12]/span').text  #  获取状态
            try:
                assert state == '停用'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.reset_table()  #  重置
        judge()
        homepage.search_name(node_n1)  # 输入节点名称
        judge()

    def test_batch_start(self):
        """批量启用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('serach_status')).select_by_value('1')  # 状态：停用
        time.sleep(1)
        node_n = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[1]/td[4]').text  #  获取节点名称
        node_n1 = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[2]/td[4]').text  #  获取节点名称
        homepage.msg_server_table_input()  #  点击复选
        homepage.msg_server_table_input1()  #  点击复选
        homepage.start_custom_toolbar()  #  点击启用
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功启用2个节点'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        Select(driver.find_element_by_id('serach_status')).select_by_visible_text('全部')  # 状态：全部
        homepage.search_name(node_n)  #  输入节点名称
        def judge():
            state = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr[1]/td[12]/span').text  #  获取状态
            try:
                assert state == '启用'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.reset_table()  #  重置
        judge()
        homepage.search_name(node_n1)  # 输入节点名称
        judge()

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_name('test-test')  #  输入要删除的名称
        homepage.del_msg_server_table()  #  点击删除
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功删除1条记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        matching = driver.find_element_by_xpath('//*[@id="msg_server_table"]/tbody/tr/td').text
        try:
            assert matching == '没有找到匹配的记录'
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





