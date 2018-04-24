# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from framework.Interface_test import Interface
from framework.logger import Logger


#节目集列表
test_name = '大面曹天'
cp_name = '优酷媒资'
logger = Logger(logger="BrowserEngine").getlog()

class VodSearch(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Sign_in(self):
        """登录
        :return:
        """
        homepage = HomePage(self.driver)
        homepage.type_search('admin')  # 调用页面对象中的方法
        homepage.type_search2('1234')
        homepage.send_fm1()#登录

    def get_ass_text(self):
        """获取弹出框断言"""
        guttv_dyn = self.driver.find_element_by_xpath('//*[@id="guttv_dyn_alert"]').text
        return guttv_dyn

    def test_Audit_fail(self):
        """节目集审核失败"""
        homepage = HomePage(self.driver)
        homepage.search_Content()#点击内容管理
        Select(self.driver.find_element_by_id('isCheck')).select_by_value('10')  # 审核下拉框并选择待审核
        time.sleep(2)
        old_name = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(审核失败测试)')#名称添加字段
        homepage.send_deter()#点击确定
        # 判断编辑操作是否成功
        try:
            self.assertEqual("保存成功!",self.get_ass_text())
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.qs_anniu()# 点击编辑确定
        namefail = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配编辑后的待审核名称
        homepage.table_input()# 点击对勾
        homepage.check_shenhe() # 点击审核
        Select(self.driver.find_element_by_name('checkStatus')).select_by_value('31')  # 点击审核失败
        homepage.check_series_form()#节目审核按钮
        try:
            assert self.get_ass_text() == '审核操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        homepage.qs_anniu()#节目确定按钮
        homepage.searchBtn()# 点击搜索按钮弹出搜索框
        homepage.add_names(namefail)#输入搜索名称
        Select(self.driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        homepage.searchByName()  # 点击搜索开始搜索
        text = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text
        try:
            assert text == namefail and text1 == '审核失败'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.send_submit_btn() # 点击编辑
        homepage.clear_edit() # 删除‘审核测试’
        homepage.edit_name(old_name)# 添加
        homepage.send_deter() # 点击编辑确定
        homepage.determine()# 点击确定
        homepage.searchReset()#重置
    def test_Audit_success(self):
        """节目集审核成功"""
        homepage = HomePage(self.driver)
        # homepage.search_Content()  # 点击内容管理
        Select(self.driver.find_element_by_id('isCheck')).select_by_value('10')  # 审核下拉框并选择待审核
        time.sleep(2)
        old_name = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配初始待审核名称
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(审核成功测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断编辑操作是否成功
        try:
            assert self.get_ass_text() == '保存成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        homepage.determine()  # 点击编辑确定
        nameSuccess = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配编辑后的待审核名称
        homepage.table_input()  # 点击对勾
        homepage.check_shenhe()  # 点击审核
        Select(self.driver.find_element_by_name('checkStatus')).select_by_value('30')  # 点击审核成功
        homepage.check_series_form()  # 节目审核按钮
        try:
            assert self.get_ass_text() == '审核操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        homepage.qs_anniu()  # 节目确定按钮
        # homepage.searchBtn()  # 点击搜索按钮弹出搜索框
        homepage.add_names(nameSuccess)  # 输入搜索名称
        Select(self.driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        homepage.searchByName()  # 点击搜索开始搜索
        text = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text
        try:
            assert text == nameSuccess and text1 == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.send_submit_btn()  # 点击编辑
        homepage.clear_edit()  # 删除‘审核测试’
        homepage.edit_name(old_name)  # 添加
        homepage.send_deter()  # 点击编辑确定
        homepage.determine()  # 点击确定
        homepage.searchReset()  # 重置

    def test_Program_up(self):
        """节目集上线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        # homepage.searchBtn()  # 点击搜索按钮弹出搜索框
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(1)
        Select(driver.find_element_by_id('isLine')).select_by_value('2')  # 在线状态下拉框并选择下线状态
        time.sleep(3)
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        time.sleep(2)
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(上线测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断是否操作编辑是否成功
        try:
            assert self.get_ass_text() == '保存成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        homepage.determine()  # 点击编辑确定
        up_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待上线名称
        homepage.table_2() # 点击上线按钮
        # 判断上线是否操作成功
        try:
            assert self.get_ass_text() == '上线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        homepage.qs_anniu()        # 确定上线成功
        # homepage.searchBtn()  # 点击搜索按钮弹出搜索框
        homepage.add_names(up_name)# 通过xpath定位输入框，send_keys传值到输入框
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 在线状态下拉框并选择全部
        time.sleep(1)
        homepage.searchByName() # 点击搜索
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert text == up_name and text1 == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.send_submit_btn()      # 点击编辑
        homepage.clear_edit()  # 删除‘上线测试’
        homepage.edit_name(old_name)  # 添加
        homepage.send_deter()  # 点击编辑确定
        homepage.determine()  # 点击确定
        homepage.searchReset()  # 重置

    def test_Downline_interface(self):
        """下线接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击内容管理
        homepage.searchBtn()  # 点击搜索按钮弹出搜索框
        homepage.add_names(test_name)  # 通过xpath定位输入框，send_keys传值到输入框

        # driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/button/span[2]/span').click()  #  点击CP下拉
        homepage.search_span_button()  #  点击CP下拉
        homepage.searchDiv_lable_input(cp_name)
        homepage.searchDiv_lable_input(Keys.ENTER)
        homepage.searchByName()  # 点击搜索
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text  #  获取在线状态
        if state == '上线':
            homepage.sleep(2)
            Interface.vod_api_browser(self)
            homepage.dj_shangxx()  #  点击下线按钮
            homepage.offline_series_form()  #  点击确定
            try:
                assert self.get_ass_text() == '下线操作成功!'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.qs_anniu()  # 确定下线成功
            down_state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text  #  获取下线状态
            if down_state == '下线':
                homepage.sleep(80)
                Interface.vod_api_downline(self)
            else:
                homepage.get_windows_img()
        elif state == '下线':
            homepage.sleep(2)
            Interface.vod_api_downline(self)
            homepage.dj_shangxx()  #  点击上线
            try:
                assert self.get_ass_text() == '上线操作成功!'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.qs_anniu()  # 确定上线成功
            up_state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
            if up_state == '上线':
                homepage.dj_chanpguanl()  #  点击产品管理
                homepage.searchBtn()  #  点击搜索
                homepage.add_names(test_name)  #  添加名称
                homepage.searchByName()  #  点击搜索
                homepage.glyphicon_edit()  #  点击b编辑
                homepage.chooseProduct()  #  点击选择产品
                homepage.cp_mingchen(test_name)  #  输入产品名称
                homepage.sr_chanp()  #点击cp
                homepage.sr_cp_mingchen(cp_name)  #  输入cp名称
                homepage.sr_cp_mingchen(Keys.ENTER)  #   回车
                homepage.dj_duig()  #  点击复选
                homepage.prd_add()  #  右添加
                homepage.btnSaves()  #  点击确认
                homepage.edit_package_form()  #  点击保存
                homepage.confirm_1()  #  点击确认
                homepage.sleep(80)
                Interface.vod_api_browser(self)
                homepage.search_Content()  # 点击内容管理
                homepage.searchBtn()  # 点击搜索按钮弹出搜索框
            else:
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def test_Online_interface(self):
        """上线接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text  # 获取在线状态
        if state == '下线':
            time.sleep(2)
            Interface.vod_api_downline(self)
            homepage.dj_shangxx()  #  点击上线
            try:
                assert self.get_ass_text() == '上线操作成功!'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.qs_anniu()  # 确定上线成功
            up_state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
            if up_state == '上线':
                homepage.dj_chanpguanl()  #  点击产品管理
                homepage.searchBtn()  #  点击搜索
                homepage.add_names(test_name)  #  添加名称
                homepage.searchByName()  #  点击搜索
                homepage.glyphicon_edit()  #  点击b编辑
                homepage.chooseProduct()  #  点击选择产品
                homepage.cp_mingchen(test_name)  #  输入产品名称
                homepage.sr_chanp()  #点击cp
                homepage.sr_cp_mingchen(cp_name)  #  输入cp名称
                homepage.sr_cp_mingchen(Keys.ENTER)  #   回车
                homepage.dj_duig()  #  点击复选
                homepage.prd_add()  #  右添加
                homepage.btnSaves()  #  点击确认
                homepage.edit_package_form()  #  点击保存
                homepage.confirm_1()  #  点击确认
                time.sleep(80)
                Interface.vod_api_browser(self)
                homepage.search_Content()  # 点击内容管理
                homepage.searchBtn()  # 点击搜索按钮弹出搜索框
            else:
                homepage.get_windows_img()

    def test_Program_down(self):
        """节目集下线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.searchReset()  #  重置
        # homepage.search_Content()  # 点击内容管理
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(1)
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 审核下拉框并选择上线状态
        time.sleep(2)
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配初始待下线名称
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(下线测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断是否操作编辑是否成功
        try:
            assert self.get_ass_text() == '保存成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        homepage.determine()  # 点击编辑确定
        new_down_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待下线名称
        homepage.table_2()  # 点击下线按钮
        homepage.offline_series_form()
        # 判断下线是否操作成功
        try:
            assert self.get_ass_text() == '下线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        homepage.qs_anniu()  # 确定下线成功
        # homepage.searchBtn()  # 点击搜索按钮弹出搜索框
        homepage.add_names(new_down_name)  # 通过xpath定位输入框，send_keys传值到输入框
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(1)
        homepage.searchByName()  # 点击搜索
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert text == new_down_name and text1 == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.send_submit_btn()  # 点击编辑
        homepage.clear_edit()  # 删除‘下线测试’
        homepage.edit_name(old_name)  # 添加
        homepage.send_deter()  # 点击编辑确定
        homepage.determine()  # 点击确定
        homepage.searchReset()  # 重置

    def test_Search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.search_Content()  # 点击内容管理
        initial_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取初始名称
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # 获取cp名称
        homepage.searchBtn()  #  点击搜索
        homepage.add_names(initial_name)
        homepage.searchDiv()#点击CP按钮
        homepage.searchDivInput(cp_name)      #输入CP名称
        homepage.searchDivInput(Keys.ENTER)
        homepage.searchByName()        # 点击搜索
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        test2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert test1 == initial_name and test2 == cp_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()

    def test_High_search(self):
        """高级搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('//*[@id="searchBtn"]').click()#点击搜索
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # 获取cp名称
        class_A = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[9]').text  # 一级分类
        class_B = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[10]').text  # 二级分类
        homepage.searchMore()        # 高级搜索
        homepage.seriesName(old_name) # 输入节目集名称
        homepage.cp_xlakuang()  # 点击cp下拉框
        homepage.hq_cp_mc(cp_name)  # 获取cp名称
        homepage.hq_cp_mc(Keys.ENTER)  # 回车确定
        homepage.fenlei_one(class_A)  # 输入一级分类
        homepage.fenlei_two(class_B)  # 输入二级分类
        homepage.dj_sous()  # 点击搜索
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        text3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text
        text4 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text
        try:
            assert text1 == old_name and text2 == cp_name and text3 == class_A and text4 == class_B
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        # homepage.get_windows_img()  # 调用基类截图方法

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        homepage.searchReset()
        test = self.driver.find_element_by_xpath('//*[@id="name"]').text
        test1 = self.driver.find_element_by_xpath('//*[@id="searchDiv"]/div/label[3]/div/button/span[1]').text
        # Audit_status = self.driver.find_element_by_xpath('//*[@id="isCheck"]/option[1]').text  # 审核状态：全部
        # online_status = self.driver.find_element_by_xpath('//*[@id="isLine"]/option[1]').text  # 在线状态：全部

        try:
            assert test == '' and test1 == '全部'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
    # def test_Refresh(self):
    #     """刷新"""
    #     homepage = HomePage(self.driver)
    #     homepage.dj_shuaxin()
    #     # homepage.get_windows_img()

    def test_Audit_status(self):
        """审核状态"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isCheck')).select_by_value('10')# 审核下拉框并选择待审核
        time.sleep(2)
        Pending_audit = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text
        try:
            assert Pending_audit == '待审核'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')
        time.sleep(2)
        Audit_success = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text
        try:
            assert Audit_success == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isCheck')).select_by_value('31')
        time.sleep(2)
        Audit_failure = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text
        try:
            assert Audit_failure == '审核失败'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(2)

    def test_Online_status(self):
        u"""在线状态"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isLine')).select_by_value('0')# 在线状态下拉框并选择待上线
        time.sleep(2)
        On_line = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        try:
            assert On_line == '待上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_value('2')#选择下线
        time.sleep(2)
        Offline = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        try:
            assert Offline == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_value('1')#上线
        time.sleep(2)
        Go_online = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        try:
            assert Go_online == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(2)

    def test_Batch_audit(self):
        """批量审核失败"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        Select(driver.find_element_by_id('isCheck')).select_by_value('10')  # 审核下拉框并选择待审核
        time.sleep(2)
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        homepage.table_input()
        homepage.table_input1()
        homepage.check_shenhe()     # 点击审核
        Select(driver.find_element_by_name('checkStatus')).select_by_value('31')  # 点击审核失败
        time.sleep(2)
        homepage.check_series_form()        # 点击按钮审核
        try:
            assert self.get_ass_text() == '审核操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()       # 点击确定
        # homepage.searchBtn()        #点击搜索
        homepage.add_names(text)        #添加搜索内容
        Select(driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        homepage.searchByName()     #点击搜索
        btn = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text  #获取审核状态
        try:
            assert btn == '审核失败'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()      #重置
        homepage.add_names(text1)  # 添加搜索内容
        homepage.searchByName()  # 点击搜索
        btn1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text  # 获取审核状态
        try:
            assert btn1 == '审核失败'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置

    def test_Batch_success(self):
        """批量审核成功"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isCheck')).select_by_value('10')  # 审核下拉框并选择待审核
        time.sleep(2)
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        # name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        time.sleep(2)
        homepage.table_input()
        homepage.table_input1()
        # try:
        #     checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
        #     for checkbox in checkboxes:
        #         checkbox.click()
        # except Exception as e:
        #     print(e)
        # time.sleep(2)
        homepage.check_shenhe()  # 点击审核
        Select(driver.find_element_by_name('checkStatus')).select_by_value('30')  # 点击审核成功
        time.sleep(2)
        homepage.check_series_form()  # 点击按钮审核
        try:
            assert self.get_ass_text() == '审核操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()  # 点击确定
        homepage.add_names(name)
        Select(driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        homepage.searchByName()  # 点击搜索
        btn2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text  # 获取审核状态
        try:
            assert btn2 == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
        homepage.add_names(name1)  # 添加搜索内容
        homepage.searchByName()  # 点击搜索
        btn3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text  # 获取审核状态
        try:
            assert btn3 == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置

    def test_Batch_up(self):
        """批量上线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(1)
        Select(driver.find_element_by_id('isLine')).select_by_value('2')  # 审核下拉框并选择下线状态
        time.sleep(1)
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        name_cp = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text #cp名称
        name_cp1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text #cp名称
        homepage.table_input()
        homepage.table_input1()
        # try:
        #     inputs = driver.find_elements_by_tag_name('input')
        #     for input in inputs:
        #         if input.get_attribute('type') == 'checkbox':
        #             input.click()
        # except Exception as e:
        #     print(e)
        # time.sleep(2)
        homepage.online_1()#点击上线按钮
        homepage.qd_anniu()#点击确定按钮
        try:
            assert self.get_ass_text() == '上线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()#点击确定按钮
        homepage.add_names(test)
        homepage.search_span_button()  # 点击CP下拉
        homepage.searchDiv_lable_input(name_cp)
        homepage.searchDiv_lable_input(Keys.ENTER)
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')
        homepage.searchByName()     #搜索
        up = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert up == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
        homepage.add_names(test1)
        homepage.search_span_button()  # 点击CP下拉
        homepage.searchDiv_lable_input(name_cp1)
        homepage.searchDiv_lable_input(Keys.ENTER)
        homepage.searchByName()  # 搜索
        ups = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert ups == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
    def test_Batch_offline(self):
        """批量下线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(1)
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 审核下拉框并选择上线状态
        time.sleep(1)
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        name_cp = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  # cp名称
        name_cp1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text  # cp名称
        homepage.table_input()
        homepage.table_input1()
        # try:
        #     inputs = driver.find_elements_by_tag_name('input')
        #     for input in inputs:
        #         if input.get_attribute('type') == 'checkbox':
        #             input.click()
        # except Exception as e:
        #     print(e)
        # time.sleep(2)
        homepage.offline()      #点击下线
        homepage.offline_series_form()      # 点击下线原因‘确定’
        try:
            assert self.get_ass_text() == '下线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()  # 点击确定按钮
        homepage.add_names(test)
        homepage.search_span_button()  # 点击CP下拉
        homepage.searchDiv_lable_input(name_cp)
        homepage.searchDiv_lable_input(Keys.ENTER)
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')
        homepage.searchByName()  # 搜索
        up = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert up == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
        homepage.add_names(test1)
        homepage.search_span_button()  # 点击CP下拉
        homepage.searchDiv_lable_input(name_cp1)
        homepage.searchDiv_lable_input(Keys.ENTER)
        homepage.searchByName()  # 搜索
        ups = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert ups == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置

    def test_Save_period(self):
        """保存集/期数"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        # homepage.searchBtn()  # 点击搜索
        homepage.add_names('梦想世界')
        homepage.searchByName()
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[2]/i').click()#点击节目列表按钮
        time.sleep(1)
        rand = random.randint(0,100)
        # rand1 = random.randint(0,100)
        homepage.clear_ji()#删除集数
        homepage.add_ji(rand)#输入随机集数
        text = driver.find_element_by_xpath('//*[@id="volumn_2100020062943265254092760"]').get_attribute('value')
        # homepage.clear_number()#删除数字
        # homepage.add_num(rand1)#输入随机数字
        # text1 = driver.find_element_by_xpath('//*[@id="stage_2100020062943265254092760"]').get_attribute('value')
        homepage.btnSaveVolumn()#点击保存按钮
        try:
            assert self.get_ass_text() == '数据已经保存'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        driver.find_element_by_xpath('/html/body/div[9]/div/div/div[3]/button').click()#点击确定按钮
        driver.find_element_by_xpath('//*[@id="program_list_dialog"]/div/div/div[1]/button/span').click() #点击X
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[2]/i').click()  # 点击节目列表按钮
        time.sleep(3)
        number = driver.find_element_by_xpath('//*[@id="volumn_2100020062943265254092760"]').get_attribute('value')
        # number1 = driver.find_element_by_xpath('//*[@id="stage_2100020062943265254092760"]').get_attribute('value')
        try:
            assert number == text
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        # homepage.btnSaveVolumn()  #  保存按钮
        homepage.program_list_dialog()  #  关闭当前页面
        homepage.searchReset()  # 重置

    def test_export(self):
        """导出"""
        homepage = HomePage(self.driver)
        driver = self.driver
        export_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  #  获取导出名称
        homepage.table_input()  #  点击复选
        homepage.exportBtn()  #  导出
        try:
            assert self.get_ass_text() == '创建成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()  #  确认
        homepage.jc_peizhi()  #  基础配置
        homepage.collapseThree()  #  任务查询
        query_name = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[3]').text  #  获取查询名称
        try:
            assert query_name == '节目集：' + export_name + '...详单导出'
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

