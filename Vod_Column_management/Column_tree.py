# coding=utf-8
import unittest,time,random
from framework.browser_engine import BrowserEngine
from pageobjects.cibn_homepage import HomePage
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
from Vod_Content_management.EpisodesList import VodSearch
from framework.Interface_test import Interface
from framework.logger import Logger

logger = Logger(logger="BrowserEngine").getlog()
#栏目树管理
class Column(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_New_tree(self):
        """新建栏目树"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.column_M()     #点击栏目管理
        display_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        management_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        homepage.treeAdd()      #点击新建栏目树
        homepage.add_names(display_name + '（测试）')
        homepage.managename(management_name + '（测试）')
        homepage.description('测试专用，勿动！')
        homepage.btnCreateTree()        #新建
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[3]').text
        test2 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[4]').text
        try:
            assert test1 == display_name + '（测试）' and test2 == management_name + '（测试）'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Start_stop(self):
        """启用/停用"""
        """启用"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.table_input1()      #点击对勾
        homepage.btnStartup()       # 启用
        alert = driver.switch_to_alert()    #定位弹出对话框
        alert.accept()          #点击对话框“确认”
        time.sleep(1)
        try:
            assert VodSearch.get_ass_text(self) == '状态更新成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        # table = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[6]').text
        table = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]').text
        try:
            assert table == '启用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """停用"""
        homepage.table_input1()     #对勾
        homepage.btnStartdown()     #停用
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确认”
        time.sleep(1)
        try:
            assert VodSearch.get_ass_text(self) == '状态更新成功。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  # 确认
        table1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[2]/td[5]').text
        try:
            assert table1 == '停用'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_Detailed(self):
        """详细"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.tab_Deta()     #点击详细
        """推荐位绑定"""
        homepage.categoryRoot()     #推荐位绑定
        homepage.selectorTable()    #推荐位选择
        font = driver.find_element_by_xpath('//*[@id="selectorTable"]/tbody/tr[1]/td[2]').text
        homepage.btnSelected()      #推荐位确认
        homepage.confirm_1()        #确认
        label = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr/td[4]/label').text
        try:
            assert label == font
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """删除推荐位"""
        homepage.categoryRoot1()        #推荐位删除
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确认”
        time.sleep(1)
        try:
            assert VodSearch.get_ass_text(self) == '推荐位已经取消'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        # try:
        #     assert label == ''
        #     print('Test pass.')
        # except Exception as e:
        #     print("Test fail.", format(e))
        #     homepage.get_windows_img()
        """添加子栏目"""
        homepage.categoryRoot2()        #添加子栏目
        film = '电影'
        homepage.add_names(film)        #栏目显示名称
        homepage.managename(film)       #栏目管理名称
        homepage.description(film)      #描述信息
        homepage.btnCreateTree()        #点击新建
        # title = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]').text
        # try:
        #     assert title == film
        #     print('Test pass.')
        # except Exception as e:
        #     print("Test fail.", format(e))
        #     homepage.get_windows_img()
        """绑定产品包"""
        homepage.html_1()       #点击产品包
        test = driver.find_element_by_xpath('//*[@id="libPkgTable"]/tbody/tr[1]/td[2]').text
        homepage.packageSearchText(test)    # 输入产品名称
        homepage.btnPkgSearch()     #点击搜索
        homepage.libPkgTable()  #对勾
        homepage.prd_add()      #右箭头添加
        homepage.bindProduct()  #确认
        try:
            assert VodSearch.get_ass_text(self) == '数据已经保存！'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()    #确认
        driver.refresh()        #刷新当前页面
        time.sleep(2)
        add = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[5]').text
        try:
            assert add != '0 分'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.html_1()
        homepage.cleanProduct()     #点击清空
        alert = driver.switch_to_alert()  # 定位弹出对话框
        alert.accept()  # 点击对话框“确定”
        text = driver.find_element_by_xpath('/html/body/div[7]/div/div/div[2]/div').text
        try:
            assert text == '栏目：电影下的产品包已经清除。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.button_1()     #确认
        col = driver.find_element_by_xpath('//*[@id="selectedPkgTable"]/tbody/tr/td').text
        try:
            assert col == '没有找到匹配的记录'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.productPkg()       #点击关闭
        homepage.categoryRoot_1()       #二次添加子栏目
        films = '电视剧'
        homepage.add_names(films)  # 栏目显示名称
        homepage.managename(films)  # 栏目管理名称
        homepage.description(films)  # 描述信息
        homepage.btnCreateTree()  # 点击新建
        """位置上移"""
        titl = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[3]/td[2]').text
        homepage.categoryRoot_2()       #位置上移按钮
        title1 = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]').text
        try:
            assert titl == title1
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """位置下移"""
        a1 = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]').text
        driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]/a[2]/i').click()
        time.sleep(1)
        a = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[3]/td[2]').text
        try:
            assert a1 == a
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        """添加/删除推荐位"""
        homepage.categoryRoot_4()       #添加推荐位
        sty = driver.find_element_by_xpath('//*[@id="selectorTable"]/tbody/tr[1]/td[2]').text
        homepage.selectorTable()    #点击选择
        homepage.btnSelected()      #确认
        homepage.confirm_1()        #确认
        lab = driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr[2]/td[4]/label').text
        try:
            assert lab == sty
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.categoryRoot_3()       #删除推荐位
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '推荐位已经取消'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()
        """编辑"""
        homepage.categoryRoot_5()   #编辑资料
        homepage.add_names('（编辑）')  #修改名称，添加“编辑”
        homepage.btnSaveTree()      #点击保存
        # titles = driver .find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]').text
        # try:
        #     assert titles == '电视剧（编辑）' or titles ==  '电影（编辑）'
        #     print('Test pass.')
        # except Exception as e:
        #     print("Test fail.", format(e))
        #     homepage.get_windows_img()
        homepage.htmlbody() #点击子栏目
        a_name = '欧美大片'
        homepage.add_names(a_name)      #显示名称
        homepage.managename(a_name)     #管理名称
        homepage.description(a_name)        #描述
        homepage.btnCreateTree()        #新建
        # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]/span[2]').click()   #点击扩展箭头
        # time.sleep(2)
        driver.find_element_by_xpath('/html/body/div[3]/div/div[2]/table/tbody/tr[3]/td[5]/a/i').click()#点击添加产品包
        time.sleep(1)
        homepage.libPkgTable()#对勾
        homepage.prd_add()#右箭头添加
        homepage.bindProduct()#确认
        homepage.confirm_1()#确认
        driver.refresh()  # 刷新当前页面
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]/span[2]').click()  # 点击扩展箭头
        # time.sleep(2)
        time_box = driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[3]/td[5]').text
        try:
            assert time_box != '0 分'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[3]/td[6]/a[2]/i').click()        #子栏目删除
        alert.accept()
        time.sleep(2)
        alerts = driver.switch_to_alert()
        alerts.accept()

    def test_Delete(self):
        """删除栏目树"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.column_M()     #点击栏目管理
        homepage.table_input1()     #点击对勾
        homepage.treeRemove()       #删除栏目树
        alert = driver.switch_to_alert()
        alert.accept()
        try:
            assert VodSearch.get_ass_text(self) == '删除完毕。'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认

    def test_Sheet_export(self):
        """片单导出"""
        homepage = HomePage(self.driver)
        driver = self.driver
        display_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.table_input()      #点击对勾
        driver.find_element_by_xpath('//*[@id="exportBtn"]').click()       #点击片单导出
        try:
            assert VodSearch.get_ass_text(self) == '创建成功'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        homepage.jc_peizhi()        #基础配置
        homepage.collapseThree()        #任务查询
        test_name = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[3]').text
        try:
            assert test_name == '通用栏目树：' +display_name+ '...详单导出'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()

    def test_tree_state_interface(self):
        """栏目树状态接口测试"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.column_M()  #  点击栏目管理
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a[2]/i').click()  #  点击AAS自动化测试（勿动）  详细
        time.sleep(1)
        Interface.Tree_enable(self)
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="cat_status_2100050106016298181750005"]').click()  #  点击  电影  复选
        homepage.shutdown()  #  点击停用
        time.sleep(5)
        Interface.Tree_disable(self)
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]/span[2]').click()  #  点击4K专区展开
        # time.sleep(1)
        try:
            inputs = driver.find_elements_by_tag_name('input')
            for input in inputs:
                if input.get_attribute('type') == 'checkbox':
                    input.click()
        except Exception as e:
            print(e)
        time.sleep(1)
        homepage.startup()  #  点击启用
        time.sleep(5)
        Interface.Tree_enable(self)
        time.sleep(2)

    def test_package_binding_tree(self):
        """产品包绑定栏目树接口测试"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.column_M()  # 点击栏目管理
        # driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[2]/a[2]/i').click()  #  点击AAS自动化测试（勿动）  详细
        # time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[5]/td[2]/span[2]').click()  #  点击 电视剧 下拉箭头
        # time.sleep(1)
        driver.find_element_by_xpath('//*[@id="product_2100050106017034577740061"]/i').click()  #  点击 产品包数量
        time.sleep(1)
        Record = driver.find_element_by_xpath('//*[@id="selectedPkgTable"]/tbody/tr/td').text
        if Record == '没有找到匹配的记录':
            homepage.packageSearchText('青橙芒果咖啡（测试勿动！）')  # 输入
            homepage.packageSearchText(Keys.ENTER)
            driver.find_element_by_xpath('//*[@id="libPkgTable"]/tbody/tr/td[1]/input').click()
            time.sleep(1)
            homepage.prd_add()
            homepage.bindProduct()
            homepage.confirm_1()
            Interface.Binding_tree(self)
        else:
            package = driver.find_element_by_xpath('//*[@id="selectedPkgTable"]/tbody/tr/td[2]').text  # 获取绑定的产品包名称
            if package == '青橙芒果咖啡（测试勿动！）':
                Interface.Binding_tree(self)
            else:
                homepage.get_windows_img()
            homepage.cleanProduct()  # 点击清空
            driver.switch_to_alert().accept()
            homepage.button_1()  # 点击确认
            homepage.productPkg()  # 点击关闭
            Interface.Unbundling_tree(self)
            driver.find_element_by_xpath('//*[@id="product_2100050106017034577740061"]/i').click()  # 点击 产品包数量
            time.sleep(1)
            homepage.packageSearchText(package)  # 输入
            homepage.packageSearchText(Keys.ENTER)
            driver.find_element_by_xpath('//*[@id="libPkgTable"]/tbody/tr/td[1]/input').click()
            time.sleep(1)
            homepage.prd_add()
            homepage.bindProduct()
            homepage.confirm_1()
            Interface.Binding_tree(self)

    # @classmethod
    # def tearDownClass(cls):
    #     """
    #     :return:
    #     """
    #     cls.driver.quit()
