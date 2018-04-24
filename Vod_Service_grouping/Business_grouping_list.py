# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface
from framework.logger import Logger
from selenium.webdriver.support import expected_conditions as EC
import os
logger = Logger(logger="BrowserEngine").getlog()
group_name = 'KS业务分组测试'
configuration = 'KS配置预览自动化测试（勿动）'
#业务分组列表
class Business(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_New_service(self):
        """新增业务分组"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()      #点击业务分组
        # style = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  #  铁通总部点播业务分组
        homepage.custom_toolbar()     #点击新增
        homepage.add_names('az')       #添加名称
        Select(driver.find_element_by_id('agentvendorcode')).select_by_value('1100094160121140000053725')   #选择铁通总部
        time.sleep(1)
        homepage.description('测试专用')        #添加描述
        homepage.btnCreates()       #点击新建

    def test_Search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[13]/td[3]').text    #搜索新增名称
        homepage.searchText(group_name)      #输入名称
        homepage.custom_button()        #点击搜索
        time.sleep(1)
        new_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            assert new_name == group_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Start_stop(self):
        """启用/停用"""
        """启用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[1]/input').click()       #点击对勾
        homepage.table_Input()  # 点击对勾
        homepage.customtoolbar()        #点击启用
        try:
            assert VodSearch.get_ass_text(self) == '业务分组状态更新成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        space = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text    #获取状态
        try:
            assert space == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """停用"""
        # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[1]/input').click()  # 点击对勾
        homepage.table_Input()  # 点击对勾
        homepage.customtoolbar2()       #D点击停用
        try:
            assert VodSearch.get_ass_text(self) == '业务分组状态更新成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        space = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[5]').text        #获取状态
        try:
            assert space == '禁用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Edit(self):
        """业务分组编辑"""
        homepage = HomePage(self.driver)
        driver = self.driver
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text     #名称
        text1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text     #渠道商
        text2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[6]').text     #描述
        homepage.table_Bj()  # 点击编辑
        homepage.clear_names()  #清空名称
        homepage.add_names(text + '（编辑）')
        Select(driver.find_element_by_id('agentvendorcode')).select_by_value('1100094160112170000031863')
        homepage.clear_description()    #清空描述
        homepage.description(text2 + '（编辑）')
        homepage.btnSaves()     #保存
        homepage.searchText(text + '（编辑）')      #输入搜索名称
        homepage.custom_button()        #点击搜索
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        channel = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text
        describe = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[6]').text
        try:
            assert name == text + '（编辑）' and channel != text1 and describe == text2 + '（编辑）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Sheet_export(self):
        """片单导出"""
        homepage = HomePage(self.driver)
        driver = self.driver
        name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        homepage.table_Input()      #点击对勾
        driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/button[5]').click()     #点击片单导出
        try:
            assert VodSearch.get_ass_text(self) == '创建成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        homepage.jc_peizhi()        #点击基础配置
        homepage.collapseThree()        #点击任务查询
        task_table = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[3]').text   #获取名称
        try:
            assert task_table == '业务分组栏目树：' + name + '...详单导出'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Column_details(self):
        """栏目详情"""
        """解除绑定"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()  # 点击业务分组
        style = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text   #   获取第一个业务分组名称
        homepage.edit_product()     #点击栏目详情按钮
        homepage.body_right()       #解除绑定
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        time.sleep(5)
        value = driver.find_element_by_xpath('//*[@id="allCategory"]/option[1]').text  # 获取value为0的‘栏目树选择’
        try:
            assert value == '--栏目树选择--'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        Select(driver.find_element_by_id('allCategory')).select_by_value('2100050106019587104660053')  # 选择AAS自动化测试（勿动）
        alert.accept()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="body_right"]/form/div[1]/button').click()        #点击绑定
        time.sleep(1)
        alert.accept()
        time.sleep(5)
        # name = driver.find_element_by_xpath('//*[@id="allCategory"]/option[5]').text
        name = driver.find_element_by_xpath('//*[@id="2100050106019587104660053"]').text
        try:
            assert name == 'AAS自动化测试（勿动）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """位置上移"""
        # title = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[6]/td[3]').text
        title = driver.find_element_by_xpath('//*[@id="2100050106017032812170050"]').text     #国产大片
        title1 = driver.find_element_by_xpath('//*[@id="2100050106017902720040065"]').text    #欧美大片
        driver.find_element_by_xpath('//*[@id="body_right"]/form/div[2]/div/table/tbody/tr[5]/td[2]/a[1]/i').click()    #点击上移
        time.sleep(1)
        new_title = driver.find_element_by_xpath('//*[@id="2100050106017902720040065"]').text  #欧美大片
        new_title1 = driver.find_element_by_xpath('//*[@id="2100050106017032812170050"]').text#国产大片
        try:
            assert title == new_title1 and title1 == new_title
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        driver.find_element_by_xpath(
            '//*[@id="body_right"]/form/div[2]/div/table/tbody/tr[5]/td[2]/a[1]/i').click()  # 点击上移
        time.sleep(1)
        """添加子栏目"""
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[2]/td[2]/a/i').click()        #点击添加栏目
        time.sleep(1)
        column_name = '综艺专栏'
        homepage.add_names(column_name)     #添加栏目名称
        homepage.description(column_name)   #添加描述
        homepage.btnCreates()       #点击新建
        test = driver.find_element_by_css_selector('html body div#main.container-fluid div.row div#body_right.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main form div.row div.col-md-9 table.table.tree.table-hover tbody tr.treegrid-8.treegrid-parent-1').text  #  获取子栏目一行名称
        new_string = test.split('私')[0].strip()  # 切割需要的字段
        try:
            assert new_string == column_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """修改栏目"""
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[9]/td[2]/a[2]/i').click()        #点击修改
        time.sleep(1)
        homepage.add_names('（修改）')
        homepage.btnSaves()     #点击保存
        modify = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[9]/td[3]').text   #获取修改后的名称
        try:
            assert modify == column_name + '（修改）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """绑定产品包"""
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[9]/td[2]/a[5]/i').click() #点击绑定产品包
        time.sleep(1)
        test_name = driver.find_element_by_xpath('//*[@id="libPkgTable"]/tbody/tr[1]/td[2]').text   #获取产品名称
        homepage.pkgStyleSearchText(test_name)   #输入产品名称
        driver.find_element_by_xpath('//*[@id="btnPkgStyleSearch"]').click()    #点击搜索
        time.sleep(2)
        homepage.libPkgTable()  #点击对勾
        homepage.prd_add()      #点击右箭头
        new_test = driver.find_element_by_xpath('//*[@id="selectedPkgTable"]/tbody/tr/td[2]').text #获取绑定产品包名称
        try:
            assert new_test == test_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.bindProduct()      #确认
        num = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        try:
            assert num == '数据已经保存！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()   #确认
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[9]/td[2]/a[5]/i').click()  # 点击绑定产品包
        time.sleep(1)
        homepage.cleanProduct() #点击清空
        alert.accept()
        time.sleep(2)
        try:
            assert VodSearch.get_ass_text(self) == '栏目下产品包清除完毕'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()    #确认
        def matching():
            colspan = driver.find_element_by_xpath('//*[@id="selectedPkgTable"]/tbody/tr/td').text
            try:
                assert colspan == '没有找到匹配的记录'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.heartPackage() #点击关闭
        matching()
        # driver.find_element_by_xpath(
        #     '/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[9]/td[2]/a[5]/i').click()  # 点击绑定产品包
        # matching()     #有BUG
        """删除"""
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/form/div[2]/div/table/tbody/tr[9]/td[2]/a[3]/i').click() #点击删除按钮
        time.sleep(2)
        """片单导出"""
        homepage.exportBtn()    #点击片单导出按钮
        bootbox = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        try:
            assert bootbox == '创建成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()   #确认
        homepage.jc_peizhi()#基础配置
        homepage.collapseThree()#任务查询
        font = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[3]').text
        try:
            assert font == '业务分组栏目树：' + style + '_详单导出'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Preview_confirmation(self):
        """配置预览和确认"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        def search():
            homepage.servicegrouping()  # 点击业务分组
            homepage.searchText(configuration)
            homepage.custom_button()  #  搜索
        search()
        dealer = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[4]').text  #  获取渠道商名称
        homepage.collapseOnes()   #  点击分发域绑定
        Select(driver.find_element_by_id('allServiceGroup')).select_by_value('1100122106018099388980003')  #  选择KS配置预览自动化测试（勿动）
        homepage.custom_toolbar()   #  点击新增
        Select(driver.find_element_by_id('domaincode')).select_by_value(
            '2100090106019242386300101')  # 选择分发域测试（测试勿动）
        driver.find_element_by_xpath('//*[@id="domain_form"]/div[2]/div/button[1]').click() # 点击绑定
        time.sleep(2)
        homepage.ffy_sx_queding()  #  点击确认
        distribution_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text  #  获取分发域名称（分发域测试（测试勿动））
        search()
        homepage.glyphicon_edit()  # 栏目详情
        Select(driver.find_element_by_id('allCategory')).select_by_value(
            '2100050106019587104660053')  # 选择AAS自动化测试（勿动）
        driver.switch_to_alert().accept()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="body_right"]/form/div[1]/button').click()  # 点击绑定
        driver.switch_to_alert().accept()
        time.sleep(1)
        film = driver.find_element_by_xpath('//*[@id="2100050106016298181750005"]').text   #  获取名称（电影）
        search()
        homepage.dj_shangxx()  #点击配置预览和确认按钮
        homepage.body_rights()#点击渠道商
        channel = driver.find_element_by_xpath('//*[@id="svcGrpTable"]/tbody/tr/td[2]').text    #  获取渠道商名称
        try:
            assert channel == dealer
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.body_rights1()#点击栏目
        column = driver.find_element_by_xpath('//*[@id="categoryTable"]/tbody/tr[2]/td[1]').text
        try:
            assert column == film
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.body_rights2()#点击分发域
        domain = driver.find_element_by_xpath('//*[@id="domainTable"]/tbody/tr/td[1]').text
        try:
            assert domain == distribution_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        def unbundling():
            homepage.collapseOnes()  # 点击分发域绑定
            Select(driver.find_element_by_id('allServiceGroup')).select_by_value(
                '1100122106018099388980003')  # 选择KS配置预览自动化测试（勿动）
            homepage.table_Bj()  #  点击解除绑定
            driver.switch_to_alert().accept()
            homepage.ffy_sx_queding()   #  点击确认
            search()
            homepage.glyphicon_edit()  # 点击栏目详情
            homepage.body_right()  # 点击解除绑定
            driver.switch_to_alert().accept()
        unbundling()
        search()
        homepage.dj_shangxx()  # 点击配置预览和确认按钮
        driver.find_element_by_xpath('//*[@id="body_right"]/div[2]/ul/li[1]/a').click() #点击产品列表
        time.sleep(2)
        homepage.btnAddSeries()  #  点击导入节目集
        add_name = driver.find_element_by_xpath('//*[@id="sgAddSeriesTable"]/tbody/tr[1]/td[2]').text   #  获取节目集名称
        homepage.addSeriesName(add_name)  #  输入名称
        homepage.addSeriesName(Keys.ENTER)  #  回车搜索
        homepage.sgAddSeriesTable()  #  点击复选
        driver.find_element_by_xpath('//*[@id="addSeries"]/div/div/div[2]/div[2]/button[1]').click()  #  点击导入
        time.sleep(2)
        try:
            assert VodSearch.get_ass_text(self) == '产品已经加入到业务分组下'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        driver.find_element_by_xpath('//*[@id="addSeries"]/div/div/div[2]/div[2]/button[2]').click()  #  点击关闭
        time.sleep(2)
        homepage.prdName(add_name)   #  搜索节目集关键字
        homepage.prdName(Keys.ENTER)
        name = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[4]').text   #获取名称
        try:
            assert name == add_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """删除节目集"""
        # driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[1]/input').click()  #  点击复选
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="btnRemoveSereis"]').click()  #  点击删除节目集
        driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[3]/a[2]/i').click()  #  点击删除
        time.sleep(2)
        driver.switch_to_alert().accept()  #  获取弹出框并确定
        try:
            assert VodSearch.get_ass_text(self) == '删除成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()  #  确认
        pipei = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td').text
        try:
            assert pipei == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.clear_prdName()  #清空
        homepage.prdName(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="productTable"]/thead/tr/th[1]/div[1]/input').click()  #  点击符合复选
        driver.find_element_by_xpath('//*[@id="btnRemoveSereis"]').click()  # 点击删除节目集
        driver.switch_to_alert().accept()  # 获取弹出框并确定
        homepage.ffy_sx_queding()  # 确认
        """导入栏目产品"""
        homepage.collapseOnes()  # 点击分发域绑定
        Select(driver.find_element_by_id('allServiceGroup')).select_by_value(
            '1100122106018099388980003')  # 选择KS配置预览自动化测试（勿动）
        homepage.custom_toolbar()  # 点击新增
        Select(driver.find_element_by_id('domaincode')).select_by_value(
            '2100090106019242386300101')  # 选择分发域测试（测试勿动）
        driver.find_element_by_xpath('//*[@id="domain_form"]/div[2]/div/button[1]').click()  # 点击绑定
        time.sleep(2)
        homepage.ffy_sx_queding()  # 点击确认
        search()
        homepage.glyphicon_edit()  # 栏目详情
        Select(driver.find_element_by_id('allCategory')).select_by_value(
            '2100050106019587104660053')  # 选择AAS自动化测试（勿动）
        driver.switch_to_alert().accept()
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="body_right"]/form/div[1]/button').click()  # 点击绑定
        driver.switch_to_alert().accept()
        time.sleep(1)
        search()
        homepage.dj_shangxx()  # 点击配置预览和确认按钮
        driver.find_element_by_xpath('//*[@id="btnSyncPrd"]').click()   #点击导入栏目产品按钮
        time.sleep(3)
        # text = driver.find_element_by_xpath('/html/body/div[5]/div/div/div[2]/div').text
        # try:
        #     assert text == '数据已经从业务分组-产品包关系同步完毕。'
        #     print('Test pass.')
        # except Exception as e:
        #     print("Test fail.", format(e))
        #     homepage.get_windows_img()
        homepage.ffy_sx_queding()   #确认
        test_name = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr[1]/td[4]').text  #  获取第一行节目集名称
        try:
            assert test_name == '冒险雷探长'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        unbundling()
        """同步到前端"""
        search()
        homepage.dj_shangxx()  # 点击配置预览和确认按钮
        driver.find_element_by_xpath('//*[@id="btnEsSync"]').click()  #  点击同步到前端
        time.sleep(1)
        try:
            assert VodSearch.get_ass_text(self) == '已发起同步'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.ffy_sx_queding()  #  确认

    def test_Display_record(self):
        """显示记录判断"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()  # 点击业务分组
        homepage.searchText('福建联通点播业务分组')  # 输入业务分组名称关键字
        homepage.searchText(Keys.ENTER)
        homepage.dj_shangxx()  #  点击配置预览和确认
        driver.execute_script("window.scrollBy(0,5000)")
        time.sleep(1)
        homepage.tab_product_button()  # 点击选择
        driver.find_element_by_xpath('//*[@id="tab_product"]/div[2]/div[2]/div[4]/div[1]/span[2]/span/ul/li[2]/a').click()  #  点击100
        time.sleep(2)
        driver.execute_script("window.scrollBy(0,3000)")
        time.sleep(1)
        number = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr[100]/td[2]').text  #  获取最后一个序号
        try:
            assert number == '100'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Delete(self):
        """删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()  # 点击业务分组
        name = group_name+'（编辑）'
        homepage.searchText(name)  #
        homepage.custom_button()  # 搜索
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[1]/input').click()   #对勾
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/button[4]').click()   #点击删除按钮
        time.sleep(1)
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        time.sleep(1)
        try:
            assert VodSearch.get_ass_text(self) == '业务分组删除成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        homepage.searchText(name)
        homepage.custom_button()
        colspan = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text
        try:
            assert colspan == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_View_blacklist(self):
        """查看黑名单列表"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()  # 点击业务分组
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a[7]/i').click()   #点击’查看黑名单列表‘按钮
        time.sleep(2)
        """新增"""
        homepage.custom_toolbar()#点击新增
        add_name = driver.find_element_by_xpath('//*[@id="productTable1"]/tbody/tr[1]/td[2]').text
        driver.find_element_by_xpath('//*[@id="productTable1"]/tbody/tr[1]/td[1]/input').click()
        time.sleep(1)
        homepage.addServiceGroupBlackProduct()#点击新增
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        ass_name = driver.find_element_by_xpath('//*[@id="guttv_dyn_alert"]').text
        try:
            self.assertEqual('添加黑名单成功。',ass_name)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.button_1()#点击确认
        driver.find_element_by_xpath('//*[@id="servicegroup_form"]/div[3]/div/button[2]').click()
        time.sleep(1)
        """搜索"""
        homepage.prdName(add_name)
        driver.find_element_by_xpath('//*[@id="custom-toolbar"]/div/input').click()#点击搜索
        time.sleep(1)
        new_name = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[2]').text
        try:
            assert new_name == add_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """删除"""
        driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[1]/input').click()#点击对勾
        time.sleep(1)
        homepage.customtoolbar2()#点击删除
        alert.accept()  # 点击对话框“确定”
        guttv = driver.find_element_by_xpath('//*[@id="guttv_dyn_alert"]').text
        try:
            self.assertEqual('删除成功',guttv)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())
        homepage.confirm_1()#点击确认
        span = driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td').text
        try:
            self.assertEqual('没有找到匹配的记录',span)
        except AssertionError as e:
            print("Test fail.",format(e),homepage.get_windows_img())

    def test_business_interface(self):
        """业务分组产品包绑定栏目树测试"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.servicegrouping()  # 点击业务分组
        homepage.searchText('KS自动化接口')
        homepage.custom_button()  # 搜索
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[2]/i').click()  #   点击栏目详情
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="body_right"]/form/div[2]/div/table/tbody/tr[7]/td[2]/a[3]/i').click()  #  点击黄金剧场绑定产品包
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[1]/input').click()  #  点击复选
        time.sleep(1)
        Interface.Unbundling_tree(self)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="productTable"]/tbody/tr/td[1]/input').click()  # 点击复选
        time.sleep(1)
        Interface.Binding_tree(self)
        driver.find_element_by_xpath('//*[@id="commonPackage"]/div/div/div[1]/button/span').click()  #  点击关闭
        time.sleep(1)

    def test_add_column(self):
        """添加栏目接口测试"""
        driver = self.driver
        homepage = HomePage(self.driver)
        # driver.find_element_by_xpath('//*[@id="addCategory_2100050106018519141430411"]/i').click()  #  点击添加栏目
        # time.sleep(2)
        # homepage.add_names('电视剧')
        # homepage.btnCreates()  #  点击新建
        # driver.find_element_by_css_selector('html body div#main.container-fluid div.row div#body_right.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main form div.row div.col-md-9 table.table.tree.table-hover tbody tr.treegrid-9.treegrid-parent-7 td input#cat_status_2100123106018823368750047').click()  #  点击复选
        # driver.find_element_by_css_selector('').click()  #  点击复选
        driver.find_element_by_xpath('//*[@id="cat_status_2100123106018915002910148"]').click()  #  点击复选
        homepage.sleep(1)
        Interface.Add_column_interface(self)
        driver.find_element_by_xpath('//*[@id="cat_status_2100123106018915002910148"]').click()  # 点击复选
        homepage.sleep(1)

    def test_Corner(self):
        """角标"""
        VodSearch.test_Sign_in(self)
        corner = '角标'
        driver = self.driver
        homepage = HomePage(self.driver)
        homepage.servicegrouping()  # 点击业务分组
        homepage.searchText(corner)
        homepage.custom_button()  # 搜索
        homepage.table_Bj()  # 点击编辑
        driver.find_element_by_xpath('//*[@id="corner_ru"]').click()  #  点击右上
        time.sleep(1)
        picture_path = os.path.abspath('..') + "\\All_pictures\\01.jpg"
        driver.find_element_by_id('pictureFile').send_keys(picture_path)
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="pictureDiv"]/div/div/div[3]/div[2]/a/i').click()  #  点击上传
        time.sleep(2)
        try:
            assert VodSearch.get_ass_text(self) == '更新成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()        #确认
        homepage.btnSaves()        #保存
        homepage.dj_chanpguanl()        # 点击产品管理
        homepage.searchBtn()        # 点击搜索
        homepage.add_names(corner)        # 输入名称
        homepage.add_names(Keys.ENTER)
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[8]/i').click()  #  点击角标
        time.sleep(1)
        Select(driver.find_element_by_id('allServiceGroup')).select_by_value('1100122106019338200200003')  # 选择角标
        driver.find_element_by_xpath('//*[@id="corner_alone"]').click()# 点击独播
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="btnUpdateCorner"]').click()# 点击保存
        time.sleep(1)
        driver.switch_to_alert().accept()
        try:
            assert VodSearch.get_ass_text(self) == '成功保存角标。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        time.sleep(100)

        Interface.superscript(self)

        homepage.servicegrouping()  # 点击业务分组
        homepage.searchText(corner)
        homepage.custom_button()  # 搜索
        homepage.table_Bj()  # 点击编辑
        driver.find_element_by_xpath('//*[@id="corner_lu"]').click()  # 点击左上
        time.sleep(1)
        picture_path = os.path.abspath('..') + "\\All_pictures\\02.jpg"
        driver.find_element_by_id('pictureFile').send_keys(picture_path)
        driver.find_element_by_xpath('//*[@id="pictureDiv"]/div/div/div[3]/div[2]/a/i').click()  # 点击上传
        time.sleep(2)
        homepage.button_1()  # 确认
        homepage.btnSaves()  # 保存















    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()



