# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.Interface_test import Interface

#升级任务
class Upgrade(unittest.TestCase,Interface):
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
        homepage.busines_com()  # 点击业务组合
        homepage.collapseThree1()  #  点击升级任务
        Select(driver.find_element_by_id('allServiceCombo')).select_by_value( '1100121023874101446610014')  # --选择业务组合--   福建联通
        task_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  #  获取任务名称
        homepage.add_recomm()  #  点击新增
        homepage.add_names(task_name + '（测试）')  #  输入升级名称
        homepage.upgradeSeq('V2.1.1')  #  输入升级序列
        homepage.addUpgradeType()  #  点击添加终端升级
        homepage.upload_versionSeq('729')  #  输入版本序列
        driver.find_element_by_id('upload_apk_file').send_keys('d:\\EPG-YH-FJLT-VER4.01.200-20161117-F.apk')  #  上传APK文件
        homepage.upload_md5('9C84A6B01A2648683C3353217101B853')  #  输入MD5
        homepage.submitTitle()  #  点击保存
        homepage.addMacs()  #  点击“选择MAC / 批次”
        mac = driver.find_element_by_xpath('//*[@id="comboMacTable"]/tbody/tr[1]/td[2]').text
        with open('D:\\mac.txt', 'w', encoding='utf-8') as ff:
            ff.write(mac)
        driver.find_element_by_xpath('//*[@id="comboMacTable"]/tbody/tr[1]/td[1]/input').click()  #  点击复选
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="saveComboMacs"]').click()  # 点击确定
        time.sleep(1)
        homepage.btnDeviceUpgrade()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        try:
            assert new_name == task_name + '（测试）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_enable(self):
        """启用"""
        driver = self.driver
        homepage = HomePage(self.driver)
        homepage.table_input()  #  点击复选
        homepage.startbutton()  #  点击启用
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '启用成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[11]').text   #  获取状态
        try:
            assert state == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        Interface.Task_recommend(self)   #  调用升级任务接口

    def test_disable(self):
        """停用"""
        driver = self.driver
        homepage = HomePage(self.driver)
        homepage.table_input()  #  点击复选
        homepage.stopbutton()  #  点击停用
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '停用成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[11]').text   #  获取状态
        try:
            assert state == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        driver = self.driver
        homepage = HomePage(self.driver)
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text   #  获取修改前名称
        homepage.business_edit()  #  点击编辑
        homepage.add_names('（编辑）')  #  编辑名称
        homepage.btnDeviceUpgrade()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        modify_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        try:
            assert modify_name == name + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_delete(self):
        """删除"""
        driver = self.driver
        homepage = HomePage(self.driver)
        modify_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text
        homepage.table_input()  # 点击复选
        homepage.deleteModify()  #  点击删除
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '删除成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        after_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  #  获取删除后的名称
        try:
            assert after_name != modify_name
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
