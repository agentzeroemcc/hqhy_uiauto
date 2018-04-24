#coding:utf-8
import unittest,os,time,HTMLTestRunner

from Vod_Content_management.EpisodesList import VodSearch
from Vod_Content_management.ProgramList import Program
from Vod_Content_management.Distribution import Domain
from Vod_Product_management.Product_pack_list import Product
from Vod_Product_management.Product_list import List
from Vod_Column_management.Column_tree import Column
from Vod_Service_grouping.Business_grouping_list import Business
from Vod_Service_grouping.Distribution_domain import Distribution
from Vod_Recomm_management.Recomm_pool import Recommend
from Vod_Basic_config.Domain_list import DomainList
from Vod_Basic_config.Template_list import Template
from Vod_Basic_config.cp_list import cpList
from Vod_Basic_config.Injection_list import InjectionList
from Oms_Navigation_management.Global_navigation import Global
from Oms_Navigation_management.Recommended_management import Recommend_M
from Oms_Navigation_management.Recommended_bit_layout import Bit
from Oms_Navigation_management.Layout_column_model import Layout
from Oms_Business_combination.Busines_combination import Business_com
from Oms_Business_combination.Terminal_binding import Terninal
from Oms_Business_combination.Terminal_list import TerninalList
from Oms_Business_combination.Upgrade_task import Upgrade
from Oms_Business_combination.Upgrade_details import Upgrade_detail
from Oms_Terminal_management.Terminal_lists import List_terminal
from Oms_Terminal_management.Terminal_manufacturer import Manufacturer
from Oms_Terminal_management.Terminal_model import Model
from Oms_Terminal_management.Chip_manufacturers import Chip
from Oms_Message_management.Message_list import Message
from Oms_Message_management.Message_server_list import Message_server
from Oms_Wallpaper_management.Operating_wallpaper import Operating
from Oms_Wallpaper_management.User_wallpaper_management import User_wallpaper
from Oms_Wallpaper_management.Tag_wallpaper import Price_tag
from Oms_Basic_config.AgentvendorList import Agentvendor
from Oms_Basic_config.AgentvendorTypeList import AgentvendorType
from Oms_Basic_config.System_attribute_management import System_attribute
from Oms_Basic_config.System_attribute_group import System_attribute_group
from Oms_Basic_config.Api_address import api_addres
from Oms_user_rights.User_management import Consumer
from Oms_user_rights.Role_management import Role_manage
from Oms_user_rights.Permission_management import Permission
from Oms_Navigation_management.Application_recommendation import Appication
from Oms_Navigation_management.Association_recommendation import Association
from Oms_Navigation_management.Order_page_recommendation import Order
from Bms_Price_management.PreferentialPolicy import Preferentialpolicy
from Bms_Price_management.PriceConfiguration import Priceconfiguration
from Bms_Channel_management.Channel_Allocation import Channelallocation
from Bms_Channel_management.Channel_Pricing import Channelpricing
from Bms_Channel_management.Commodity_Sorting import CommoditySorting
from Bms_Order_management.OrderList import Orderlist
from Bms_Order_management.OrderFlow import OrderFlow
from Bms_Channel_management.bms_interface import bmsInterface


