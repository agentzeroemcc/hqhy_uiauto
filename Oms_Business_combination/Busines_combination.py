# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from Oms_Navigation_management.Global_navigation import Global
from framework.logger import Logger
from framework.Interface_test import Interface

logger = Logger(logger="BrowserEngine").getlog()
com_name = 'AA业务组合测试'
#业务组合
class Business_com(unittest.TestCase,Interface):
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
        homepage.busines_com()  #  点击业务组合
        homepage.add_recomm()  #   点击新增
        homepage.add_names(com_name)  #  输入名称
        homepage.comboKey('AZ')  #  输入标识
        Select(driver.find_element_by_id('agentvendorcode')).select_by_value('1100101022393220106740001')  #  选择渠道商  福建联通
        time.sleep(1)
        Select(driver.find_element_by_id('authMode')).select_by_value('1')  #  选择注册模式  全动态
        time.sleep(1)
        Select(driver.find_element_by_id('imStatus')).select_by_value('1')  #  选择消息服务  开通
        time.sleep(1)
        homepage.btnCreates()  #  点击添加

    def test_search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchinputcom(com_name)  #  输入搜索内容
        time.sleep(2)
        test_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div[2]/table/tbody/tr/td[4]').text   #  获取序号1名称
        logger.info("%s"%test_name)
        try:
            assert test_name == com_name
            logger.info('Test pass.')
        except Exception as e:
            logger.info("Test fail.", format(e))
            homepage.get_windows_img()
        # homepage.clear_searchinputcom()  #清空
        # time.sleep(1)

    def test_Enable(self):
        """启用"""
        homepage = HomePage(self.driver)
        homepage.table_Input()  #  点击对勾
        homepage.startup()  #  点击启用
        try:
            assert VodSearch.get_ass_text(self) == '更改成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  点击确认
        state = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[11]').text  #  获取状态
        try:
            self.assertEqual('启用',state)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_disable(self):
        """停用"""
        homepage = HomePage(self.driver)
        homepage.table_Input()  # 点击对勾
        homepage.shutdown()  # 点击停用
        try:
            assert VodSearch.get_ass_text(self) == '更改成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  点击确认
        state = self.driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[11]').text  # 获取状态
        try:
            self.assertEqual('停用', state)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_edit(self):
        """编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.business_edit()  #  点击编辑
        homepage.add_names('（编辑）')  #  添加编辑
        homepage.btnSaves()  #  点击更新
        homepage.searchinputcom(com_name)  #  输入搜索
        bj_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        try:
            assert bj_name == com_name + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Bound_service(self):
        """绑定业务分组"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.bound_ser()  #  点击绑定业务分组
        unbind = driver.find_element_by_xpath('//*[@id="unbindTable"]/tbody/tr/td[2]').text
        homepage.unbindTable()  #  点击复选框
        homepage.svcgrpBind()  #  向右添加
        bind = driver.find_element_by_xpath('//*[@id="bindTable"]/tbody/tr/td[2]').text
        try:
            self.assertEqual(unbind, bind)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        homepage.bindSvcgrp()  #  点击确认
        alert = driver.switch_to_alert()
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '绑定数据成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  点击确认
        group = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[10]').text #  获取业务分组
        try:
            assert group == unbind
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Bound_Navigation(self):
        """绑定导航"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.navigation_bind()  #  点击绑定导航
        homepage.navigationTable()  #  点击复选框
        homepage.btnNavigationBind()  #  点击绑定
        try:
            assert VodSearch.get_ass_text(self) == '绑定成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  #  确认
        nav_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[9]').text
        logger.info('aaa%s'%nav_name)
        try:
            self.assertEqual('  福建联通', nav_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())

    def test_Navigation_details(self):
        """导航详情"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.busines_com()  # 点击业务组合
        homepage.navigation_details()  #  点击导航详情
        Select(driver.find_element_by_id('navList')).select_by_value('1100070023874046224810008')  # 选择导航项  推荐
        time.sleep(1)
        recommend_name = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr[1]/td[4]').text   #  获取第一行名称
        homepage.recommend_names(recommend_name)  #   输入推荐项名称
        homepage.recommend_names(Keys.ENTER)  #   回车搜索
        search_name = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td[4]').text
        try:
            self.assertEqual(recommend_name, search_name)
        except AssertionError as e:
            print("Test fail.", format(e), homepage.get_windows_img())
        """定制"""
        homepage.recommendListTable()  #  点击定制按钮
        Select(driver.find_element_by_id('serviceType')).select_by_value('GAME')  # 选择业务类型  游戏
        time.sleep(1)
        input_name = '游戏'
        driver.find_element_by_xpath('//*[@id="recommendname"]').clear()  #  删除名称
        driver.find_element_by_xpath('//*[@id="recommendname"]').send_keys(input_name)  #  输入名称
        time.sleep(1)
        homepage.btnComboRecommendSave()  #  点击保存
        try:
            assert VodSearch.get_ass_text(self) == '更新成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()  #  点击确认
        homepage.combo_nav_list()  # 点击重置
        homepage.recommend_names(input_name)  # 输入推荐项名称
        homepage.recommend_names(Keys.ENTER)  # 回车搜索
        test_name = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td[4]').text  #获取名称
        business = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td[9]').text  #  获取业务类型
        type = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td[6]').text  #  获取类型
        try:
            assert test_name == input_name and business == input_name and type == '定制'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """启用/停用"""
        def state_type():
            homepage.recommendListTable1()  #  点击启用/停用
            try:
                assert VodSearch.get_ass_text(self) == '更新状态成功'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.qs_anniu()  #  确认
        state_type()
        state_name = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td[5]').text
        try:
            assert state_name == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        state_type()
        state_name1 = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td[5]').text
        try:
            assert state_name1 == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """删除定制"""
        homepage.recommendListTable2()  #  dj删除定制
        try:
            assert VodSearch.get_ass_text(self) == '删除成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.qs_anniu()  #  确认
        matching = driver.find_element_by_xpath('//*[@id="recommendListTable"]/tbody/tr/td').text  #获取匹配记录
        try:
            assert matching == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """重置"""
        homepage.combo_nav_list()  #  d点击重置
        tj_name = driver.find_element_by_xpath('//*[@id="name_n"]').text
        try:
            assert tj_name == ''
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.combo_nav_list_button()  #  点击关闭

    def test_delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        test_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text  #  AA业务组合测试（编辑）
        homepage.bound_ser()  # 点击绑定业务分组
        homepage.bindTable()  #  点击复选框
        homepage.svcgrpUnbind()  #  向左点击
        homepage.bindSvcgrp()   #  确认
        alert = driver.switch_to_alert()
        alert.accept()
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '绑定数据成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  # 点击确认
        homepage.Remove_navigation()  #  解除导航
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '解除绑定成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  # 点击确认
        homepage.navigation_details()  #  点击删除
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '删除成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()  # 点击确认
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert new_name == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_fjlt_interface(self):
        """福建联通绑定业务分组接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.clear_searchinputcom()  #  清空搜索
        homepage.searchinputcom('福建联通')  # 输入搜索内容
        time.sleep(2)
        inter = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[10]').text   #   获取业务分组名称
        if inter == 'KS自动化接口':
            Interface.Bound_recommend(self)   #  调用KS自动化接口
            homepage.unbound_edit1()  #  点击绑定业务分组
            homepage.bindTable()  #  点击已绑定业务分组第一个复选框
            homepage.svcgrpUnbind()  #  点击向左箭头
            driver.find_element_by_xpath('//*[@id="unbindTable"]/tbody/tr[1]/td[1]/input').click()  #  点击可选业务分组第一个复选框
            time.sleep(1)
            homepage.svcgrpBind()  #  点击向右箭头
            homepage.bindSvcgrp()  #  点击确认
            driver.switch_to_alert().accept()
            homepage.button_1() #   点击确认
            Interface.FJLT_Bound_recommend(self)   #调用福建联通点播业务分组
        else:
            Interface.FJLT_Bound_recommend(self)  # 调用福建联通点播业务分组

    def test_paging(self):
        """隐藏/显示分页"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.busines_com()  # 点击业务组合
        test_name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]').is_displayed()  #  is_displayed用于该元素是否存在的判断
        if test_name:
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/button[1]/i').click()
            time.sleep(1)
            try:
                name = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[2]/div[4]/div[1]/span[1]').is_displayed()
                assert not name
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()

    def test_column_operation(self):
        """列操作"""
        # Global.Oms_sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.busines_com()  # 点击业务组合
        number = driver.find_element_by_xpath('//*[@id="table"]/thead/tr/th[2]/div[1]').text   #  序号
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/button').click()  #  点击列
        i = 0
        while 1:
            i = i+1
            driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/div[2]/div[1]/div[2]/div/ul/li['+ str(i) +']/label/input').click()  #  点击序号复选
            time.sleep(2)
            num = driver.find_element_by_xpath('//*[@id="table"]/thead/tr/th[2]/div[1]').text   #   操作
            try:
                assert num != number
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
            if i == 9:
                break

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()