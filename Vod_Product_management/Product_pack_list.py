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
product_api_name = '测试产品包专用'
display_name = '测试专用'
#产品包列表
class Product(unittest.TestCase,Interface):
    @classmethod
    def setUpClass(cls):
        """
        :return:
        """
        browse = BrowserEngine(cls)
        cls.driver = browse.open_browser(cls)

    def test_Newly_added(self):
        """产品包新增"""
        VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_chanpguanl()        #产品管理
        # homepage.searchBtn()        #点击搜索
        # homepage.add_names(product_api_name)        #输入名称
        # homepage.add_names(Keys.ENTER)
        # packagename = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        # if packagename == product_api_name or packagename == product_api_name+'接口测试' or packagename == product_api_name+'_复制':
        #     driver.find_element_by_xpath('//*[@id="body_right"]/div[5]/div[2]/div[1]/table/thead/tr/th[1]/div[1]/input').click()  #  点击复选
        #     time.sleep(1)
        #     homepage.custom4_toolbar()  #  点击删除
        #     driver.switch_to_alert().accept()
        #     homepage.confirm_1()  #  确认
        #     homepage.searchReset()  #  重置
        homepage.custom_toolbar()        #新增
        homepage.sr_mingchen(product_api_name)   #输入名称
        homepage.sr_zs_mingchen(display_name)   #输入展示名称
        homepage.xz_chanping()      #选择产品
        product_name = driver.find_element_by_xpath('//*[@id="unSelectedProductTable"]/tbody/tr[6]/td[2]').text# 产品包-产品管理-选择产品名称
        cp_name = driver.find_element_by_xpath('//*[@id="unSelectedProductTable"]/tbody/tr[6]/td[4]').text  # 产品包-产品管理-选择cp名称
        homepage.cp_mingchen(product_name)      #输入产品名称
        homepage.sr_chanp()     #点击CP下拉框
        homepage.sr_cp_mingchen(cp_name)    #输入cp名称
        homepage.sr_cp_mingchen(Keys.ENTER)
        homepage.dj_duig()      #点击对勾
        homepage.prd_add()      #点击右箭头
        select = driver.find_element_by_xpath('//*[@id="selectedProductTable"]/tbody/tr/td[2]').text
        cp_select = driver.find_element_by_xpath('//*[@id="selectedProductTable"]/tbody/tr/td[4]').text
        try:
            assert select == product_name and cp_select == cp_name
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        homepage.pd_dialog()        #点击清除筛选
        none = driver.find_element_by_xpath('//*[@id="productName"]').text  #匹配‘输入产品名称框’
        cps = driver.find_element_by_xpath('//*[@id="product_dialog"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/label[2]/div/button/span[1]').text  #匹配‘输入产品名称框’
        try:
            assert none == '' and cps == '全部'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        homepage.btnSaves()      #确认按钮
        currenttime = time.strftime("%Y-%m-%d %H:%M", time.localtime())
        logger.info('The current time is:%s' % currenttime)
        Select(self.driver.find_element_by_id('create_type1')).select_by_value('1')  # 包类型选择专题包
        driver.find_element_by_id('create_pictureurl1File').send_keys('d:\\prac.jpg')   #上传图片
        driver.find_element_by_xpath('//*[@id="create_package_form"]/div[5]/div/div/div[3]/div[2]/a/span').click()#点击上传
        time.sleep(3)
        homepage.btnCreat()     #点击保存按钮
        try:
            assert VodSearch.get_ass_text(self) == '创建操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.',format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认按钮
        """产品打包时间"""
        homepage.searchBtn()        #点击搜索
        # test_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.add_names(product_api_name)       #输入搜索名称
        homepage.searchByName()                #点击搜索按钮
        homepage.dj_shangxx()                #点击编辑
        homepage.chooseProduct()                #点击选择产品
        packingtime = driver.find_element_by_xpath('//*[@id="selectedProductTable"]/tbody/tr/td[7]').text
        pack0 = packingtime.split(':')[0]
        pack1 = packingtime.split(':')[1]
        get_time = pack0 + ':' + pack1
        logger.info('The time to get is:%s'%get_time)
        try:
            assert get_time == currenttime
            print('Test pass')
        except Exception as e:
            print('Test fail.',format(e))
            homepage.get_windows_img()
        homepage.btnSaves()  #  确认
        driver.find_element_by_xpath('//*[@id="edit_package_form"]/div[10]/div/button[2]').click()   #  点击关闭
        time.sleep(1)
        search_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        try:
            assert search_name == product_api_name
            print('Test pass')
        except Exception as e:
            print('Test fail.',format(e))
            homepage.get_windows_img()
        homepage.searchReset()      #点击重置

    def test_Product_up(self):
        """产品包上线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isLine')).select_by_value('0')  # 在线状态选择待上线
        time.sleep(5)
        # old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        # time.sleep(2)
        homepage.table_2()  # 点击编辑
        homepage.package_name('(上线测试)')  # 名称添加字段
        homepage.edit_package_tag('测试')#添加产品标签
        homepage.edit_package_form()  # 点击保存
        # 判断是否操作编辑是否成功
        try:
            assert VodSearch.get_ass_text(self) == '编辑操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        homepage.confirm_1()  # 点击编辑确定
        up_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待上线名称
        homepage.send_submit_btn()      #点击上线
        try:
            assert VodSearch.get_ass_text(self) == '上线操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()            #点击确认
        homepage.add_names(up_name)  # 通过xpath定位输入框，send_keys传值到输入框
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(2)
        homepage.searchByName()  # 点击搜索
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert test == up_name and test1 == '上线'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.searchReset()  # 重置

    def test_Product_down(self):
        """产品包下线"""
        homepage = HomePage(self.driver)
        driver = self.driver
        Select(driver.find_element_by_id('isLine')).select_by_value('1')  # 在线状态选择上线
        time.sleep(5)
        # old_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        # time.sleep(2)
        homepage.edit_product()  # 点击编辑
        homepage.package_name('(下线测试)')  # 名称添加字段
        homepage.edit_package_form()  # 点击保存
        # 判断是否操作编辑是否成功
        try:
            assert VodSearch.get_ass_text(self) == '编辑操作成功!'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()  # 调用基类截图方法
        time.sleep(2)
        homepage.confirm_1()  # 点击编辑确定
        up_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 匹配待上线名称
        homepage.send_submit_btn()      #点击下线
        try:
            assert VodSearch.get_ass_text(self) == '下线操作成功!'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()            #点击确认
        homepage.add_names(up_name)  # 通过xpath定位输入框，send_keys传值到输入框
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(2)
        homepage.searchByName()  # 点击搜索
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        test1 = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[8]').text
        try:
            assert test == up_name and test1 == '下线'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        # homepage.searchReset()  # 重置

    def test_Special_poster(self):
        """专题海报"""
        """上传"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.special_poster()  #  专题海报
        homepage.spec_table()  #  点击上传
        driver.find_element_by_id('spec_pictureurl1File').send_keys('d:\\spec.jpg')  # 上传图片
        time.sleep(2)
        driver.find_element_by_xpath('//*[@id="spec_poster"]/div/div/div[2]/div[1]/div[3]/div[2]/a/span').click()  # 点击上传
        time.sleep(3)
        try:
            assert VodSearch.get_ass_text(self) == '专题海报更新成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.button_1()   #  确认
        """删除"""
        homepage.spec_input_table()  #  点击复选
        driver.find_element_by_css_selector('html body div#main.container-fluid div.row div#body_right.col-sm-9.col-sm-offset-3.col-md-10.col-md-offset-2.main div#spec_pkg_pic.modal.fadein.in div.modal-dialog.modal-lg div.modal-content div.modal-body div#custom-toolbar div.form-inline button.btn.btn-warning').click()  #  删除
        try:
            assert VodSearch.get_ass_text(self) == '删除专题海报成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.button_1()   #  确认
        old_name = driver.find_element_by_xpath('//*[@id="spec_table"]/tbody/tr/td[4]').text
        try:
            assert old_name == ''
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.spec_pkg_pic()   #  关闭


    def test_delete(self):
        """产品包删除"""
        homepage = HomePage(self.driver)
        driver = self.driver
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        homepage.delete_an()
        driver.switch_to_alert().accept()   #点击弹出里面的确定按钮
        try:
            assert VodSearch.get_ass_text(self) == '删除成功！'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()
        homepage.add_names(test)        #输入产品包名称
        homepage.searchByName()     #点击搜索
        text = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td').text    #没有找到匹配的记录
        try:
            assert text == '没有找到匹配的记录'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.searchReset()      #重置

    def test_Search(self):
        """搜索"""
        homepage = HomePage(self.driver)
        driver = self.driver
        initial_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text  # 获取初始名称
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[9]').text  # 获取包类型
        homepage.add_names(initial_name)
        Select(driver.find_element_by_id('type1')).select_by_visible_text(cp_name)  # 审核下拉框并选择全部
        time.sleep(2)
        homepage.searchByName()  # 点击搜索
        test = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[3]').text
        type = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[9]').text
        try:
            assert test == initial_name and type == cp_name
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Reset(self):
        """重置"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.searchReset()
        test = driver.find_element_by_xpath('//*[@id="name"]').text
        select = driver.find_element_by_xpath('//*[@id="type1"]/option[1]').text
        try:
            assert test == '' and select == '全部'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Sheet_export(self):
        """片单导出"""
        homepage = HomePage(self.driver)
        driver = self.driver
        initial = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text   #获取初始名称
        homepage.table_input()      #点击对勾
        driver.find_element_by_xpath('//*[@id="exportBtn"]').click()        #点击片单导出
        # homepage.dc_shuju()     #数据导出
        try:
            assert VodSearch.get_ass_text(self) == '创建成功'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()
        homepage.confirm_1()        #确认
        homepage.jc_peizhi()        #基础配置
        homepage.collapseThree()    #任务查询
        new_text = driver.find_element_by_xpath('//*[@id="task_table"]/tbody/tr[1]/td[3]').text
        try:
            assert new_text == '产品包：'+initial+'_详单导出' or new_text == '产品包：' +initial+ '...详单导出'
            print('Test pass')
        except Exception as e:
            print('Test fail.', format(e))
            homepage.get_windows_img()

    def test_Online_status(self):
        """在线状态"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_chanpguanl()
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
        Select(driver.find_element_by_id('isLine')).select_by_visible_text('全部')  # 审核下拉框并选择全部
        time.sleep(2)

    def test_package_copy(self):
        """产品包复制"""
        homepage = HomePage(self.driver)
        driver = self.driver
        cp_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[3]').text
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[3]/td[1]/input').click()  #
        time.sleep(1)
        homepage.copyBtn()  #  点击产品包复制
        try:
            assert VodSearch.get_ass_text(self) == '产品包复制中'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        copy_name = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[3]').text
        try:
            assert copy_name == cp_name + '_复制'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.delete_copy()  #  删除
        driver.switch_to_alert().accept()
        homepage.confirm_1()  # 确认

    def test_package_interface(self):
        """产品包接口测试"""
        # VodSearch.test_Sign_in(self)
        homepage = HomePage(self.driver)
        driver = self.driver
        # homepage.dj_chanpguanl()  # 产品管理
        homepage.custom_toolbar()  # 新增
        homepage.sr_mingchen(product_api_name+'接口测试')  # 输入名称
        homepage.sr_zs_mingchen(display_name)  # 输入展示名称
        homepage.xz_chanping()  # 选择产品
        homepage.cp_mingchen('厉害了我的歌 高清')  #  输入产品名称
        homepage.sr_chanp()  # 点击CP下拉框
        homepage.sr_cp_mingchen('天脉')  # 输入cp名称
        homepage.sr_cp_mingchen(Keys.ENTER)
        homepage.dj_duig()  # 点击对勾
        homepage.prd_add()  # 点击右箭头
        homepage.btnSaves()  #  点击确认
        homepage.btnCreat()  #  点击保存
        homepage.confirm_1()  #  点击确认
        code = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[4]').text
        with open('D:\\code.txt', 'w', encoding='utf-8') as ff:
            ff.write(code)
        state = driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[1]/td[8]').text
        if state != '上线':
            homepage.table_input()  #  点击复选
            homepage.online_1()  #  点击上线
            homepage.confirm_1()  #  点击确认
            homepage.column_M()  #  点击栏目管理
            driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[10]/td[2]/a[2]/i').click()  #  点击江苏移动详情
            time.sleep(2)
            # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[2]/td[2]/span[2]').click() #  点击展开纪录片
            # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[8]/td[2]/span[2]').click() #  点击展开纪录片
            # time.sleep(2)
            driver.execute_script("window.scrollBy(0,100)")
            time.sleep(1)
            driver.find_element_by_xpath('//*[@id="product_2100050106018763352330003"]/i').click()  #  点击产品包数量
            time.sleep(2)
            homepage.packageSearchText(product_api_name+'接口测试')  #  输入产品名称
            homepage.btnPkgSearch()  #  点击搜索
            driver.find_element_by_xpath('//*[@id="libPkgTable"]/tbody/tr/td[1]/input').click()  #  点击复选
            homepage.prd_add()  #  向右追加
            homepage.bindProduct()  #  点击确认
            homepage.confirm_1()  #  确认
            # time.sleep(25)
            # Interface.Product_downline(self)

    def test_Product_interface(self):
        """产品加入产品包接口测试"""
        homepage = HomePage(self.driver)
        driver = self.driver
        homepage.dj_chanpguanl()  # 点击产品管理
        homepage.collapseOne()  # 点击产品列表
        homepage.searchBtn()  # 点击搜索
        homepage.add_names('大话天仙')  # 输入产品名称
        homepage.cp_dianji()  # 点击cp下拉
        homepage.cp_shuru('4K花园')  # 输入cp名称
        homepage.cp_shuru(Keys.ENTER)
        homepage.searchByName()  # 点击搜索
        homepage.table_Input()  # 点击复选
        driver.find_element_by_xpath('//*[@id="batchAddPkgs"]').click()  #  点击加入产品包
        homepage.s_PkgName(product_api_name+'接口测试')  #  输入产品包名称
        homepage.s_BtnSearch()  #  点击搜索
        homepage.unbindPkgTable()  #  点击复选
        homepage.add_package_dialog()  #  点击导入
        homepage.btnSaves()  #  点击确认
        try:
            assert VodSearch.get_ass_text(self) == '产品已经加入产品包中'
            print('Test pass.')
        except Exception as e:
            print("Test fail.", format(e))
            homepage.get_windows_img()
        homepage.confirm_1()  #  确认
        # time.sleep(20)
        # Interface.Binding_package(self)
        homepage.coLLapseTwo()  #  点击产品包列表
        homepage.edit_product()  #  点击编辑
        homepage.chooseProduct()  #  点击选择产品
        driver.find_element_by_xpath('//*[@id="selectedProductTable"]/tbody/tr[1]/td[1]/input').click()  #  点击复选
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="productRemove"]').click()  #  点击导出
        time.sleep(1)
        homepage.btnSaves()  #  点击确认
        homepage.edit_package_tag('测试')  #  点击确认
        homepage.edit_package_form()  #  点击保存
        homepage.confirm_1()  #  点击确认
        # time.sleep(5)
        # Interface.Product_No_downline(self)
        """删除产品包"""
        homepage.column_M()  # 点击栏目管理
        driver.find_element_by_xpath('//*[@id="table"]/tbody/tr[10]/td[2]/a[2]/i').click()  # 点击江苏移动详情
        time.sleep(2)
        # driver.find_element_by_xpath('//*[@id="categoryRoot"]/tbody/tr[8]/td[2]/span[2]').click()  # 点击展开纪录片
        # time.sleep(1)
        driver.execute_script("window.scrollBy(0,100)")
        time.sleep(1)
        driver.find_element_by_xpath('//*[@id="product_2100050106018763352330003"]/i').click()  # 点击产品包数量
        time.sleep(1)
        homepage.cleanProduct()  #  点击清空
        driver.switch_to_alert().accept()
        homepage.button_1()  #  点击确认
        homepage.productPkg()  #  点击关闭
        # driver.find_element_by_xpath('//*[@id="selectedPkgTable"]/tbody/tr[1]/td[1]/input').click()  #  点击复选
        # time.sleep(1)
        # driver.find_element_by_xpath('//*[@id="productRemove"]').click()  #  点击导出
        # time.sleep(1)
        # homepage.bindProduct()  #  点击确认
        # homepage.confirm_1()  #  点击确认
        homepage.dj_chanpguanl()  #  点击产品管理
        homepage.delete_an()  #  点击删除
        driver.switch_to_alert().accept()
        homepage.confirm_1()  #  点击确认

    def test_Corner(self):
        """角标"""
        # VodSearch.test_Sign_in(self)
        corner = '角标'
        driver = self.driver
        homepage = HomePage(self.driver)
        homepage.dj_chanpguanl()  # 点击产品管理
        homepage.searchBtn()  # 点击搜索
        homepage.add_names(corner)  # 输入产品名称
        homepage.add_names(Keys.ENTER)
        def choice_corner():
            driver.find_element_by_xpath('//*[@id="table"]/tbody/tr/td[2]/a[8]/i').click()  #  点击角标
            time.sleep(1)
            Select(driver.find_element_by_id('allServiceGroup')).select_by_value('1100122106019338200200003')  # 选择角标
        choice_corner()
        driver.find_element_by_xpath('//*[@id="corner_alone"]').click()  # 点击独播
        time.sleep(1)
        def preservation():
            driver.find_element_by_xpath('//*[@id="btnUpdateCorner"]').click()  # 点击保存
            time.sleep(1)
            driver.switch_to_alert().accept()
            try:
                assert VodSearch.get_ass_text(self) == '成功保存角标。'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
            homepage.confirm_1()  # 确认
            time.sleep(100)
        preservation()
        Interface.top_left_corner(self)
        choice_corner()
        driver.find_element_by_xpath('//*[@id="corner_vip"]').click()  # 点击VIP
        time.sleep(1)
        preservation()
        Interface.upper_right_corner(self)
        choice_corner()
        driver.find_element_by_xpath('//*[@id="corner_head"]').click()  # 点击首播
        time.sleep(1)
        preservation()
        Interface.lower_right_corner(self)
        choice_corner()
        driver.find_element_by_xpath('//*[@id="corner_hot"]').click()  # 点击热播
        time.sleep(1)
        preservation()
        Interface.lower_left_corner(self)

    @classmethod
    def tearDownClass(cls):
        """
        :return:
        """
        cls.driver.quit()