def suite():
    suites = unittest.TestSuite()

    # # VOD--内容管理--节目集列表
    # suites.addTest(VodSearch('test_Sign_in'))
    # suites.addTest(VodSearch('test_Audit_fail'))
    # suites.addTest(VodSearch('test_Audit_success'))
    # suites.addTest(VodSearch('test_Program_up'))
    # suites.addTest(VodSearch('test_Downline_interface'))   #   下线接口测试
    # suites.addTest(VodSearch('test_Online_interface'))    #   上线接口测试
    # suites.addTest(VodSearch('test_Program_down'))
    # suites.addTest(VodSearch('test_Search'))
    # suites.addTest(VodSearch('test_High_search'))
    # suites.addTest(VodSearch('test_Reset'))
    # # suites.addTest(VodSearch('test_Refresh'))         #刷新
    # suites.addTest(VodSearch('test_Audit_status'))
    # suites.addTest(VodSearch('test_Online_status'))
    # suites.addTest(VodSearch('test_Batch_audit'))
    # suites.addTest(VodSearch('test_Batch_success'))
    # suites.addTest(VodSearch('test_Batch_up'))
    # suites.addTest(VodSearch('test_Batch_offline'))
    # suites.addTest(VodSearch('test_Save_period'))
    # suites.addTest(VodSearch('test_export'))
    #
    # # VOD--内容管理--节目列表
    # suites.addTest(Program('test_Audit_fail'))
    # suites.addTest(Program('test_Audit_success'))
    # suites.addTest(Program('test_Program_up'))
    # suites.addTest(Program('test_Program_down'))
    # suites.addTest(Program('test_online_interface'))  #   节目上线接口测试
    # suites.addTest(Program('test_downline_interface'))   #   节目下线接口测试
    # suites.addTest(Program('test_Delete_program'))
    # suites.addTest(Program('test_Search'))
    # suites.addTest(Program('test_High_search'))
    # suites.addTest(Program('test_Reset'))
    # # suites.addTest(Program('test_Refresh'))           #刷新
    # suites.addTest(Program('test_Audit_status'))
    # suites.addTest(Program('test_Online_status'))
    # suites.addTest(Program('test_Batch_audit'))
    # suites.addTest(Program('test_Batch_up'))
    # suites.addTest(Program('test_Batch_offline'))
    # # suites.addTest(Program('test_Save_period'))       #待测
    #
    # # VOD--内容管理--分发域媒资
    # suites.addTest(Domain('test_Program_up'))
    # suites.addTest(Domain('test_Program_down'))
    # suites.addTest(Domain('test_Search'))
    # suites.addTest(Domain('test_online_interface'))   #    节目上线接口测试
    # suites.addTest(Domain('test_downline_interface'))   #   节目下线接口测试
    #
    # # VOD--产品管理--产品包列表
    # suites.addTest(Product('test_Newly_added'))  #新增产品包打包时间
    # suites.addTest(Product('test_Product_up'))
    # suites.addTest(Product('test_Product_down'))
    # suites.addTest(Product('test_Special_poster'))
    # suites.addTest(Product('test_delete'))
    # suites.addTest(Product('test_Search'))
    # suites.addTest(Product('test_Reset'))
    # suites.addTest(Product('test_Sheet_export'))
    # suites.addTest(Product('test_Online_status'))
    # suites.addTest(Product('test_package_copy'))    #    产品包复制
    # suites.addTest(Product('test_package_interface'))    #   产品包接口测试   (在栏目树加入产品包时确保江苏移动在第十个，否则要修改359行，在展开记录片时要保证其在第二行，多一行tr+6，修改362行)
    # suites.addTest(Product('test_Product_interface'))   #    产品加入产品包接口测试
    # suites.addTest(Product('test_Corner'))   #    角标测试
    #
    # # VOD--产品管理--产品列表
    # suites.addTest(List('test_Search'))
    # suites.addTest(List('test_Reset'))
    # suites.addTest(List('test_Online_status'))
    # # suites.addTest(List('test_Es'))
    # suites.addTest(List('test_Edit'))
    # suites.addTest(List('test_Add_package'))
    #
    # # VOD--栏目管理--栏目树
    # suites.addTest(Column('test_New_tree'))
    # suites.addTest(Column('test_Start_stop'))
    # suites.addTest(Column('test_Detailed'))
    # suites.addTest(Column('test_Delete'))
    # suites.addTest(Column('test_Sheet_export'))
    # suites.addTest(Column('test_tree_state_interface'))   #   栏目树状态接口测试
    # suites.addTest(Column('test_package_binding_tree'))   #   产品包绑定栏目树接口测试

    #VOD--业务分组--业务分组列表
    # suites.addTest(Business('test_New_service'))
    # suites.addTest(Business('test_Search'))
    # suites.addTest(Business('test_Start_stop'))
    # suites.addTest(Business('test_Edit'))
    # suites.addTest(Business('test_Sheet_export'))
    # suites.addTest(Business('test_Column_details'))
    # suites.addTest(Business('test_Delete'))
    # suites.addTest(Business('test_Preview_confirmation'))
    # suites.addTest(Business('test_Display_record'))   #  显示记录判断
    # suites.addTest(Business('test_View_blacklist'))
    # suites.addTest(Business('test_business_interface'))     #   业务分组产品包绑定栏目树测试
    # suites.addTest(Business('test_add_column'))     #   添加栏目接口测试
    # suites.addTest(Business('test_Corner'))     #   添加栏目接口测试：角标

    # # VOD--业务分组--分发域绑定
    # suites.addTest(Distribution('test_New_service'))
    # suites.addTest(Distribution('test_Priority_up'))
    # suites.addTest(Distribution('test_Unbound'))
    #
    # # VOD--推荐池管理--推荐池
    # suites.addTest(Recommend('test_Recomm_pool'))
    # suites.addTest(Recommend('test_Recomm_search'))
    # suites.addTest(Recommend('test_Editorial_recomm'))
    # suites.addTest(Recommend('test_Delete_recomm'))
    #
    # # VOD--基础配置--分发域列表
    # suites.addTest(DomainList('test_Newly_added'))  #  在操作之前查看记录是否有12条，如记录不是12条需修改部分代码，行数（40,97,98,114,116,121,136,203），只需将tr[13]中的数字换成记录数+1
    # suites.addTest(DomainList('test_Disable'))
    # suites.addTest(DomainList('test_Enable'))
    # suites.addTest(DomainList('test_synchronization'))
    # suites.addTest(DomainList('test_edit'))
    # suites.addTest(DomainList('test_Template_list'))#显示模板列表
    # suites.addTest(DomainList('test_delete'))
    #
    # # VOD--基础配置--模板列表
    # suites.addTest(Template('test_Newly_added'))
    # suites.addTest(Template('test_edit'))
    # suites.addTest(Template('test_delete'))
    #
    # # VOD--基础配置--CP列表
    # suites.addTest(cpList('test_Newly_added'))
    # suites.addTest(cpList('test_search'))
    # suites.addTest(cpList('test_Enable'))
    # suites.addTest(cpList('test_Disable'))
    # suites.addTest(cpList('test_edit'))
    # suites.addTest(cpList('test_delete'))
    #
    # # VOD--基础配置--注入域列表
    # suites.addTest(InjectionList('test_Newly_added'))
    # suites.addTest(InjectionList('test_edit'))
    # suites.addTest(InjectionList('test_delete'))
    # # suites.addTest(InjectionList('test_Task_query'))   #  任务查询  （有bug）

    # OMS--导航管理--全局导航
    suites.addTest(Global('test_Add_to'))
    suites.addTest(Global('test_search'))
    suites.addTest(Global('test_edit'))
    suites.addTest(Global('test_delete'))
    suites.addTest(Global('test_details'))  #  全局导航详情测试 + 接口测试

    # # OMS--导航管理--推荐位管理
    suites.addTest(Recommend_M('test_New_add'))
    suites.addTest(Recommend_M('test_Search'))
    suites.addTest(Recommend_M('test_Status'))
    suites.addTest(Recommend_M('test_Edit'))
    suites.addTest(Recommend_M('test_Details'))
    suites.addTest(Recommend_M('test_New_search'))
    suites.addTest(Recommend_M('test_New_collection'))
    suites.addTest(Recommend_M('test_New_history'))
    suites.addTest(Recommend_M('test_New_center'))
    suites.addTest(Recommend_M('test_New_Setting'))
    suites.addTest(Recommend_M('test_New_vod_Package'))
    suites.addTest(Recommend_M('test_New_Vod_Product'))
    suites.addTest(Recommend_M('test_New_Special'))
    suites.addTest(Recommend_M('test_New_Column'))
    suites.addTest(Recommend_M('test_Child_state'))
    suites.addTest(Recommend_M('test_Child_edit'))
    suites.addTest(Recommend_M('test_Child_delete'))
    suites.addTest(Recommend_M('test_Child_search'))
    suites.addTest(Recommend_M('test_Move'))
    suites.addTest(Recommend_M('test_Top'))
    suites.addTest(Recommend_M('test_Upmove'))
    suites.addTest(Recommend_M('test_Recommendation'))
    suites.addTest(Recommend_M('test_Delete'))
    suites.addTest(Recommend_M('test_Recommended_bit_interface'))   #  福建联通推荐位接口测试
    #suites.addTest(Recommend_M('test_Recommended_JsEpg5'))   #    江苏移动EPG5.0推荐位接口测试

    # OMS--导航管理--推荐位布局
    suites.addTest(Bit('test_New_add'))
    suites.addTest(Bit('test_Status'))
    suites.addTest(Bit('test_edit'))
    suites.addTest(Bit('test_Detail'))
    suites.addTest(Bit('test_Detail_append'))
    suites.addTest(Bit('test_Detail_edit'))
    suites.addTest(Bit('test_Detail_preview'))
    suites.addTest(Bit('test_Detail_delete'))
    suites.addTest(Bit('test_Detail_deleteall'))
    suites.addTest(Bit('test_Detail_deletebatch'))
    suites.addTest(Bit('test_Delete'))
    suites.addTest(Bit('test_Delete_batch'))

    # OMS--导航管理--布局列模式
    suites.addTest(Layout('test_New_add'))
    suites.addTest(Layout('test_Status'))
    suites.addTest(Layout('test_edit'))
    suites.addTest(Layout('test_Delete'))
    suites.addTest(Layout('test_Delete_batch'))

    #OMS--导航管理--打开应用推荐
    suites.addTest(Appication('test_New_add'))
    suites.addTest(Appication('test_top'))  #   应用推荐添加接口测试
    suites.addTest(Appication('test_search_app'))
    suites.addTest(Appication('test_app_edit'))    #    应用推荐编辑接口
    suites.addTest(Appication('test_bottom'))
    suites.addTest(Appication('test_del_app'))   #  删除接口测试

    #OMS--导航管理--关联推荐--搜索热门推荐
    suites.addTest(Association('test_New_add'))      #  新添加关联推荐接口
    suites.addTest(Association('test_top'))      #   置顶接口测试
    suites.addTest(Association('test_edit'))    #   编辑接口测试
    suites.addTest(Association('test_delete'))    #    删除接口测试

    # OMS--导航管理--关联推荐--订购页面推荐
    suites.addTest(Order('test_New_add'))
    suites.addTest(Order('test_top'))
    suites.addTest(Order('test_edit'))
    suites.addTest(Order('test_delete'))

    # OMS--业务组合--业务组合
    suites.addTest(Business_com('test_Newly_added'))
    suites.addTest(Business_com('test_search'))
    suites.addTest(Business_com('test_Enable'))
    suites.addTest(Business_com('test_disable'))
    suites.addTest(Business_com('test_edit'))
    suites.addTest(Business_com('test_Bound_service'))
    suites.addTest(Business_com('test_Bound_Navigation'))
    suites.addTest(Business_com('test_Navigation_details'))
    suites.addTest(Business_com('test_delete'))
    suites.addTest(Business_com('test_fjlt_interface'))   #福建联通绑定业务分组接口测试
    suites.addTest(Business_com('test_paging'))
    suites.addTest(Business_com('test_column_operation'))

    # OMS--业务组合--终端绑定
    suites.addTest(Terninal('test_Newly_added'))
    suites.addTest(Terninal('test_Enable_disable'))
    suites.addTest(Terninal('test_Edit'))
    suites.addTest(Terninal('test_Handoff_service'))
    suites.addTest(Terninal('test_Unbound'))
    suites.addTest(Terninal('test_reset'))

    # OMS--业务组合--终端列表
    suites.addTest(TerninalList('test_search'))
    suites.addTest(TerninalList('test_enable_disable'))
    suites.addTest(TerninalList('test_Handoff_service'))
    suites.addTest(TerninalList('test_Unbound'))
    suites.addTest(TerninalList('test_Reset'))

    # OMS--业务组合--升级任务
    suites.addTest(Upgrade('test_Newly_added'))
    suites.addTest(Upgrade('test_enable'))
    suites.addTest(Upgrade('test_disable'))
    suites.addTest(Upgrade('test_edit'))
    suites.addTest(Upgrade('test_delete'))

    # OMS--业务组合--升级详情
    suites.addTest(Upgrade_detail('test_search'))
    suites.addTest(Upgrade_detail('test_Reset'))

    # OMS--终端管理--终端列表
    suites.addTest(List_terminal('test_search'))
    suites.addTest(List_terminal('test_Reset'))
    suites.addTest(List_terminal('test_Advanced_search'))

    # OMS--终端管理--终端厂商列表
    # suites.addTest(Manufacturer('test_Newly_added'))      #  只能加不能删，启用时请慎重考虑
    suites.addTest(Manufacturer('test_search'))
    suites.addTest(Manufacturer('test_edit'))

    # OMS--终端管理--终端型号列表
    # suites.addTest(Model('test_Newly_added'))     #  只能加不能删，启用时请慎重考虑
    suites.addTest(Model('test_search'))
    suites.addTest(Model('test_edit'))

    # OMS--终端管理--芯片厂商列表
    # suites.addTest(Chip('test_Newly_added'))     #  只能加不能删，启用时请慎重考虑
    suites.addTest(Chip('test_search'))
    suites.addTest(Chip('test_edit'))

    # OMS--消息管理--消息列表
    suites.addTest(Message('test_Newly_added'))
    suites.addTest(Message('test_edit'))
    suites.addTest(Message('test_search'))
    suites.addTest(Message('test_To_examine'))
    suites.addTest(Message('test_Message_preview'))
    suites.addTest(Message('test_details'))
    suites.addTest(Message('test_delete'))

    # OMS--消息管理--消息服务器列表
    suites.addTest(Message_server('test_Newly_added'))
    suites.addTest(Message_server('test_edit'))
    suites.addTest(Message_server('test_Start_stop'))
    suites.addTest(Message_server('test_batch_stop'))
    suites.addTest(Message_server('test_batch_start'))
    suites.addTest(Message_server('test_delete'))

    # OMS--壁纸管理--运营壁纸管理
    suites.addTest(Operating('test_Newly_added'))
    suites.addTest(Operating('test_search'))   #   选择页面类型接口
    suites.addTest(Operating('test_edit'))
    suites.addTest(Operating('test_delete'))

    # OMS--壁纸管理--用户壁纸库管理
    suites.addTest(User_wallpaper('test_Upload_wallpaper'))   #新增用户壁纸接口测试  跑接口是保证有6张壁纸
    suites.addTest(User_wallpaper('test_search'))
    suites.addTest(User_wallpaper('test_delete'))

    # OMS--壁纸管理--价签壁纸库管理
    suites.addTest(Price_tag('test_Newly_added'))
    suites.addTest(Price_tag('test_edit'))
    suites.addTest(Price_tag('test_Business_selection'))
    suites.addTest(Price_tag('test_delete'))

    # oms--用户权限--用户管理
    suites.addTest(Consumer('test_Add_to'))
    suites.addTest(Consumer('test_search'))
    suites.addTest(Consumer('test_edit'))
    suites.addTest(Consumer('test_see'))
    suites.addTest(Consumer('test_delete'))
    suites.addTest(Consumer('test_Reset'))

    # oms--用户权限--角色管理
    suites.addTest(Role_manage('test_Add_to'))
    suites.addTest(Role_manage('test_search'))
    suites.addTest(Role_manage('test_edit'))
    suites.addTest(Role_manage('test_distribution'))
    suites.addTest(Role_manage('test_delete'))
    suites.addTest(Role_manage('test_Reset'))

    # oms--用户权限--权限管理
    suites.addTest(Permission('test_Newly_build'))
    suites.addTest(Permission('test_search'))
    suites.addTest(Permission('test_edit'))
    suites.addTest(Permission('test_delete'))
    suites.addTest(Permission('test_Reset'))

    # oms--基础配置--渠道商列表
    suites.addTest(Agentvendor('test_Add_to'))
    suites.addTest(Agentvendor('test_search'))
    suites.addTest(Agentvendor('test_edit'))
    suites.addTest(Agentvendor('test_delete'))

    # oms--基础配置--渠道商类型列表
    suites.addTest(AgentvendorType('test_Add_to'))
    suites.addTest(AgentvendorType('test_edit'))
    suites.addTest(AgentvendorType('test_delete'))

    # oms--基础配置--系统属性管理
    suites.addTest(System_attribute('test_Add_to'))
    suites.addTest(System_attribute('test_search'))
    suites.addTest(System_attribute('test_edit'))
    suites.addTest(System_attribute('test_synchronization'))
    suites.addTest(System_attribute('test_delete'))

    # oms--基础配置--系统属性组管理
    # # suites.addTest(System_attribute_group('test_Add_to'))   #    新增无删除，请谨慎操作

    # oms--基础配置--api地址管理
    suites.addTest(api_addres('test_Add_to'))
    suites.addTest(api_addres('test_edit'))
    suites.addTest(api_addres('test_delete'))

    # # BMS 价签管理 价签配置
    # suites.addTest(Priceconfiguration('test_Newly_added'))
    # suites.addTest(Priceconfiguration('test_search'))
    # # suites.addTest(Priceconfiguration('test_edit'))
    # suites.addTest(Priceconfiguration('test_delete'))

    # # BMS 价签管理 优惠策略
    # suites.addTest(Preferentialpolicy('test_Newly_added'))
    # suites.addTest(Preferentialpolicy('test_search'))
    # suites.addTest(Preferentialpolicy('test_edit'))
    # suites.addTest(Preferentialpolicy('test_delete'))

    # # BMS 渠道管理  渠道策略配置
    # suites.addTest(Channelallocation('test_Newly_added'))
    # suites.addTest(Channelallocation('test_search'))
    # suites.addTest(Channelallocation('test_edit'))
    # suites.addTest(Channelallocation('test_delete'))

    # # BMS 渠道管理  渠道定价
    # suites.addTest(Channelpricing('test_channel'))
    # # suites.addTest(Channelpricing('test_delete')) # 因为下面的商品定价排序需要渠道定价的信息 所以批量删除可以选择性执行

    # # BMS 渠道管理  商品定价排序
    # suites.addTest(CommoditySorting('test_commodity'))

    # # # BMS 订单管理  订单列表
    # suites.addTest(Orderlist('test_Orderlist'))

    # # BMS 订单管理  订购流水
    # suites.addTest(OrderFlow('test_orderflow'))

    # # bms_interface
    # suites.addTest(bmsInterface('test_bms'))

    return suites
# suite = unittest.TestSuite(unittest.makeSuite(Domain))
if __name__ == '__main__':
    report_path = os.path.dirname(os.path.abspath('.')) + '/test_report/'
    now = time.strftime("%Y-%m-%d-%H-%M-%S", time.localtime(time.time()))
    filename = report_path + now + "result.html"
    fp = open(filename, "wb")
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp, title='测试报告', description='用例执行情况：')
    # 执行测试用例
    runner.run(suite())
    fp.close()