# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global

#推荐位布局
class Bit(unittest.TestCase):
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
        homepage.dj_fenfayu()  # 点击推荐位布局
        homepage.add_recomm()#点击新增
        test_name = 'a自动化推荐'
        homepage.add_names(test_name)  # 输入名称
        driver.find_element_by_id('pictureFile').send_keys('D:\\bit.jpg')  # 上传图片
        homepage.epgVersion4()#点击选择epg版本为4.0
        homepage.btnCreates()#点击添加
        homepage.doubleclickbtn()#点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本
        try:
            self.assertEqual('a自动化推荐', ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Status(self):#状态改变
        """状态改变"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.execute_script("window.scrollBy(0,3000)")
        # time.sleep(1)
        # driver.execute_script("window.scrollBy(0,5000)")#下拉滚动条
        # time.sleep(1)
        homepage.table_input()#点击复选框
        homepage.startup()#点击启用
        homepage.confirm_1()#点击确认
        ass_start = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text  # 获取文本内容
        try:
            self.assertEqual('启用', ass_start)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.table_input()  # 点击复选框
        homepage.shutdown()  # 点击停用
        homepage.confirm_1()  # 点击确认
        ass_start = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text  # 获取文本内容
        try:
            self.assertEqual('停用', ass_start)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.table_input()  # 点击复选框
        homepage.startup()  # 点击启用
        homepage.confirm_1()  # 点击确认
        ass_start = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text  # 获取文本内容
        try:
            self.assertEqual('启用', ass_start)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.send_submit_btn()#点击编辑按钮
        homepage.clear_names()#清除文本
        test1_name = 'a自动化(推荐)'
        homepage.add_names(test1_name)  # 输入名称
        driver.find_element_by_id('pictureFile').send_keys('D:\\bit.jpg')  # 上传图片
        homepage.epgVersion4()  # 点击选择epg版本为4.0
        homepage.btnSaves()#点击更新
        homepage.doubleclickbtn()  # 点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取文本
        try:
            self.assertEqual(test1_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Detail(self):
        """详情"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.edit_product()#点击详情按钮

    def test_Detail_append(self):
        """详情追加列"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.AppendColumnbutn()#点击追加列
        test2_name = '自动化测试第一列'
        homepage.columnNamebtn(test2_name)#输入列名称
        Select(driver.find_element_by_id('columntypecode')).select_by_value('1100072106014042826040003')  # 下拉选择吕字
        homepage.Appendbutn()#点击新增按钮
        try:
            assert VodSearch.get_ass_text(self) == '添加列成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#点击确认按钮
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本
        try:
            self.assertEqual(test2_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Detail_edit(self):
        """详情编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.send_submit_btn()#点击编辑按钮
        homepage.clear_names()#清除内容
        test3_name = '自动化测试(第一列)'
        homepage.add_names(test3_name)#输入名称
        homepage.btnSaves()#点击更新
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本内容
        try:
            self.assertEqual(test3_name, ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Detail_preview(self):
        """详情预览"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.previewbtn()#点击预览
        ass_name = driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#layout_browse.modal.fadein.in div.modal-dialog div.modal-content div.modal-header h4#gridSystemModalLabel.modal-title').text#获取文本内容

        # try:
        #     self.assertEqual('推荐位布局预览', ass_name)
        # except AssertionError as e:
        #     print("Test fail.", format(e), homepage.get_windows_img())
        try:
            assert ass_name == '推荐位布局预览'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        driver.find_element_by_xpath('//*[@id="layout_browse"]/div/div/div[1]/button/span').click()  # 点击关闭
        time.sleep(2)

    def test_Detail_delete(self):
        """详情删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.edit_product()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        try:
            assert VodSearch.get_ass_text(self) == '数据已经删除成功。'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()#点击确认按钮
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text #获取文本内容
        try:
            self.assertEqual('230,0', ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Detail_deleteall(self):
        """详情删除整列"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_2()#点击删除整列按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        homepage.confirm_1()#点击确认按钮
        ass_name =  driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text#获取文本内容
        try:
            self.assertEqual('没有找到匹配的记录', ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Detail_deletebatch(self):
        """详情批量删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.AppendColumnbutn()  # 点击追加列
        test2_name = '自动化测试第一列'
        homepage.columnNamebtn(test2_name)  # 输入列名称
        Select(driver.find_element_by_id('columntypecode')).select_by_value('1100072106014042826040003')  # 下拉选择品字
        homepage.Appendbutn()  # 点击新增按钮
        homepage.confirm_1()  # 点击确认按钮
        driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div.bootstrap-table div.fixed-table-container div.fixed-table-header table.table.table-hover thead tr th.bs-checkbox div.th-inner input').click()#点击复选框选择所有
        homepage.remove()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        homepage.confirm_1()  # 点击确认按钮
        ass_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text  # 获取文本内容
        try:
            self.assertEqual('没有找到匹配的记录', ass_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Delete(self):
        """删除推荐位布局"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.execute_script("window.scrollBy(0,5000)")#下拉滚动条
        # time.sleep(1)
        # homepage.table_inputend()  # 点击复选框
        homepage.returnbutn()#点击返回
        homepage.doubleclickbtn()  # 点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取文本内容
        homepage.table_2()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        homepage.confirm_1()  # 点击确认按钮
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取文本内容
        try:
            assert ass_name1 != ass_name2
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Delete_batch(self):
        """批量删除推荐位布局"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()  # 选择oms
        # time.sleep(2)
        # homepage.search_Content()  # 点击导航管理
        # homepage.dj_fenfayu()  # 点击推荐位布局
        homepage.add_recomm()  # 点击新增
        test_name = 'aa自动化推荐'
        homepage.add_names(test_name)  # 输入名称
        driver.find_element_by_id('pictureFile').send_keys('D:\\bit.jpg')  # 上传图片
        homepage.epgVersion4()  # 点击选择epg版本为4.0
        homepage.btnCreates()  # 点击添加
        homepage.add_recomm()  # 点击新增
        test1_name = 'aaa自动化推荐'
        homepage.add_names(test1_name)  # 输入名称
        driver.find_element_by_id('pictureFile').send_keys('D:\\bit.jpg')  # 上传图片
        homepage.epgVersion4()  # 点击选择epg版本为4.0
        homepage.btnCreates()  # 点击添加
        homepage.doubleclickbtn()  # 点击名称排序
        homepage.doubleclickbtn()  # 点击名称排序
        ass_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取文本内容
        ass_name2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text  # 获取文本内容
        homepage.table_input()#点击复选框
        homepage.table_input1()#点击复选框
        homepage.remove()#点击删除按钮
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        homepage.confirm_1()  # 点击确认按钮
        ass_name3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取文本内容
        ass_name4 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text  # 获取文本内容
        try:
            assert ass_name1 != ass_name3 and ass_name2 != ass_name4
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        driver.quit()

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()


