# -*- coding:utf-8 -*-
import configparser     #处理ini文件
import os.path
import urllib.request,re,json
from framework.logger import Logger
from pageobjects.cibn_homepage import HomePage

logger = Logger(logger="BrowserEngine").getlog()
test_name = '文雀 高清'
details_test = '详情测试'
class Interface(object):
    dir = os.path.dirname(os.path.abspath('.'))  # 相对路径获取方法
    chrome_driver_path = dir + '/tools/chromedriver.exe'
    ie_driver_path = dir + '/tools/IEDriverServer.exe'

    def __init__(self, driver):
        self.driver = driver

    def Browser(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        vod_api_url = config.get("testServer", "vod_api_URL")
        logger.info("The test server url is: %s" % vod_api_url)
        get_url = urllib.request.urlopen(vod_api_url).read()
        self.Code = get_url.decode('utf-8')
        self.ret_data = json.loads(self.Code)
        return self.ret_data

    def vod_api_browser(self):
        homepage = HomePage(self.driver)
        self.Browser()
        device_id = self.ret_data["retCode"]
        if device_id == '00000000':
            prod = re.findall('.*?"productName":"(.*?)"', self.Code)
            join = ''.join(prod)
            try:
                assert join == '大面曹天'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def vod_api_downline(self):
        homepage = HomePage(self.driver)
        self.Browser()
        device_id = self.ret_data["retCode"]
        if device_id == 'A0000000':
            retmsg = self.ret_data["retMsg"]
            try:
                assert retmsg == '无对应数据'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Program(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Program_URL = config.get("testServer", "Program_URL")
        logger.info("The test server url is: %s" % Program_URL)
        get_url = urllib.request.urlopen(Program_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_pro = json.loads(Code)
        return self.ret_pro

    def ProgramName(self):
        program = self.ret_pro["retMsg"]["programList"]
        self.programName = re.findall(".*?'programName': '(.*?)'", str(program))[0]
        return self.programName

    def Program_online(self):
        homepage = HomePage(self.driver)
        self.Program()
        device_id = self.ret_pro["retCode"]
        if device_id == '00000000':
            self.ProgramName()
            try:
                assert self.programName == '大面曹天 01'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Program_downline(self):
        homepage = HomePage(self.driver)
        self.Program()
        device_id = self.ret_pro["retCode"]
        if device_id == '00000000':
            self.ProgramName()
            try:
                assert self.programName != '大面曹天 01'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Product(self):
        code_name = open('D:\\code.txt').read()
        Product_URL = 'http://10.3.1.107:8804/vod_api/assetList!getProductList?serviceGroupCode=1100122022055962258270018&packageCodes='
        add = '&pageLimit=200&pageNum=0&isAll=1'
        logger.info("The test server url is: %s" % Product_URL + code_name + add)
        get_url = urllib.request.urlopen(Product_URL + code_name +add).read()
        Code = get_url.decode('utf-8')
        self.ret_Product = json.loads(Code)
        return self.ret_Product

    def Product_downline(self):
        homepage = HomePage(self.driver)
        self.Product()
        device_id = self.ret_Product["retCode"]
        if device_id == '00000000':
            program = self.ret_Product["retMsg"]["listInfo"]
            programName = re.findall(".*?'productName': '(.*?)'", str(program))[0]
            try:
                assert programName == '厉害了我的歌 高清'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Binding_package(self):
        homepage = HomePage(self.driver)
        self.Product()
        device_id = self.ret_Product["retCode"]
        if device_id == '00000000':
            program = self.ret_Product["retMsg"]["listInfo"]
            programName = re.findall(".*?'productName': '(.*?)'", str(program))[1]
            try:
                assert programName == '大话天仙'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Product_No_downline(self):
        homepage = HomePage(self.driver)
        self.Product()
        device_id = self.ret_Product["retCode"]
        if device_id == '00000000':
            program = self.ret_Product["retMsg"]["listInfo"]
            programName = re.findall(".*?'productName': '(.*?)'", str(program))[0]
            try:
                assert programName != '厉害了我的歌 高清'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Tree_state(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Tree_state_URL = config.get("testServer", "Tree_state_URL")
        logger.info("The test server url is: %s" % Tree_state_URL)
        get_url = urllib.request.urlopen(Tree_state_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_tree = json.loads(Code)
        return self.ret_tree


    def Tree_enable(self):
        homepage = HomePage(self.driver)
        self.Tree_state()
        device_id = self.ret_tree["retCode"]
        if device_id == '00000000':
            program = self.ret_tree["retMsg"][1]
            name = re.findall(".*?'name': '(.*?)'", str(program))[0]
            sub = self.ret_tree["retMsg"][2]
            subsection = re.findall(".*?'name': '(.*?)'", str(sub))[0]
            try:
                assert name == '电影' and subsection == '国产大片'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Tree_disable(self):
        homepage = HomePage(self.driver)
        self.Tree_state()
        device_id = self.ret_tree["retCode"]
        if device_id == '00000000':
            program = self.ret_tree["retMsg"][1]
            name = re.findall(".*?'name': '(.*?)'", str(program))[0]
            sub = self.ret_tree["retMsg"][2]
            subsection = re.findall(".*?'name': '(.*?)'", str(sub))[0]
            try:
                assert name == '电视剧' and subsection == '黄金剧场'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Binding_tree(self):
        homepage = HomePage(self.driver)
        self.Tree_state()
        device_id = self.ret_tree["retCode"]
        if device_id == '00000000':
            program = self.ret_tree["retMsg"][3]
            name = re.findall(".*?'packageCodes': '(.*?)'", str(program))[0]
            try:
                assert name == '2100130106012450206570001'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Unbundling_tree(self):
        homepage = HomePage(self.driver)
        self.Tree_state()
        device_id = self.ret_tree["retCode"]
        if device_id == '00000000':
            program = self.ret_tree["retMsg"][3]
            name = re.findall(".*?'packageCodes': '(.*?)'", str(program))[0]
            try:
                assert name == ''
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Add_column_interface(self):
        homepage = HomePage(self.driver)
        self.Tree_state()
        device_id = self.ret_tree["retCode"]
        if device_id == '00000000':
            program = self.ret_tree["retMsg"][4]
            add_name = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_name == '子栏目'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Globa_navigation(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Globa_navigation_URL = config.get("testServer", "Globa_navigation_URL")
        logger.info("The test server url is: %s" % Globa_navigation_URL)
        get_url = urllib.request.urlopen(Globa_navigation_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_m = json.loads(Code)
        return self.ret_m

    def name_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            program = self.ret_m["retMsg"]
            add_name = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_name == details_test
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Re_get(self):
        program = self.ret_m["retMsg"]
        self.add_name = re.findall(".*?'name': '(.*?)'", str(program))[0]
        self.action = re.findall(".*?'action': '(.*?)'", str(program))[0]
        self.serviceType = re.findall(".*?'serviceType': '(.*?)'", str(program))[0]
        return self.add_name,self.action,self.serviceType

    def Vod_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_PROGRAM_LIST' and self.serviceType == 'VOD'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Live_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_LIVEPLAYER' and self.serviceType == 'LIVE'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def App_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_APP' and self.serviceType == 'APP'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Setting_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_SETTINGS' and self.serviceType == 'SETTING'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Favoerite_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_FAVOR' and self.serviceType == 'FAVOERITE'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def History_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_HISTORY' and self.serviceType == 'HISTORY'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def About_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_ABOUT_US' and self.serviceType == 'ABOUT'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Special_index_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.Re_get()
            try:
                assert self.add_name == details_test and self.action == 'OPEN_SPECIAL_INDEX' and self.serviceType == 'SPECIAL_INDEX'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def CategoryCode_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            program = self.ret_m["retMsg"]
            category = re.findall(".*?'categoryCode': '(.*?)'", str(program))[0]
            categoryTree = re.findall(".*?'categoryTreeCode': '(.*?)'", str(program))[0]
            try:
                assert category == '2100050106019587104660053' and categoryTree == '2100050106019587104660053'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Recommend_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            program = self.ret_m["retMsg"]
            recommend = re.findall(".*?'recommendCode': '(.*?)'", str(program))[0]
            try:
                assert recommend == '1100070023874046224810008'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Del_name_interface(self):
        homepage = HomePage(self.driver)
        self.Globa_navigation()
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            program = self.ret_m["retMsg"]
            add_name = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_name != details_test
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Recommended_bit_public(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Recommended_bit_URL = config.get("testServer", "Recommended_bit_URL")
        logger.info("The test server url is: %s" % Recommended_bit_URL)
        get_url = urllib.request.urlopen(Recommended_bit_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_m = json.loads(Code)
        return self.ret_m

    def upMovebtn_interface(self):
        self.Recommended_bit_public()
        program = self.ret_m["retMsg"]['recommendContent']
        self.add_name = re.findall(".*?'name': '(.*?)'", str(program))[3]
        self.idx_num = re.findall(".*?'idx': (.*?),", str(program))[3]
        # return self.add_name,self.idx_num

    def Newly_added_interface(self):
        self.Recommended_bit_public()
        homepage = HomePage(self.driver)
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            program = self.ret_m["retMsg"]['recommendContent']
            self.add_name = re.findall(".*?'name': '(.*?)'", str(program))[3]
            self.idx_num = re.findall(".*?'idx': (.*?),", str(program))[3]
            # self.upMovebtn_interface()
            try:
                assert self.add_name == test_name and self.idx_num == '4'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def delete_inter(self):
        homepage = HomePage(self.driver)
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.upMovebtn_interface()
            try:
                assert self.add_name == '神探夏洛克' and self.idx_num == '4'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def No_nine(self):
        self.Recommended_bit_public()
        program = self.ret_m["retMsg"]['recommendContent']
        self.nine_name = re.findall(".*?'name': '(.*?)'", str(program))[8]
        self.idx_nine = re.findall(".*?'idx': (.*?),", str(program))[8]
        return self.nine_name,self.idx_nine

    def btnMoveTo_interface(self):

        homepage = HomePage(self.driver)
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.No_nine()
            try:
                assert self.nine_name == '神探夏洛克' and self.idx_nine == '9'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Top_interface(self):
        homepage = HomePage(self.driver)
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.No_nine()
            try:
                assert self.nine_name == '微微一笑很倾城 高清' and self.idx_nine == '9'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Shutdown_interface(self):
        homepage = HomePage(self.driver)
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.No_nine()
            try:
                assert self.nine_name == '我是幸运儿 高清' and self.idx_nine == '9'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Edit_inter(self):
        homepage = HomePage(self.driver)
        device_id = self.ret_m["retCode"]
        if device_id == '00000000':
            self.upMovebtn_interface()
            try:
                assert self.add_name == test_name + '（编辑）' and self.idx_num == '4'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def JsEpg5(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        JsEpg5_URL = config.get("testServer", "JSEPG5_URL")
        logger.info("The test server url is: %s" % JsEpg5_URL)
        get_url = urllib.request.urlopen(JsEpg5_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_js = json.loads(Code)
        return self.ret_js

    def Change_name(self):
        program = self.ret_js["retMsg"]['remdList'][0]['remmendList'][0]['contentList']
        self.move_name = re.findall(".*?'name': '(.*?)'", str(program))[0]
        self.move_idx = re.findall(".*?'idx': (.*?),", str(program))[0]
        return self.move_name,self.move_idx

    def JsEpg5_add(self):
        self.JsEpg5()
        homepage = HomePage(self.driver)
        device_id = self.ret_js["retCode"]
        if device_id == '00000000':
            self.Change_name()
            try:
                assert self.move_name == test_name
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def JsEpg5_Move(self):
        self.JsEpg5()
        homepage = HomePage(self.driver)
        device_id = self.ret_js["retCode"]
        if device_id == '00000000':
            self.Change_name()
            try:
                assert self.move_name == '尊严殖民地' and self.move_idx == '0'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def get_four(self):
        program = self.ret_js["retMsg"]['remdList'][0]['remmendList'][0]['contentList']
        self.move_name = re.findall(".*?'name': '(.*?)'", str(program))[2]
        self.move_idx = re.findall(".*?'idx': (.*?),", str(program))[3]
        logger.info(self.move_name,self.move_idx)
        # return self.move_name,self.move_idx

    def Moveto_four(self):
        self.JsEpg5()
        homepage = HomePage(self.driver)
        device_id = self.ret_js["retCode"]
        if device_id == '00000000':
            self.get_four()
            try:
                assert self.move_name == '尊严殖民地' and self.move_idx == '3'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Moveto_top(self):
        self.JsEpg5()
        homepage = HomePage(self.driver)
        device_id = self.ret_js["retCode"]
        if device_id == '00000000':
            self.get_four()
            try:
                assert self.move_name == '从你的全世界路过' and self.move_idx == '3'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def JsEpg5_edit(self):
        self.JsEpg5()
        homepage = HomePage(self.driver)
        device_id = self.ret_js["retCode"]
        if device_id == '00000000':
            self.Change_name()
            try:
                assert self.move_name == test_name + '（编辑）'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def App_recommend(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        App_recommend_URL = config.get("testServer", "App_recommend_URL")
        logger.info("The test server url is: %s" % App_recommend_URL)
        get_url = urllib.request.urlopen(App_recommend_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_app = json.loads(Code)
        return self.ret_app

    def add_app(self):
        self.App_recommend()
        homepage = HomePage(self.driver)
        device_id = self.ret_app["retCode"]
        if device_id == '00000000':
            program = self.ret_app["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to == test_name
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def edit_app(self):
        self.App_recommend()
        homepage = HomePage(self.driver)
        device_id = self.ret_app["retCode"]
        if device_id == '00000000':
            program = self.ret_app["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to == test_name + '（编辑）'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def del_app(self):
        homepage = HomePage(self.driver)
        self.App_recommend()
        device_id = self.ret_app["retCode"]
        if device_id == '00000000':
            retmsg = self.ret_app["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(retmsg))[0]
            try:
                assert add_to == '六月与弓箭'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def User_wallpaper(self):
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        user_wallpaper_URL = config.get("testServer", "user_wallpaper_URL")
        logger.info("The test server url is: %s" % user_wallpaper_URL)
        get_url = urllib.request.urlopen(user_wallpaper_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_wall = json.loads(Code)
        return self.ret_wall

    def add_wallpaper(self):
        self.User_wallpaper()
        homepage = HomePage(self.driver)
        device_id = self.ret_wall["retCode"]
        if device_id == '00000000':
            program = self.ret_wall["retMsg"]['listInfo']
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[6]
            try:
                assert add_to == 'spec.jpg'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Association(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Association_URL = config.get("testServer", "Association_URL")
        logger.info("The test server url is: %s" % Association_URL)
        get_url = urllib.request.urlopen(Association_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)
        # return ret_ass

    def get_need(self):
        program = self.ret_ass["retMsg"]
        self.add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
        self.display = re.findall(".*?'displayIndex': (.*?),", str(program))[0]
        # return add_to,display

    def ass_recommend(self):
        self.Association()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[2]
            # display = re.findall(".*?'displayIndex': (.*?),", str(program))[2]
            try:
                assert add_to == test_name
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def ass_top(self):
        self.Association()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            self.get_need()
            try:
                assert self.add_to == test_name and self.display == '1'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def ass_edit(self):
        self.Association()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            self.get_need()
            try:
                assert self.add_to == test_name+'（编辑）' and self.display == '1'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def ass_delete(self):
        self.Association()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to != test_name
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Order_page(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Order_page_URL = config.get("testServer", "Order_page_URL")
        logger.info("The test server url is: %s" % Order_page_URL)
        get_url = urllib.request.urlopen(Order_page_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    def Order_recommend(self):
        self.Order_page()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[2]
            display = re.findall(".*?'displayIndex': (.*?),", str(program))[2]
            try:
                assert add_to == test_name and display == '3'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Order_top(self):
        self.Order_page()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            self.get_need()
            try:
                assert self.add_to == test_name and self.display == '1'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Order_edit(self):
        self.Order_page()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            self.get_need()
            try:
                assert self.add_to == test_name+'（编辑）' and self.display == '1'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Order_delete(self):
        self.Order_page()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to != test_name
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Bound_business(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Bound_business_URL = config.get("testServer", "Bound_business_URL")
        logger.info("The test server url is: %s" % Bound_business_URL)
        get_url = urllib.request.urlopen(Bound_business_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    def Bound_recommend(self):
        self.Bound_business()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['serviceGroupList']
            add_to = re.findall(".*?'serviceGroupCode': '(.*?)'", str(program))[0]
            try:
                assert add_to == '1100122106019589435850019'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def FJLT_Bound_recommend(self):
        self.Bound_business()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['serviceGroupList']
            add_to = re.findall(".*?'serviceGroupCode': '(.*?)'", str(program))[0]
            try:
                assert add_to == '1100122023874084936460012'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()


    def Task_Upgrade(self):
        mac_name = open('D:\\mac.txt').read()
        Upgrade_task_URL = 'http://10.3.1.107:8802/oms_api/device!deviceUpgrade?mac='+mac_name+'&comboCode=1100121023874101446610014'
        logger.info("The test server url is: %s" % Upgrade_task_URL)
        get_url = urllib.request.urlopen(Upgrade_task_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    # def Task_Upgrade(self):
    #     config = configparser.ConfigParser()
    #     file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
    #     config.read(file_path)
    #     Upgrade_task_URL = config.get("testServer", "Upgrade_task_URL")
    #     logger.info("The test server url is: %s" % Upgrade_task_URL)
    #     get_url = urllib.request.urlopen(Upgrade_task_URL).read()
    #     Code = get_url.decode('utf-8')
    #     self.ret_ass = json.loads(Code)

    def Task_recommend(self):
        self.Task_Upgrade()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['listInfo']
            add_to = re.findall(".*?'versionSeq': '(.*?)'", str(program))[0]
            try:
                assert add_to == '729'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Page_type(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Page_type_URL = config.get("testServer", "Page_type_URL")
        logger.info("The test server url is: %s" % Page_type_URL)
        get_url = urllib.request.urlopen(Page_type_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    def Page_recommend(self):
        self.Page_type()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['listInfo']
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to == 'Wallpaper testing0'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Page_type1(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Page_type_URL1 = config.get("testServer", "Page_type_URL1")
        logger.info("The test server url is: %s" % Page_type_URL1)
        get_url = urllib.request.urlopen(Page_type_URL1).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    def Page_recommend1(self):
        self.Page_type1()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['listInfo']
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to == 'Wallpaper testing1'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def Page_type2(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Page_type_URL2 = config.get("testServer", "Page_type_URL2")
        logger.info("The test server url is: %s" % Page_type_URL2)
        get_url = urllib.request.urlopen(Page_type_URL2).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    def Page_recommend2(self):
        self.Page_type2()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['listInfo']
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to == 'Wallpaper testing2'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def price_tag_wallpaper(self):
        config = configparser.ConfigParser()
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        Tag_wallpaper_URL = config.get("testServer", "Tag_wallpaper_URL")
        logger.info("The test server url is: %s" % Tag_wallpaper_URL)
        get_url = urllib.request.urlopen(Tag_wallpaper_URL).read()
        Code = get_url.decode('utf-8')
        self.ret_ass = json.loads(Code)

    def price_tag_recommend(self):
        self.price_tag_wallpaper()
        homepage = HomePage(self.driver)
        device_id = self.ret_ass["retCode"]
        if device_id == '00000000':
            program = self.ret_ass["retMsg"]['listInfo']
            add_to = re.findall(".*?'name': '(.*?)'", str(program))[0]
            try:
                assert add_to == 'The price tag library test'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def get_corner(self):
        corner = 'http://10.3.1.107:8804/vod_api/assetList!getProductList?serviceGroupCode=1100122106019338200200003&packageCodes=2100130106019335716000073&pageLimit=200&pageNum=0&isAll=1'
        logger.info("The test server url is: %s" % corner)
        get_url = urllib.request.urlopen(corner).read()
        Code = get_url.decode('utf-8')
        self.ret_corner = json.loads(Code)

    def superscript(self):
        self.get_corner()
        homepage = HomePage(self.driver)
        device_id = self.ret_corner["retCode"]
        if device_id == '00000000':
            program = self.ret_corner["retMsg"]['listInfo'][0]['corners'][1]
            try:
                assert program == 'http://images.aliyun.ott.guttv.cibntv.net/efb2813e0e5810798285c3a900ec736c'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def top_left_corner(self):
        self.get_corner()
        homepage = HomePage(self.driver)
        device_id = self.ret_corner["retCode"]
        if device_id == '00000000':
            program = self.ret_corner["retMsg"]['listInfo'][0]['corners'][0]
            try:
                assert program == 'http://images.aliyun.ott.guttv.cibntv.net/10bd8766a2a9cd6ff27161f69fab2851'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def upper_right_corner(self):
        self.get_corner()
        homepage = HomePage(self.driver)
        device_id = self.ret_corner["retCode"]
        if device_id == '00000000':
            program = self.ret_corner["retMsg"]['listInfo'][0]['corners'][1]
            try:
                assert program == 'http://images.aliyun.ott.guttv.cibntv.net/d9d0647a4000fcdeb2e0067596d09659'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def lower_right_corner(self):
        self.get_corner()
        homepage = HomePage(self.driver)
        device_id = self.ret_corner["retCode"]
        if device_id == '00000000':
            program = self.ret_corner["retMsg"]['listInfo'][0]['corners'][2]
            try:
                assert program == 'http://images.aliyun.ott.guttv.cibntv.net/0ea965a3e59e1becda5c654a060f6c7b'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def lower_left_corner(self):
        self.get_corner()
        homepage = HomePage(self.driver)
        device_id = self.ret_corner["retCode"]
        if device_id == '00000000':
            program = self.ret_corner["retMsg"]['listInfo'][0]['corners'][3]
            try:
                assert program == 'http://images.aliyun.ott.guttv.cibntv.net/670788e13bd6c7ab68a6b971ddbd9cd3'
                logger.info('Test pass.')
            except Exception as e:
                logger.info("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()


        # az bms

    def bms_api_getPackagePrice(self):
        homepage = HomePage(self.driver)
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        Package_price_URL = config.get("testServer", "Package_price_URL")
        logger.info("The test server url is: %s" % Package_price_URL)
        get_url = urllib.request.urlopen(Package_price_URL).read()
        Code = get_url.decode('utf-8')
        ret = json.loads(Code)
        device_id = ret["retCode"]
        if device_id == '00000000':
            prod = ret["retInfo"]['priceInfo'][0]['policyName']
            logger.info(prod)
            try:
                assert prod == 'agentzero渠道定价'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def bms_api_getProductPrice(self):
        homepage = HomePage(self.driver)
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        product_price_URL = config.get("testServer", "product_price_URL")
        logger.info("The test server url is: %s" % product_price_URL)
        get_url = urllib.request.urlopen(product_price_URL).read()
        Code = get_url.decode('utf-8')
        ret = json.loads(Code)
        device_id = ret["retCode"]
        if device_id == '00000000':
            prod = ret["retInfo"]['packagePriceList'][0]['pricingList'][0]['policyName']
            logger.info(prod)
            try:
                assert prod == '单片点播10元' or 'agentzero渠道定价'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def bms_api_getPackagesPrices(self):
        homepage = HomePage(self.driver)
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        packages_prices_URL = config.get("testServer", "packages_prices_URL")
        logger.info("The test server url is: %s" % packages_prices_URL)
        get_url = urllib.request.urlopen(packages_prices_URL).read()
        Code = get_url.decode('utf-8')
        ret = json.loads(Code)
        device_id = ret["retCode"]
        if device_id == '00000000':
            prod = ret["retInfo"]['packagePriceList'][0]['pricingList'][0]['policyName']
            logger.info(prod)
            try:
                assert prod == 'agentzero渠道定价'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

    def bms_api_getOrderList(self):
        homepage = HomePage(self.driver)
        config = configparser.ConfigParser()  # 创建一个管理对象
        file_path = os.path.dirname(os.path.abspath('.')) + '/config/config.ini'
        config.read(file_path)
        browser = config.get("browserType", "browserName")
        logger.info("You had select %s browser." % browser)
        OrderList_URL = config.get("testServer", "OrderList_URL")
        logger.info("The test server url is: %s" % OrderList_URL)
        get_url = urllib.request.urlopen(OrderList_URL).read()
        Code = get_url.decode('utf-8')
        ret = json.loads(Code)
        device_id = ret["resultDesc"]
        if device_id == '查询成功':
            prod = ret["resultBody"]['rows'][0]['policyName']
            logger.info(prod)
            try:
                assert prod == 'agentzero渠道定价'
                print('Test pass.')
            except Exception as e:
                print("Test fail.", format(e))
                homepage.get_windows_img()
        else:
            homepage.get_windows_img()

