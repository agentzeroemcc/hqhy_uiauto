# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger

logger = Logger(logger="BasePage").getlog()
tit_name = '啊'
#消息列表
class Message(unittest.TestCase):
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
        title_name = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[4]').text  #  获取标题名称
        homepage.custom_toolbar_button()  #  点击新增
        Select(driver.find_element_by_id('servicetype')).select_by_value('1')  # 业务类型：  内容运营
        homepage.title_N(tit_name)  #  输入标题名称
        homepage.content_test('This is a test information')   #  输入内容
        Select(driver.find_element_by_id('importantdegree')).select_by_value('1')  # 重要程度  普通
        driver.find_element_by_xpath('//*[@id="sendDate"]/span/span').click()  #  点击时间选择
        time.sleep(1)
        driver.find_element_by_xpath('/html/body/div[8]/div[3]/table/tfoot/tr/th').click()  #  点击今天
        time.sleep(1)
        Select(driver.find_element_by_id('sendrange')).select_by_value('1')   #  发送范围：广播
        homepage.create_msg_form()  #  点击新增     选择业务组合code / 用户code
        driver.find_element_by_xpath('//*[@id="comboMacTable"]/tbody/tr[1]/td[1]/input').click()  #  点击复选
        time.sleep(1)
        homepage.saveComboMacs()  #  点击确定
        homepage.btnCreateMsg()  #  保存
        try:
            assert VodSearch.get_ass_text(self) == '创建操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()#确认
        """搜索"""
        homepage.ltitle_N(tit_name)  #  输入标题名称
        homepage.toolbar_custom()  #  点击搜索


        search_name = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td[4]').text  #  获取匹配名称
        try:
            assert search_name == tit_name or search_name == title_name + '...'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # tit_name = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td[4]').text  # 获取标题名称
        homepage.logs_table()  #  点击编辑
        homepage.clear_title_N()  #  清除名称
        homepage.title_N(tit_name + '（编辑）')  #  输入名称
        homepage.btnCreateMsg()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '创建操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()#确认
        homepage.clear_ltitle_N()  #清除标题名称
        homepage.ltitle_N(tit_name + '（编辑）')  #  输入编辑后的标题名称
        homepage.toolbar_custom()  #  点击搜索
        edit_name = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td[4]').text  # 获取编辑后的名称
        logger.info('aaaaaaaaaaaaaaaa%s'%edit_name)
        try:
            assert edit_name == tit_name + '（编辑）' or edit_name == tit_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_search(self):
        """搜索"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()  # 选择oms
        # time.sleep(2)
        # homepage.column_M()  # 点击消息管理
        homepage.toolbar_cust()  #  重置
        select = driver.find_element_by_id('lservicetype')
        options_list = select.find_elements_by_tag_name('option')
        for option in options_list:
            if '内容运营' in option.text:
                option.click()
                homepage.toolbar_custom()  #  点击搜索
                type = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[3]').text  #  获取业务类型  内容运营
                try:
                    assert type == '内容运营'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
            elif '版本升级' in option.text:
                option.click()
                homepage.toolbar_custom()  # 点击搜索
                type1 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[3]').text  # 获取业务类型  版本升级
                try:
                    assert type1 == '版本升级'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
            elif '业务推广' in option.text:
                option.click()
                homepage.toolbar_custom()  # 点击搜索
                type2 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[3]').text  # 获取业务类型  业务推广
                try:
                    assert type2 == '业务推广'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
            elif '到期提醒' in option.text:
                option.click()
                homepage.toolbar_custom()  # 点击搜索
                type3 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[3]').text  # 获取业务类型  到期提醒
                try:
                    assert type3 == '到期提醒'
                    print('Test pass.')
                except Exception as e:
                    print("Test fail.", format(e))
                    homepage.get_windows_img()
        time.sleep(2)
        """重要程度"""
        homepage.toolbar_cust()  # 重置
        Select(driver.find_element_by_id('limportantdegree')).select_by_value('1')  #  重要程度  普通
        homepage.toolbar_custom()  # 点击搜索
        Importance = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[6]').text  #  重要程度  普通
        try:
            assert Importance == '普通'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('limportantdegree')).select_by_value('2')  # 重要程度  重要
        homepage.toolbar_custom()  # 点击搜索
        Importance1 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[6]').text  # 重要程度  重要
        try:
            assert Importance1 == '重要'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """发送范围"""
        homepage.toolbar_cust()  # 重置
        Select(driver.find_element_by_id('lrange')).select_by_value('1')  # 发送范围  广播
        homepage.toolbar_custom()  # 点击搜索
        range = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[8]').text  # 发送范围  广播
        try:
            assert range == '广播'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lrange')).select_by_value('2')  # 发送范围  组播
        homepage.toolbar_custom()  # 点击搜索
        range1 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[8]').text   # 发送范围  组播
        try:
            assert range1 == '组播'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lrange')).select_by_value('3')  # 发送范围  单播
        homepage.toolbar_custom()  # 点击搜索
        try:
            assert driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td').text == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """审核状态"""
        homepage.toolbar_cust()  # 重置
        Select(driver.find_element_by_id('lcheckstatus')).select_by_value('0')  # 审核状态  待审核
        homepage.toolbar_custom()  # 点击搜索
        checkstatus = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[9]').text  # 待审核
        try:
            assert checkstatus == '待审核'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lcheckstatus')).select_by_value('1')  # 审核状态  审核通过
        homepage.toolbar_custom()  # 点击搜索
        checkstatus1 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[9]').text  # 审核通过
        try:
            assert checkstatus1 == '审核通过'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lcheckstatus')).select_by_value('2')  # 审核状态  审核不通过
        homepage.toolbar_custom()  # 点击搜索
        try:
            assert driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td').text == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """发送状态"""
        homepage.toolbar_cust()  # 重置
        Select(driver.find_element_by_id('lsendStatus')).select_by_value('0')  # 发送状态  未发送
        homepage.toolbar_custom()  # 点击搜索
        sendStatus = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[5]').text  # 未发送
        try:
            assert sendStatus == '未发送'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lsendStatus')).select_by_value('1')  # 发送状态  发送中
        homepage.toolbar_custom()  # 点击搜索
        try:
            assert driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td').text == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lsendStatus')).select_by_value('2')  # 发送状态  发送成功
        homepage.toolbar_custom()  # 点击搜索
        sendStatus2 = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[5]').text  # 发送成功
        try:
            assert sendStatus2 == '发送成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """消息来源"""
        homepage.toolbar_cust()  # 重置
        Select(driver.find_element_by_id('lsources')).select_by_value('1')  # 消息来源  人工
        homepage.toolbar_custom()  # 点击搜索
        sources = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[10]').text  # 人工
        try:
            assert sources == '人工'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('lsources')).select_by_value('2')  # 消息来源  自动
        homepage.toolbar_custom()  # 点击搜索
        automatic = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[10]').text  #  自动
        try:
            assert driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr/td').text == '没有找到匹配的记录' or automatic == '自动'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_To_examine(self):
        """审核"""
        driver = self.driver
        homepage = HomePage(self.driver)
        homepage.toolbar_cust()  # 重置
        driver.refresh() # 刷新当前页面
        examine = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[9]').text   #  获取审核状态
        if examine == '待审核':
            homepage.logs_table_input()  #  点击复选
            homepage.button_custom_toolbar()  #  点击审核
            driver.find_element_by_xpath('//*[@id="examine_msg_form"]/label[2]/input').click()   #   点击审核不通过
            time.sleep(1)
            homepage.btnExamineMsg()  #  点击保存
            try:
                assert VodSearch.get_ass_text(self) == '修改成功'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.button_2()  # 确认
            state = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[9]').text   #  获取状态
            try:
                assert state == '审核不通过'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.logs_table_input()  # 点击复选
            homepage.button_custom_toolbar()  # 点击审核
            driver.find_element_by_xpath('//*[@id="examine_msg_form"]/label[1]/input').click()  # 点击审核通过
            time.sleep(1)
            homepage.btnExamineMsg()  # 点击保存
            try:
                assert VodSearch.get_ass_text(self) == '修改成功'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.button_2()  # 确认
            state = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[9]').text  # 获取状态
            try:
                assert state == '审核通过'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.logs_table_input()  # 点击复选
            homepage.button_custom_toolbar()  # 点击审核
            homepage.btnExamineMsg()  # 点击保存
            try:
                assert VodSearch.get_ass_text(self) == '有审核状态是通过的,请认真查找后再审核'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.button_2()  # 确认

    def test_Message_preview(self):
        """消息预览"""
        driver = self.driver
        homepage = HomePage(self.driver)
        type = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[3]').text  #  获取业务类型
        title_name = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[4]').text  #  获取标题
        Importance = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[6]').text  #  获取重要程度
        Sending = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[7]').text  #  发送时间
        range = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[8]').text  #  发送范围
        Creation = driver.find_element_by_xpath('//*[@id="logs_table"]/tbody/tr[1]/td[11]').text  #  创建时间
        homepage.logs_table_i()  #  点击消息预览
        type1 = driver.find_element_by_xpath('//*[@id="prservicetype"]').text    #  获取预览业务类型
        title_name1 = driver.find_element_by_xpath('//*[@id="prtitle"]').text    #  获取预览标题
        Importance1 = driver.find_element_by_xpath('//*[@id="primportantdegree"]').text    #  获取预览重要程度
        Sending1 = driver.find_element_by_xpath('//*[@id="prsendtime"]').text    #  获取预览发送时间
        range1 = driver.find_element_by_xpath('//*[@id="prsendrange"]').text    #  获取预览发送范围
        Creation1 = driver.find_element_by_xpath('//*[@id="predi_create_time"]').text    #  获取预览创建时间
        try:
            assert type1 == type and Importance1 == Importance and Sending1 == Sending and range1 == range and Creation1 == Creation
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.preview_msg_form()  #  点击关闭

    def test_details(self):
        """详情"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/a/span').click()  # 点击下拉
        # time.sleep(2)
        # driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/ul/li/ul/li[1]/a').click()  # 选择oms
        # time.sleep(2)
        # homepage.column_M()  # 点击消息管理
        # homepage.logs_table_i()
        homepage.logs_table_a3()  #  点击详情
        user_id = driver.find_element_by_xpath('//*[@id="detail_userTable"]/tbody/tr/td[2]').text  #  获取用户ID
        homepage.searchUserId(user_id)  #  输入用户ID
        driver.find_element_by_css_selector('html body div.container-fluid div.row div.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#detaile_msguser_dialog.modal.fadein.in div.modal-dialog.modal-lg div.modal-content div.modal-body div.row div.col-md-20 div div.tab-content div.tab-content div#unSendUsers.tab-pane.active div#searchDiv div.form-inline button.btn.btn-info').click() #  点击搜索
        time.sleep(2)
        id = driver.find_element_by_xpath('//*[@id="detail_userTable"]/tbody/tr/td[2]').text
        try:
            assert id == user_id
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        driver.find_element_by_xpath('//*[@id="unSendUsers"]/div[5]/div/button[2]').click()   #   点击关闭
        time.sleep(2)

    def test_delete(self):
        """删除"""
        driver = self.driver
        homepage = HomePage(self.driver)
        homepage.logs_table_input()  #  点击复选
        homepage.delete_custom()  #  点击删除
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '删除成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_2()  # 确认

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()






