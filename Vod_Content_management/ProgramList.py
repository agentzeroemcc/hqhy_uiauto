# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface

#节目列表
program_test_name = '大面曹天'
program_cp_name = '优酷媒资'

class Program(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Audit_fail(self):
        """节目审核失败"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        homepage.search_Content()#点击内容管理
        homepage.collapseOnes()#节目列表按钮
        time.sleep(5)
        Select(self.driver.find_element_by_id('isCheck')).select_by_value('10')  # 审核下拉框并选择待审核
        time.sleep(3)
        old_name = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(审核失败测试)')#名称添加字段
        homepage.send_deter()#点击确定
        # 判断编辑操作是否成功
        try:
            self.assertEqual("保存成功!",VodSearch.get_ass_text(self))
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
            # homepage.get_windows_img()  # 调用基类截图方法
        homepage.determine()# 点击编辑确定
        namefail = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配编辑后的待审核名称
        homepage.table_input()# 点击对勾
        homepage.check_shenhe() # 点击审核
        Select(self.driver.find_element_by_name('checkStatus')).select_by_value('31')  # 点击审核失败
        homepage.check_program_form()#节目审核按钮
        try:
            assert VodSearch.get_ass_text(self) == '审核失败操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        homepage.button_1()#节目确定按钮
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
        """节目审核成功"""
        homepage = HomePage(self.driver)
        # homepage.search_Content()  # 点击内容管理
        # homepage.collapseOnes()  # 节目列表按钮
        Select(self.driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(3)
        old_name = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配初始待审核名称
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(审核成功测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断编辑操作是否成功
        try:
            assert VodSearch.get_ass_text(self) == '保存成功!'
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
        homepage.check_program_form()  # 节目审核按钮
        try:
            assert VodSearch.get_ass_text(self) == '审核成功操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        homepage.button_1()  # 节目确定按钮
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
        """节目上线"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        # homepage.collapseOnes()  # 节目列表按钮
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(3)
        Select(driver.find_element_by_id('isLine')).select_by_value('0')  # 审核下拉框并选择待上线状态
        time.sleep(3)
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始节目名称
        old_names = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  # 获取初始节目集名称
        pc_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[12]').text
        test_name = '节目['+old_name+']属节目集['+old_names+']状态是待上线或下线，故此节目无法上线！'
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(上线测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断是否操作编辑是否成功
        try:
            assert VodSearch.get_ass_text(self) == '保存成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        homepage.determine()  # 点击编辑确定
        up_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待上线名称
        homepage.table_2()#点击上线
        if test_name == '节目['+old_name+']属节目集['+old_names+']状态是待上线或下线，故此节目无法上线！':
            homepage.button_1()      #无法上线的确定按钮
            homepage.dj_jiemj()     #点击节目集列表
            homepage.searchBtn()#点击搜索
            homepage.add_names(old_names)
            homepage.searchDiv()  # 点击CP按钮
            homepage.searchDivInput(pc_name)  # 输入CP名称
            homepage.searchDivInput(Keys.ENTER)
            Select(driver.find_element_by_id('isLine')).select_by_value('2')  # 在线状态选择待上线
            time.sleep(1)
            homepage.searchByName()  # 点击搜索
            matching = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text  #没有找到匹配的记录
            def operation():
                homepage.dj_shangxx()#点击上线按钮
                try:
                    assert VodSearch.get_ass_text(self) == '上线操作成功!'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()  # 调用基类截图方法
                homepage.qs_anniu()
                homepage.collapseOnes()  # 节目列表按钮
                homepage.searchBtn()
                homepage.add_names(up_name)
                homepage.searchByName()
                homepage.dj_shangxx()#点击下线
                homepage.offline_program_from()  # 点击下线确定
                try:
                    assert VodSearch.get_ass_text(self) == '下线操作成功!'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()  # 调用基类截图方法
                homepage.button_1()
                homepage.dj_shangxx()
                try:
                    assert VodSearch.get_ass_text(self) == '上线操作成功!'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()  # 调用基类截图方法
                homepage.button_1()
                test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
                test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
                try:
                    assert test == '上线' and test1 == up_name
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()  # 调用基类截图方法
                # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[1]/i').click()      #点击编辑
                homepage.send_submit_btn()  # 点击编辑
                homepage.clear_edit()  # 删除‘上线测试’
                homepage.edit_name(old_name)  # 添加
                homepage.send_deter()  # 点击编辑确定
                homepage.determine()  # 点击确定
                homepage.searchReset()  # 重置
            if matching == '没有找到匹配的记录':
                Select(driver.find_element_by_id('isLine')).select_by_value('0')  # 在线状态选择待上线
                operation()
            else:
                operation()
        else:
            # homepage.table_2() # 点击上线按钮
            # 判断上线是否操作成功
            try:
                assert VodSearch.get_ass_text(self) == '上线操作成功!'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()  # 调用基类截图方法
            time.sleep(2)
            homepage.button_1()        # 确定上线成功
            homepage.add_names(up_name)# 通过xpath定位输入框，send_keys传值到输入框
            Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
            time.sleep(1)
            homepage.searchByName() # 点击搜索
            # homepage.get_windows_img()  # 调用基类截图方法
            homepage.send_submit_btn()      # 点击编辑
            homepage.clear_edit()  # 删除‘上线测试’
            homepage.edit_name(old_name)  # 添加
            homepage.send_deter()  # 点击编辑确定
            homepage.determine()  # 点击确定
            homepage.searchReset()  # 重置

    def test_Program_down(self):
        """节目下线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        # homepage.collapseOnes()  # 节目列表按钮
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核下拉框并选择审核成功
        time.sleep(3)
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 审核下拉框并选择上线状态
        time.sleep(5)
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配初始待下线名称
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(下线测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断是否操作编辑是否成功
        try:
            assert VodSearch.get_ass_text(self) == '保存成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        homepage.determine()  # 点击编辑确定
        new_down_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待下线名称
        homepage.table_2()  # 点击下线按钮
        homepage.offline_program_from()
        # 判断下线是否操作成功
        try:
            assert VodSearch.get_ass_text(self) == '下线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        homepage.button_1()  # 确定下线成功
        # homepage.searchBtn()  # 点击搜索按钮弹出搜索框
        homepage.add_names(new_down_name)  # 通过xpath定位输入框，send_keys传值到输入框
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(1)
        homepage.searchByName()  # 点击搜索
        text = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        text1 = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
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

    def test_online_interface(self):
        """节目上线接口测试"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        # homepage.search_Content()  # 点击内容管理
        # homepage.collapseOnes()  # 节目列表按钮
        # homepage.searchBtn()   #  点击搜索
        driver = self.driver
        homepage.seriesName(program_test_name)  #  输入节目集名称
        homepage.cp_dianji()  #点击cp下拉
        homepage.cp_shuru(program_cp_name)  #输入cp 内容
        homepage.cp_shuru(Keys.ENTER)  #
        homepage.searchByName()  #  点击搜索
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text  #  获取状态
        if state == '上线':
            Interface.Program_online(self)
            time.sleep(2)
        elif state == '下线':
            Interface.Program_downline(self)
            homepage.table_2()  #  点击上线按钮
            homepage.button_1()  # 点击确认
            Interface.Program_online(self)
            time.sleep(2)
        else:
            homepage.get_windows_img()

    def test_downline_interface(self):
        """节目下线接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text  # 获取状态
        if state == '上线':
            homepage.table_2()  #  点击下线按钮
            homepage.offline_program_from()  #  点击确定
            homepage.button_1()  #  点击确认
            Interface.Program_downline(self)
            time.sleep(2)
            homepage.table_2()  # 点击上线按钮
            homepage.button_1()  # 点击确认
        else:
            homepage.get_windows_img()

    def test_Delete_program(self):
        """删除节目"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # Select(driver.find_element_by_id('isLine')).select_by_value('2')  # 审核下拉框并选择下线状态
        # time.sleep(2)
        homepage.searchReset()  # 重置
        homepage.send_submit_btn()  # 点击编辑
        homepage.edit_name('(删除测试)')  # 名称添加字段
        homepage.send_deter()  # 点击确定
        # 判断是否操作编辑是否成功
        try:
            assert VodSearch.get_ass_text(self) == '保存成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        time.sleep(2)
        homepage.determine()  # 点击编辑确定
        del_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待删除名称
        homepage.table_input()
        homepage.sc_anniu()      #点击删除按钮
        try:
            assert VodSearch.get_ass_text(self) == '成功删除1个节目。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  # 删除‘确认’按钮
        homepage.add_names(del_name)
        homepage.searchByName()
        delete = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert delete == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置

    def test_Search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        initial_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取节目名称
        initials_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text#获取节目集名称
        # initials_code = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text#获取节目集code
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[12]').text  # 获取cp名称
        homepage.add_names(initial_name)
        homepage.seriesName(initials_name)
        homepage.cp_dianji()#点击CP按v钮
        homepage.cp_shuru(cp_name)      #输入CP名称
        homepage.cp_shuru(Keys.ENTER)
        homepage.searchByName()        # 点击搜索
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        test2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        test3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[12]').text
        try:
            assert test1 == initial_name and test2 == initials_name and test3 == cp_name
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
        old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text#获取节目名称
        initials_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[5]').text  # 获取节目集名称
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[12]').text  # 获取cp名称
        class_A = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[9]').text  # 一级分类
        class_B = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[10]').text  # 二级分类
        homepage.searchMore()        # 高级搜索
        homepage.gj_jmmc(old_name) # 输入节目名称
        homepage.gj_jmjmc(initials_name) # 输入节目集名称
        homepage.dj_cpkuang()  # 点击cp下拉框
        homepage.sr_cpneirong(cp_name)  # 获取cp名称
        homepage.sr_cpneirong(Keys.ENTER)  # 点击选定项
        homepage.fenlei_one(class_A)  # 输入一级分类
        homepage.fenlei_two(class_B)  # 输入二级分类
        homepage.dj_sous()  # 点击搜索
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        test2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text
        test3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[12]').text
        test4 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text
        test5 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text
        try:
            assert test1 == old_name and test2 == initials_name and test3 == cp_name and test4 == class_A and test5 == class_B
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        homepage.searchReset()
        text = self.driver.find_element_by_xpath('//*[@id="name"]').text
        text1 = self.driver.find_element_by_xpath('//*[@id="seriesName"]').text
        text2 = self.driver.find_element_by_xpath('//*[@id="seriesCode"]').text
        # Audit_status = self.driver.find_element_by_xpath('//*[@id="isCheck"]/option[1]').text   #  审核状态：全部
        # online_status = self.driver.find_element_by_xpath('//*[@id="isLine"]/option[1]').text   #  在线状态：全部
        try:
            assert text == '' and text1 == '' and text2 == ''
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
        time.sleep(4)
        Pending_audit = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text
        try:
            assert Pending_audit == '待审核'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')
        time.sleep(4)
        Audit_success = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[7]').text
        try:
            assert Audit_success == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isCheck')).select_by_value('31')
        time.sleep(4)
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
        """在线状态"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isLine')).select_by_value('0')# 在线状态下拉框并选择待上线
        time.sleep(3)
        On_line = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        try:
            assert On_line == '待上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_value('2')#选择下线
        time.sleep(3)
        Offline = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        try:
            assert Offline == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_value('1')#上线
        time.sleep(3)
        Go_online = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        try:
            assert Go_online == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 在线下拉框并选择全部
        time.sleep(3)

    def test_Batch_audit(self):
        """批量审核"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.search_Content()  # 点击内容管理
        # homepage.collapseOnes()  # 节目列表按钮
        # homepage.searchBtn()
        Select(driver.find_element_by_id('isCheck')).select_by_value('10')  # 审核下拉框并选择待审核
        time.sleep(3)
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        homepage.table_input()
        homepage.table_input1()
        homepage.check_shenhe()     # 点击审核
        Select(driver.find_element_by_name('checkStatus')).select_by_value('31')  # 点击审核失败
        time.sleep(3)
        homepage.check_program_form()        # 点击按钮审核
        try:
            assert VodSearch.get_ass_text(self) == '审核失败操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()       # 点击确定
        homepage.add_names(test)        #添加节目名称
        Select(driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        homepage.searchByName()         #点击搜索
        fail_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text
        try:
            assert fail_name == '审核失败'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()      #重置
        homepage.add_names(test1)  # 添加节目名称
        homepage.searchByName()  # 点击搜索
        fail_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text
        try:
            assert fail_name1 == '审核失败'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置


        #批量审核成功
        Select(driver.find_element_by_name('isCheck')).select_by_value('10')        #选择待审核
        time.sleep(3)
        Select(driver.find_element_by_name('isLine')).select_by_value('1')        #在线状态   上线
        # try:
        #     checkboxes = driver.find_elements_by_css_selector('input[type=checkbox]')
        #     for checkbox in checkboxes:
        #         checkbox.click()
        # except Exception as e:
        #     print(e)
        # time.sleep(2)
        time.sleep(3)
        test2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        test3 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        homepage.table_input()
        homepage.table_input1()
        homepage.check_shenhe()  # 点击审核
        Select(driver.find_element_by_name('checkStatus')).select_by_value('30')  # 点击审核成功
        time.sleep(2)
        homepage.check_program_form()  # 点击按钮审核
        try:
            assert VodSearch.get_ass_text(self) == '审核成功操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  # 点击确定
        homepage.add_names(test2)  # 添加节目名称
        Select(driver.find_element_by_id('isCheck')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        homepage.searchByName()  # 点击搜索
        success_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text
        try:
            assert success_name == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
        homepage.add_names(test3)  # 添加节目名称
        homepage.searchByName()  # 点击搜索
        success_name1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[7]').text
        try:
            assert success_name1 == '审核成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
    def test_Batch_up(self):
        """批量上线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isCheck')).select_by_value('30')  # 审核状态  审核成功
        time.sleep(3)
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 在线状态   下线
        time.sleep(3)
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        homepage.table_input()
        homepage.table_input1()
        homepage.online_1()#点击上线按钮
        homepage.online_program_form()#点击确定按钮
        try:
            assert VodSearch.get_ass_text(self) == '上线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()#点击确定按钮
        homepage.add_names(test)  # 添加节目名称
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 在线状态   上线
        homepage.searchByName()  # 点击搜索
        onlinename = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert onlinename == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
        homepage.add_names(test1)  # 添加节目名称
        homepage.searchByName()  # 点击搜索
        onlinename1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert onlinename1 == '上线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
    def test_Batch_offline(self):
        """批量下线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 在线状态   上线
        time.sleep(3)
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text#获取名称
        homepage.table_input()
        homepage.table_input1()
        homepage.offline()
        homepage.offline_program_from()
        try:
            assert VodSearch.get_ass_text(self) == '下线操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  # 点击确定按钮
        homepage.add_names(test)  # 添加节目名称
        Select(driver.find_element_by_id('isLine')).select_by_value('2')  # 在线状态   下线
        homepage.searchByName()  # 点击搜索
        offlinename = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert offlinename == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置
        homepage.add_names(test1)  # 添加节目名称
        homepage.searchByName()  # 点击搜索
        offlinename1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert offlinename1 == '下线'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置

    def test_Save_period(self):
        """播放地址列表"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.add_names('梦想世界')
        homepage.searchByName()
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a[2]/i').click()#点击节目列表按钮
        time.sleep(1)
        rand = random.randint(0,100)
        homepage.clear_ji()#删除集数
        homepage.add_ji(rand)#输入随机集数
        homepage.clear_number()#删除数字
        homepage.add_num(rand)#输入随机数字
        homepage.btnSaveVolumn()#点击保存按钮
        period = driver.find_element_by_xpath('/html/body/div[8]/div/div/div[2]/div').text
        try:
            assert period == '数据已经保存'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()#点击确定按钮

    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     :return:
    #     """
    #     cls.driver.quit()




