# coding=utf-8
from framework.base_page import BasePage

class HomePage(BasePage):
    input_usr = "id=>username"
    input_pas = "id=>password"
    fm1 = "xpath=>//*[@id='fm1']/div[7]/div/button"#登录
    search_Con = "xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[2]/a"#点击内容管理
    search_submit_btn = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a[1]/i'#编辑按钮
    add_edit = 'xpath=>//*[@id="edit_name"]'#编辑名称
    deter = "selector_selector=>div.col-sm-offset.text-center > button.btn.btn-info"#编辑确定
    b_deter = "selector_selector=>html body div.bootbox.modal.fade.in div.modal-dialog div.modal-content div.modal-footer button.btn.btn-success"# 点击编辑确定
    tab_1 = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[3]'# 匹配编辑后的待审核名称
    tab_input = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[1]/input'# 点击对勾
    tab_input1 = 'xpath=>//*[@id="table"]/tbody/tr[2]/td[1]/input'# 点击对勾
    check_1 = 'xpath=>//*[@id="check"]'# 点击审核
    check_series = 'xpath=>//*[@id="check_series_form"]/div[3]/div/button[1]'#节目集审核按钮
    check_program = 'xpath=>//*[@id="check_program_form"]/div[3]/div/button[1]'#节目审核按钮
    but_1 = "xpath=>/html/body/div[7]/div/div/div[3]/button"#节目确定按钮
    but_2 = "xpath=>/html/body/div[9]/div/div/div[3]/button"#节目确定按钮
    search = 'xpath=>//*[@id="searchBtn"]'#点击搜索按钮弹出搜索框
    add_name = 'xpath=>//*[@id="name"]'#输入搜索名称
    search_B = 'xpath=>//*[@id="searchByName"]'  # 点击搜索开始搜索
    search_R = 'xpath=>//*[@id="searchReset"]'#重置

    tab_2 = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a[3]/i'    # 点击上/下线按钮
    offline_series = 'xpath=>//*[@id="offline_series_form"]/div[3]/div/button[1]'        # 点击下线原因‘确定’
    search_D = "xpath=>//*[@id='searchDiv']/div/label[3]/div/button/span[1]"       #点击CP按钮
    search_D_input = "xpath=>//*[@id='searchDiv']/div/label[3]/div/div/div/input"        #输入CP名称
    search_M = 'xpath=>//*[@id="searchMore"]'        # 高级搜索
    series_N = 'xpath=>//*[@id="seriesName"]'         # 输入节目集名称
    cp_xlk = 'xpath=>//*[@id="search_series_form"]/div[2]/div/div/button/span[1]'       # 点击cp下拉框
    hq_cp_name = 'xpath=>//*[@id="search_series_form"]/div[2]/div/div/div/div/input'       # 获取cp名称
    dj_xd = 'xpath=>//*[@id="search_series_form"]/div[2]/div/div/div/ul/li[221]/a'        # 点击选定项
    fl_one = 'xpath=>//*[@id="programType"]'        # 输入一级分类
    fl_two = 'xpath=>//*[@id="programType2"]'        # 输入二级分类
    dj_seach = 'xpath=>//*[@id="searchByMore"]'        # 点击搜索
    dj_shuax = 'xpath=>//*[@id="refreshBtn"]'         # 点击刷新
    on_line = 'xpath=>//*[@id="online"]'         # 上线按钮
    qd_ann = 'xpath=>//*[@id="online_series_form"]/div[2]/div/button[1]'         # 点击确定按钮
    off_line = 'xpath=>//*[@id="offline"]'         # 下线按钮
    del_num = 'xpath=>//*[@id="stage_2100020062943265254092760"]'         # 期数
    ji_num = 'xpath=>//*[@id="volumn_2100020062943265254092760"]'         # 分集数
    btnSave = 'xpath=>//*[@id="btnSaveVolumn"]'         #点击保存按钮
    qs_ann = 'xpath=>/html/body/div[8]/div/div/div[3]/button'         #保存期数确定按钮
    collapseO = 'xpath=>//*[@id="collapseOne"]/div/ul/li[2]/a'         #节目列表按钮
    dj_jmj = 'xpath=>//*[@id="collapseOne"]/div/ul/li[1]/a'         #点击节目集列表
    dj_sxx = 'xpath=>//*[@id="table"]/tbody/tr/td[2]/a[3]/i'         #点击上/下线按钮
    offline_program = 'xpath=>//*[@id="offline_program_form"]/div[3]/div/button[1]'         #点击下线确定
    sc_ann = 'xpath=>//*[@id="deleteProgram"]'         #点击删除按钮
    series_C = 'xpath=>//*[@id="seriesCode"]'         #节目集code
    cp_dj = 'xpath=>//*[@id="searchDiv"]/div/label[5]/div/button/span[1]'         #
    cp_sr = 'xpath=>//*[@id="searchDiv"]/div/label[5]/div/div/div/input'         #
    gj_jm = 'xpath=>//*[@id="programName"]'         #高级搜索节目名称
    gj_jmj = 'xpath=>//*[@id="programSeriesName"]'         #高级搜索节目集名称
    dj_cpk = 'xpath=>//*[@id="search_program_form"]/div[3]/div/div/button/span[1]'         #点击CP框
    sr_cpnr = 'xpath=>//*[@id="search_program_form"]/div[3]/div/div/div/div/input'         #输入CP内容
    dj_ffy = 'xpath=>//*[@id="collapseOne"]/div/ul/li[3]/a'         #分发域媒资按钮
    ffy_sx_qd = 'xpath=>/html/body/div[5]/div/div/div[3]/button'         #分发域上线确定按钮

    dj_cp_gl ='xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[4]/a'   #产品管理
    custom ='xpath=>//*[@id="custom-toolbar"]/div/button[1]'   #新增按钮
    customT ='xpath=>//*[@id="custom-toolbar"]/div/button'
    sr_mc ='xpath=>//*[@id="create_package_form"]/div[1]/div/input'   #产品包创建--名称
    sr_zs_mc ='xpath=>//*[@id="create_package_form"]/div[2]/div/input'   #产品包创建--展示名称
    xz_cp ='xpath=>//*[@id="create_package_form"]/div[3]/div/div/div[2]/button'   #产品包创建--选择产品
    cp_mc ='xpath=>//*[@id="productName"]'   #产品包-产品管理-输入产品名称
    sr_cp_mc = 'xpath=>//*[@id="product_dialog"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/label[2]/div/button/span[1]'   #产品包-产品管理-点击cp
    sr_cp_mingc = 'xpath=>//*[@id="product_dialog"]/div/div/div[2]/div[1]/div[1]/div[1]/div[2]/label[2]/div/div/div/input'   #产品包-产品管理-输入CP
    dj_dg = 'xpath=>//*[@id="unSelectedProductTable"]/tbody/tr/td[1]/input'   #产品包-产品管理-点击对勾
    click_dg = 'xpath=>//*[@id="selectedProductTable"]/tbody/tr/td[1]/input'   #产品包-产品管理-点击对勾
    pd_add = 'xpath=>//*[@id="productAdd"]'   #产品包-产品管理-右箭头
    pd_Remove = 'xpath=>//*[@id="productRemove"]'   #产品包-产品管理-左箭头
    pd_dia = 'xpath=>//*[@id="product_dialog"]/div/div/div[2]/div[1]/div[1]/div[2]/div[8]/button'   #产品包-产品管理-清楚筛选
    btn = 'xpath=>//*[@id="btnSave"]'   #产品包-产品管理-清楚筛选
    btn_c = 'xpath=>//*[@id="btnCreatePkg"]'   #产品包-产品管理-保存按钮
    confirm = 'xpath=>/html/body/div[6]/div/div/div[3]/button'   #产品包-产品管理-确认按钮
    pk_name = 'xpath=>//*[@id="package_name"]'   #编辑产品包名称
    edit_pac = 'xpath=>//*[@id="edit_package_form"]/div[10]/div/button[1]'   #产品包保存
    edit_p = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a[2]/i'   #编辑按钮
    del_an = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a[4]/i'   #删除按钮
    dc_sj = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a[6]/i'   #数据导出

    jc_pz = 'xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[8]/a'   #基础配置
    coll = 'xpath=>//*[@id="collapseThree"]/div/ul/li[6]/a'   #任务查询
    online_program = 'xpath=>//*[@id="online_program_form"]/div[2]/div/button[1]'   #任务查询
    collapse = 'xpath=>//*[@id="collapseOne"]/div/ul/li/a'   #产品列表
    product_N = 'xpath=>//*[@id="product_name"]'   #产品名称
    edit_product_f = 'xpath=>//*[@id="edit_product_form"]/div[5]/div/button[1]'   #保存按钮
    s_Pkg = 'xpath=>//*[@id="s_PkgName"]'   #产品包名称
    s_PkgC = 'xpath=>//*[@id="s_PkgCode"]'   #产品包CODE
    s_Btn = 'xpath=>//*[@id="s_BtnSearch"]'   #产品包搜索
    unbind = 'xpath=>//*[@id="UnbindPkgTable"]/tbody/tr/td[1]/input'   #对勾
    add_package = 'xpath=>//*[@id="add_package_dialog"]/div/div/div[2]/div[1]/div[2]/button[1]'   #导入箭头
    package_span = 'xpath=>//*[@id="add_package_dialog"]/div/div/div[1]/button/span'   #X按钮
    searchBy = 'xpath=>//*[@id="searchByContentName"]'   #搜索
    glyphicon = 'xpath=>//*[@id="table"]/tbody/tr/td[2]/a[2]/i'   #编辑

    column = 'xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[5]/a'   #栏目管理
    tree = 'xpath=>//*[@id="treeAdd"]'   #新建栏目树
    manage = 'xpath=>//*[@id="managename"]'   #栏目管理名称
    descrip = 'xpath=>//*[@id="description"]'   #栏目描述信息
    btnCreate = 'xpath=>//*[@id="btnCreateTree"]'   #新建按钮
    btnStart = 'xpath=>//*[@id="btnStartup"]'   #启用
    btnStart1 = 'xpath=>//*[@id="btnShutdown"]'   #停用
    tab_D = 'xpath=>//*[@id="table"]/tbody/tr[2]/td[2]/a[2]/i'   #详细
    category = 'xpath=>//*[@id="categoryRoot"]/tbody/tr/td[4]/a[1]/i'   #推荐位绑定
    selector = 'xpath=>//*[@id="selectorTable"]/tbody/tr[1]/td[1]/input'   #推荐位选择
    btn_S = 'xpath=>//*[@id="btnSelected"]'   #推荐位确认
    category_R = 'xpath=>//*[@id="categoryRoot"]/tbody/tr/td[4]/a[2]/i'   #删除推荐位
    category_Ro = 'xpath=>//*[@id="categoryRoot"]/tbody/tr/td[6]/a/i'   #添加子栏目
    html = 'xpath=>/html/body/div[3]/div/div[2]/table/tbody/tr[2]/td[5]/a/i'   #产品包数量
    packageSearch = 'xpath=>//*[@id="packageSearchText"]'   #产品包名称
    btnPkg = 'xpath=>//*[@id="btnPkgSearch"]'   #搜索
    libPkg = 'xpath=>//*[@id="libPkgTable"]/tbody/tr[1]/td[1]/input'   #点击对勾
    bind = 'xpath=>//*[@id="bindProduct"]'   #确认
    category1 = 'xpath=>//*[@id="categoryRoot"]/tbody/tr[1]/td[6]/a/i'   #二次添加子栏目
    category2 = 'xpath=>//*[@id="categoryRoot"]/tbody/tr[3]/td[2]/a/i'   #位置上移
    category3 = 'xpath=>//*[@id="categoryRoot"]/tbody/tr[2]/td[4]/a[2]/i'   #删除推荐位
    category4 = 'xpath=>//*[@id="categoryRoot"]/tbody/tr[2]/td[4]/a[1]/i'   #添加推荐位

    clean = 'xpath=>//*[@id="cleanProduct"]'   #清空产品包
    product = 'xpath=>//*[@id="productPkg"]/div/div/div[2]/div[2]/button[1]'   #关闭产品包
    category5 = 'xpath=>//*[@id="categoryRoot"]/tbody/tr[2]/td[6]/a[1]/i'   #编辑产品包
    btnSave_t = 'xpath=>//*[@id="btnSaveTree"]'   #编辑保存
    html2 = 'xpath=>/html/body/div[3]/div/div[2]/table/tbody/tr[2]/td[6]/a[3]/i'   #添加子栏目
    tree_R = 'xpath=>//*[@id="treeRemove"]'   #删除栏目树
    btn_C = 'xpath=>//*[@id="btnCreate"]'   #新建
    service = 'xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[6]/a'   #业务分组
    custom1 = 'xpath=>//*[@id="custom-toolbar"]/div/button[2]'   #启用
    custom2 = 'xpath=>//*[@id="custom-toolbar"]/div/button[3]'   #停用
    search_T = 'xpath=>//*[@id="searchText"]'   #搜索框
    table_I = 'xpath=>//*[@id="table"]/tbody/tr/td[1]/input'   #点击对勾
    table_B = 'xpath=>//*[@id="table"]/tbody/tr/td[2]/a[1]/i'   #编辑
    custom_B = 'xpath=>//*[@id="custom-toolbar"]/div/button[6]'   #搜索
    body_r = 'xpath=>//*[@id="body_right"]/form/div[1]/button[2]'   #解除绑定
    pkgStyle = 'xpath=>//*[@id="pkgStyleSearchText"]'   #产品名称
    heart = 'xpath=>//*[@id="heartPackage"]/div/div/div[2]/div[2]/button[1]'   #关闭
    export = 'xpath=>//*[@id="exportBtn"]'   #片单导出
    body = 'xpath=>//*[@id="body_right"]/div[2]/ul/li[2]/a'   #渠道商
    body1 = 'xpath=>//*[@id="body_right"]/div[2]/ul/li[3]/a'   #栏目
    body2 = 'xpath=>//*[@id="body_right"]/div[2]/ul/li[4]/a'   #分发域
    prd = 'xpath=>//*[@id="prdName"]'   #输入框
    domain = 'xpath=>//*[@id="domain_form"]/div[2]/div/button[1]'   #绑定
    recomm = 'xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[7]/a'   #推荐池管理
    add = 'xpath=>//*[@id="add"]'   #新增
    productT = 'xpath=>//*[@id="productTable"]/tbody/tr/td[1]/input'
    btnA = 'xpath=>//*[@id="btnAppend"]'   #添加
    pool = 'xpath=>//*[@id="poolSearchName"]'   #搜索框
    frmRecommend = 'xpath=>//*[@id="frmRecommendItemDoc"]/div[8]/button[2]'   #更新
    collapse_t = 'xpath=>//*[@id="collapseThree"]/div/ul/li[1]/a'
    interface = 'xpath=>//*[@id="interfaceURL"]'   #分发域接口地址
    cms = 'xpath=>//*[@id="cmsID"]'   #本层节点编号
    sop = 'xpath=>//*[@id="sopID"]'   #下层节点编号
    priority = 'xpath=>//*[@id="priority"]'   #优先级
    table_10 = 'xpath=>//*[@id="table"]/tbody/tr[10]/td[1]/input'
    # table_10 = 'xpath=>//*[@id="table"]/tbody/tr[9]/td[1]/input'
    custom4 = 'xpath=>//*[@id="custom-toolbar"]/div/button[4]'   #同步
    i_table = 'xpath=>//*[@id="table"]/tbody/tr[10]/td[2]/a[1]/i'   #编辑
    i_table_3 = 'xpath=>//*[@id="table"]/tbody/tr[10]/td[2]/a[3]/i'   #模板列表
    create = 'xpath=>//*[@id="create_template_form"]/div[6]/div/button[1]'   #模板列表
    template = 'xpath=>//*[@id="templateTable"]/tbody/tr/td[2]/a[1]/i'   #
    template2 = 'xpath=>//*[@id="templateTable"]/tbody/tr/td[2]/a[2]/i'   #
    edit_tem = 'xpath=>//*[@id="edit_template_form"]/div[6]/div/button[1]'   #
    show_domainTemplate = 'xpath=>//*[@id="show_domainTemplate_dialog"]/div/div/div/div[2]/div/button'   #关闭
    tab_del = 'xpath=>//*[@id="table"]/tbody/tr[10]/td[2]/a[2]/i'   #删除按钮
    collaps = 'xpath=>//*[@id="collapseThree"]/div/ul/li[2]/a'   #
    template_N = 'xpath=>//*[@id="templateName"]'   #文件名称
    e_table = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a/i'   #编辑
    templateFile = 'xpath=>//*[@id="templateFileSubmit"]'   #保存
    deleteTemplate = 'xpath=>//*[@id="deleteTemplateFileBtn"]'   #删除
    cp_collapse = 'xpath=>//*[@id="collapseThree"]/div/ul/li[4]/a'   #cp列表
    new_custom = 'xpath=>//*[@id="custom-toolbar"]/div/div[1]/div/a'   #新增
    frm = 'xpath=>//*[@id="frmCP"]/div[1]/div/input'   #CP名称
    code = 'xpath=>//*[@id="code"]'   #cp编码
    startD = 'xpath=>//*[@id="startDate"]/span/span'
    endD = 'xpath=>//*[@id="endDate"]/span/span'
    btnAdd = 'xpath=>//*[@id="btnAdd"]'
    cpName = 'xpath=>//*[@id="cpName"]'
    btnS = 'xpath=>//*[@id="btnSearch"]'
    btnUp = 'xpath=>//*[@id="btnUp"]'
    btnDown = 'xpath=>//*[@id="btnDown"]'
    dj_edit = 'xpath=>//*[@id="table"]/tbody/tr/td[2]/a/i'
    btnUpdate = 'xpath=>//*[@id="btnUpdate"]'
    custom_del = 'xpath=>//*[@id="custom-toolbar"]/div/div[4]/div/button'
    domaininjection = 'xpath=>//*[@id="domaininjection_form"]/div[9]/div/button[1]'
    edit_package = 'xpath=>//*[@id="edit_package_tag"]'
    custom_add = 'xpath=>//*[@id="custom-toolbar"]/div/div[1]/div/button'
    btnCreateGlobal = 'xpath=>//*[@id="btnCreateGlobalNav"]'
    nav = 'xpath=>//*[@id="navName"]'
    btnSaveGlobal = 'xpath=>//*[@id="btnSaveGlobalNav"]'
    btnSel = 'xpath=>//*[@id="btnSelCategory"]'
    # categoryTree = 'xpath=>//*[@id="categoryTreeTable"]/tbody/tr[1]/td[1]/input'
    categoryTree = 'xpath=>//*[@id="categoryTreeTable"]/tbody/tr[15]/td[1]/input'
    category_T = 'xpath=>//*[@id="categoryTable"]/tbody/tr[1]/td[1]/input'
    btnSelC = 'xpath=>//*[@id="btnSelComment"]'
    btnCreateN = 'xpath=>//*[@id="btnCreateNav"]'
    addService = 'xpath=>//*[@id="addServiceGroupBlackProduct"]'
    detail = 'xpath=>//*[@id="detailTable"]/tbody/tr[2]/td[2]/a[1]/i'
    btnSaveN = 'xpath=>//*[@id="btnSaveNav"]'
    recommendN = 'xpath=>//*[@id="recommendName"]'
    btnRecommend = 'xpath=>//*[@id="btnRecommendSearch"]'
    detailT = 'xpath=>//*[@id="detailTable"]/tbody/tr[3]/td[2]/a[2]/i'#上移
    detailT1 = 'xpath=>//*[@id="detailTable"]/tbody/tr[2]/td[2]/a[3]/i'#下移
    detailT2 = 'xpath=>//*[@id="detailTable"]/tbody/tr[2]/td[2]/a[4]/i'#删除
    detailT3 = 'xpath=>//*[@id="detailTable"]/tbody/tr[2]/td[2]/a[5]/i'#取消推荐位
    detailT4 = 'xpath=>//*[@id="detailTable"]/tbody/tr[2]/td[2]/a[6]/i'   #  取消跳转
    small = 'xpath=>/html/body/div[3]/div/div[2]/h2/small/a'
    busines = 'xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[3]/a'
    combo = 'xpath=>//*[@id="comboKey"]'
    start = 'xpath=>//*[@id="startup"]'
    shut = 'xpath=>//*[@id="shutdown"]'
    bus_edit = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[3]/a[1]/i'
    bound = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[3]/a[2]/i'
    unbindT = 'xpath=>//*[@id="unbindTable"]/tbody/tr/td[1]/input'
    svcgrp = 'xpath=>//*[@id="svcgrpBind"]'
    bindS = 'xpath=>//*[@id="bindSvcgrp"]'
    navigation = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[3]/a[3]/i'
    navigationT = 'xpath=>//*[@id="navigationTable"]/tbody/tr[1]/td[1]/input'
    btnNavigation = 'xpath=>//*[@id="btnNavigationBind"]'
    details = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[3]/a[4]/i'
    recommend_n = 'xpath=>//*[@id="name_n"]'
    recommendList = 'xpath=>//*[@id="recommendListTable"]/tbody/tr/td[1]/a/i'
    btnComboRecommend = 'xpath=>//*[@id="btnComboRecommendSave"]'
    recommendList1 = 'xpath=>//*[@id="recommendListTable"]/tbody/tr/td[1]/a[3]/i'
    recommendList2 = 'xpath=>//*[@id="recommendListTable"]/tbody/tr/td[1]/a[2]/i'
    combo_nav = 'xpath=>//*[@id="combo_nav_list"]/div/div/div[2]/div[3]/div/button[2]'
    combo_nav_button = 'xpath=>//*[@id="combo_nav_list"]/div/div/div[2]/div[6]/button'
    bindT = 'xpath=>//*[@id="bindTable"]/tbody/tr/td[1]/input'
    svcgrpUn = 'xpath=>//*[@id="svcgrpUnbind"]'
    # relieve = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[9]/a[2]/i'
    relieve = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[9]/a/i'
    collapseT = 'xpath=>//*[@id="collapseTwo"]/div/ul/li[1]/a'
    mac_type = 'xpath=>//*[@id="mac_type2"]'
    startM = 'xpath=>//*[@id="startMac"]'
    endM = 'xpath=>//*[@id="endMac"]'
    create_devicerule = 'xpath=>//*[@id="create_devicerule_form"]/div[13]/div/button[1]'
    startbutt = 'xpath=>//*[@id="start"]'
    stopbutt = 'xpath=>//*[@id="stop"]'
    program_list = 'xpath=>//*[@id="program_list_dialog"]/div/div/div[1]/button/span'
    poster = 'xpath=>//*[@id="table"]/tbody/tr/td[2]/a[7]/i'
    spec = 'xpath=>//*[@id="spec_table"]/tbody/tr/td[2]/a/i'
    spec_input = 'xpath=>//*[@id="spec_table"]/tbody/tr/td[1]/input'
    spec_pkg = 'xpath=>//*[@id="spec_pkg_pic"]/div/div/div[2]/div[5]/button'
    btnAddS = 'xpath=>//*[@id="btnAddSeries"]'
    addSeries = 'xpath=>//*[@id="addSeriesName"]'
    sgAddSeries = 'xpath=>//*[@id="sgAddSeriesTable"]/tbody/tr/td[1]/input'
    ter_edit = 'xpath=>//*[@id="table"]/tbody/tr/td[3]/a[1]/i'
    edit_devicerule = 'xpath=>//*[@id="edit_devicerule_form"]/div[12]/div/button[1]'
    handoff = 'xpath=>//*[@id="table"]/tbody/tr/td[3]/a[4]/i'
    change_servicecombo = 'xpath=>//*[@id="change_servicecombo_form"]/div[2]/div/button[1]'
    unbound = 'xpath=>//*[@id="table"]/tbody/tr/td[3]/a[3]/i'
    collapse2 = 'xpath=>//*[@id="collapseTwo"]/div/ul/li[2]/a'
    mac = 'xpath=>//*[@id="mac"]'
    unbound1 = 'xpath=>//*[@id="table"]/tbody/tr/td[3]/a[2]/i'
    addUpgrade = 'xpath=>//*[@id="addUpgradeType"]'
    upload_version = 'xpath=>//*[@id="upload_versionSeq"]'
    md5 = 'xpath=>//*[@id="upload_md5"]'
    submitT = 'xpath=>//*[@id="submitTitle"]'
    addMac = 'xpath=>//*[@id="addMacs"]'
    btnDevice = 'xpath=>//*[@id="btnDeviceUpgrade"]'
    upgradeS = 'xpath=>//*[@id="upgradeSeq"]'
    deleteM = 'xpath=>//*[@id="delete"]'
    apkVersion = 'xpath=>//*[@id="apkVersionSeq"]'
    searchDiv_lab = 'xpath=>//*[@id="searchDiv"]/div/label[3]/div/button'
    searchDiv_lab_input = 'xpath=>//*[@id="searchDiv"]/div/label[3]/div/div/div/input'
    search_m = 'xpath=>//*[@id="search_mac"]'
    create_vendor = 'xpath=>//*[@id="create_vendor_form"]/div[1]/div/input'
    create_vendor_text = 'xpath=>//*[@id="create_vendor_form"]/div[3]/div/textarea'
    create_vendor_button = 'xpath=>//*[@id="create_vendor_form"]/div[4]/div/button[1]'
    search_n = 'xpath=>//*[@id="search_name"]'
    edit_vendor = 'xpath=>//*[@id="edit_vendor_form"]/div[4]/div/button[1]'
    coLL = 'xpath=>//*[@id="collapseTwo"]/div/ul/li/a'
    create_type = 'xpath=>//*[@id="create_type_form"]/div[1]/div/input'
    create_type_text = 'xpath=>//*[@id="create_type_form"]/div[5]/div/textarea'
    create_type_button = 'xpath=>//*[@id="create_type_form"]/div[6]/div/button[1]'
    edit_type = 'xpath=>//*[@id="edit_type_form"]/div[6]/div/button[1]'
    create_chipvendor = 'xpath=>//*[@id="create_chipvendor_form"]/div[1]/div/input'
    create_chipvendor_text = 'xpath=>//*[@id="create_chipvendor_form"]/div[3]/div/textarea'
    create_chipvendor_button = 'xpath=>//*[@id="create_chipvendor_form"]/div[4]/div/button[1]'
    edit_chipvendor = 'xpath=>//*[@id="edit_chipvendor_form"]/div[4]/div/button[1]'
    custom_tool = 'xpath=>//*[@id="custom-toolbar"]/div[3]/div[1]/button'
    title = 'xpath=>//*[@id="title"]'
    content = 'xpath=>//*[@id="content"]'
    create_msg = 'xpath=>//*[@id="create_msg_form"]/div[14]/div[2]/button'
    saveCombo = 'xpath=>//*[@id="saveComboMacs"]'
    btnCreateM = 'xpath=>//*[@id="btnCreateMsg"]'
    ltitle = 'xpath=>//*[@id="ltitle"]'
    tool_custom = 'xpath=>//*[@id="custom-toolbar"]/div[3]/div[2]/button'
    logs = 'xpath=>//*[@id="logs_table"]/tbody/tr/td[2]/a[1]/i'
    toolbar_cus = 'xpath=>//*[@id="custom-toolbar"]/div[3]/div[3]/button'
    logs_input = 'xpath=>//*[@id="logs_table"]/tbody/tr[1]/td[1]/input'
    button_custom = 'xpath=>//*[@id="custom-toolbar"]/div[3]/div[5]/button'
    btnExamine = 'xpath=>//*[@id="btnExamineMsg"]'
    logs_i = 'xpath=>//*[@id="logs_table"]/tbody/tr[1]/td[2]/a[2]/i'
    preview_msg = 'xpath=>//*[@id="preview_msg_form"]/div[11]/div/button[2]'
    logs_a3 = 'xpath=>//*[@id="logs_table"]/tbody/tr[1]/td[2]/a[3]/i'
    searchUser = 'xpath=>//*[@id="searchUserId"]'
    del_custom = 'xpath=>//*[@id="custom-toolbar"]/div[3]/div[4]/button'
    search_button = 'xpath=>//*[@id="searchDiv"]/div/button'
    Onecollapse = 'xpath=>//*[@id="collapseOne"]/div/ul[2]/li/a'
    custom_new = 'xpath=>//*[@id="custom-toolbar"]/div/div/button[1]'
    url = 'xpath=>//*[@id="url"]'
    node = 'xpath=>//*[@id="node_name"]'
    secret = 'xpath=>//*[@id="secret"]'
    opt = 'xpath=>//*[@id="opt-btn"]'
    msg_server = 'xpath=>//*[@id="msg_server_table"]/tbody/tr/td[2]/a[3]/i'
    reset = 'xpath=>//*[@id="reset"]'
    msg_server_input = 'xpath=>//*[@id="msg_server_table"]/tbody/tr[1]/td[1]/input'
    msg_server_input1 = 'xpath=>//*[@id="msg_server_table"]/tbody/tr[2]/td[1]/input'
    stop_custom = 'xpath=>//*[@id="custom-toolbar"]/div/div/button[4]'
    start_custom = 'xpath=>//*[@id="custom-toolbar"]/div/div/button[3]'
    t_msg_server = 'xpath=>//*[@id="msg_server_table"]/tbody/tr/td[2]/a[1]/i'
    del_msg_server = 'xpath=>//*[@id="msg_server_table"]/tbody/tr/td[2]/a[2]/i'
    frmRecommend_button = 'xpath=>//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/button/span[2]/span'
    frmRecommend_span = 'xpath=>//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/div/ul/li[1]/a/span[1]'
    special = 'xpath=>//*[@id="specialName"]'
    ordinary = 'xpath=>//*[@id="ordinaryName"]'

    #chunxiao
    Agentvendor = 'xpath=>//*[@id="agentVendorKey"]'
    Sure = 'xpath=>//*[@id="agentvendor_form"]/div[12]/div/button[1]'  # 点击确定
    N_search = 'xpath=>//*[@id="searchName"]'  # 输入名称
    AgentvendorType = 'xpath=>//*[@id="create_agentvendortype_form"]/div[1]/div/input'
    Descriptive_information = 'xpath=>//*[@id="create_agentvendortype_form"]/div[3]/div/textarea'
    Preservation1 = 'xpath=>//*[@id="create_agentvendortype_form"]/div[4]/div/button[1]'  # 点击保存
    Preservation2 = 'xpath=>//*[@id="edit_agentvendortype_form"]/div[4]/div/button[1]'  # 点击保存
    System_attribute = 'xpath=>//*[@id="collapseFour"]/div/ul/li[1]/a'  # 点击系统属性管理
    Chinese_name = 'xpath=>//*[@id="cn"]'  # 输入属性名称
    Attribute_value = 'xpath=>//*[@id="value"]'  # 输入属性值
    Newly_build = 'xpath=>//*[@id="create_systemproperties_form"]/div[6]/div/button[1]'  # 系统列表新增
    Search1 = 'xpath=>//*[@id="btnNameSearch"]'  # 点击搜索
    Property_name1 = 'xpath=>//*[@id="nameSearch"]'  # 点击搜索后输入属性名称
    Property_name2 = 'xpath=>//*[@id="search_name"]'  # 点击高级搜索后输入属性名称
    Edit = 'xpath=>//*[@id="table"]/tbody/tr[47]/td[2]/a[1]/i'  # 点击系统属性管理编辑
    Preservation3 = 'xpath=>//*[@id="edit_systemproperties_form"]/div[6]/div/button[1]'  # 点击保存
    Edit_name1 = 'xpath=>//*[@id="edit_value"]'  # 编辑属性值
    Radio = 'xpath=>//*[@id="table"]/tbody/tr[47]/td[1]/input'  # 点击单选框
    Delete1 = 'xpath=>//*[@id="table"]/tbody/tr[47]/td[2]/a[2]/i'  # 点击删除
    System_attribute_group = 'xpath=>//*[@id="collapseFour"]/div/ul/li[2]/a'  # 点击系统属性组管理
    Remarks = 'xpath=>//*[@id="systempropertiesgroup_form"]/div[2]/div/textarea'  # 点击系统属性组管理
    Newly_build1 = 'xpath=>//*[@id="systempropertiesgroup_form"]/div[3]/div/button[1]'  # 点击新建
    Api_address = 'xpath=>//*[@id="collapseFour"]/div/ul/li[3]/a'  # 点击新建
    Newly_added = 'xpath=>//*[@id="custom-toolbar"]/div/div/button[1]'  # 点击新增
    Preservation4 = 'xpath=>//*[@id="opt-btn"]'  # 点击新增
    Edit = 'xpath=>//*[@id="apiurl_table"]/tbody/tr[4]/td[2]/a[1]/i'  # 点击编辑
    Delete2 = 'xpath=>//*[@id="apiurl_table"]/tbody/tr[4]/td[2]/a[2]/i'  # 点击删除
    Login_name1 = 'xpath=>//*[@id="loginName"]'  # 输入登录名
    Login_pwd = 'xpath=>//*[@id="pwd"]'  # 输入登录名
    Login_pwd_2 = 'xpath=>//*[@id="pwd_2"]'  # 输入登录名
    Binding = 'xpath=>//*[@id="myForm"]/div[6]/div/div/button/span[1]'  # 点击‘绑定业务组合’
    Select_all = 'xpath=>//*[@id="myForm"]/div[6]/div/div/div/div[2]/div/button[1]'  # 点击select_all
    Telephone = 'xpath=>//*[@id="myForm"]/div[7]/div/input'  # 输入联系电话
    Inputname = 'xpath=>//*[@id="searchForm"]/div[1]/label[2]/input'  # 输入搜索内容
    Click_search = 'xpath=>//*[@id="searchForm"]/div[2]/button[1]'  # 点击搜索
    Click_edit = 'xpath=>//*[@id="user_table"]/tbody/tr/td[2]/a[1]/i'  # 点击编辑
    Edit_name2 = 'xpath=>//*[@id="myForm"]/div[4]/div/input'  # 点击编辑
    Click_del = 'xpath=>//*[@id="user_table"]/tbody/tr/td[2]/a[3]/i'  # 点击删除
    Type_role = 'xpath=>//*[@id="myForm"]/div[1]/div/input'  # 输入角色名称
    Click_edit2 = 'xpath=>//*[@id="role_table"]/tbody/tr/td[2]/a[1]/i'  # 点击编辑
    Click_distribution = 'xpath=>//*[@id="role_table"]/tbody/tr/td[2]/a[3]/i'  # 点击分配权限
    Click_del2 = 'xpath=>//*[@id="role_table"]/tbody/tr/td[2]/a[2]/i'  # 点击删除
    Type_role2 = 'xpath=>//*[@id="searchForm"]/div[1]/label[2]/input[1]'  # 点击编辑
    Click_wallpaper = 'xpath=>//*[@id="collapseTwo"]/div/ul/li[1]/a'  # 点击运营壁纸管理
    Click_binding2 = 'xpath=>//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/button/span[1]'  # 点击绑定业务组合
    Click_search2 = 'xpath=>//*[@id="frmRecommendDoc"]/div[2]/div[1]/div/div/div[2]/div/button[1]'  # 点击select all
    Type_wallpaper = 'xpath=>//*[@id="specialName"]'  # 输入搜索内容
    Click_search3 = 'xpath=>//*[@id="custom-toolbar"]/div/button'  # 点击搜索

    # jiaojiao
    # upLoad = 'xpath=>//*[@id="frmRecommendItemDoc"]/div[10]/div/div/div[3]/div[2]/a'
    upLoad = 'xpath=>//*[@id="frmRecommendItemDoc_r"]/div[10]/div/div/div[3]/div[2]/a'
    allK = 'xpath=>//*[@id="allKeyword"]'
    btnAll = 'xpath=>//*[@id="btnAllKeywordSearch"]'
    btnAllS = 'xpath=>//*[@id="btnAllSelected"]'
    product_play = 'xpath=>//*[@id="product_play_info"]/div/div/div[2]/div/button'
    catS = 'xpath=>//*[@id="catSelector"]'
    btnSelect = 'xpath=>//*[@id="btnSelectNext"]'
    btnSelectC = 'xpath=>//*[@id="btnSelectCategory"]'
    tab_input0 = 'xpath=>//*[@id="table"]/thead/tr/th[1]/div[1]/input'  # 点击对勾
    pictureDelete = 'xpath=>//*[@id="frmRecommendItemDoc"]/div[6]/div/div/div[1]/div[1]'
    searchDetail = 'xpath=>//*[@id="search_detail_name"]'
    moveT = 'xpath=>//*[@id="moveTo"]'
    btnMoveT = 'xpath=>//*[@id="btnMoveTo"]'
    upMove = 'xpath=>//*[@id="table"]/tbody/tr[2]/td[2]/a[1]/i'
    removE = 'xpath=>//*[@id="remove"]'
    doubleclick = 'xpath=>/html/body/div[3]/div/div[2]/div[3]/div[2]/div[1]/table/thead/tr/th[3]/div[1]'
    epgVersion = 'xpath=>//*[@id="epgVersion4"]'
    AppendColumnbtn = 'xpath=>//*[@id="btnAppendColumn"]'
    columnName = 'xpath=>//*[@id="columnName"]'
    Appendbtn = 'xpath=>//*[@id="btnAppendColumnItem"]'
    preview = 'xpath=>//*[@id="browse"]'
    returnbtn = 'xpath=>/html/body/div[3]/div/div[2]/h2/small/a'
    authN = 'xpath=>//*[@id="authName"]'
    searchB = 'xpath=>//*[@id="searchButton"]'
    choose = 'xpath=>//*[@id="chooseProduct"]'
    search_span = 'xpath=>//*[@id="searchDiv"]/div/label[3]/div/button/span[2]/span'
    productAll = 'xpath=>//*[@id="productAllSelector"]'
    selectorT = 'xpath=>//*[@id="selectorTable"]/tbody/tr/td[1]/input'
    search_detail = 'xpath=>//*[@id="search_detail_showName"]'
    manualOpen = 'xpath=>//*[@id="manualOpenToolbar"]/button[1]'
    combo_div = 'xpath=>//*[@id="combo_div"]/div/div/div/div/input'
    input_search = 'xpath=>/html/body/div[3]/div/div[2]/div[3]/div[1]/div[3]/input'
    customId = 'xpath=>//*[@id="customId_0"]/td[1]/input'
    manualOpen_butt = 'xpath=>//*[@id="manualOpenToolbar"]/button[2]'
    manualOpen_butt3 = 'xpath=>//*[@id="manualOpenToolbar"]/button[3]'
    shown = 'xpath=>//*[@id="showname"]'
    customId4 = 'xpath=>//*[@id="customId_4"]/td[1]/input'
    customId2 = 'xpath=>//*[@id="customId_2"]/td[1]/input'
    manualOpen4 = 'xpath=>//*[@id="manualOpenToolbar"]/button[4]'
    manualOpen5 = 'xpath=>//*[@id="manualOpenToolbar"]/button[5]'
    manualTool = 'xpath=>//*[@id="manualToolbar"]/button[1]'
    confirm_butt = 'xpath=>/html/body/div[10]/div/div/div[3]/button'
    manualTool3 = 'xpath=>//*[@id="manualToolbar"]/button[3]'
    collapse3 = 'xpath=>//*[@id="collapseTwo"]/div/ul/li[3]/a'
    selectedProduct = 'xpath=>//*[@id="selectedProductName"]'
    btnPool = 'xpath=>//*[@id="btnPoolSearch"]'
    Toolbar = 'xpath=>//*[@id="manualOpenToolbar"]/div/button'
    Toolbarinput = 'xpath=>//*[@id="manualOpenToolbar"]/div/div/div/input'
    Toolbarspan = 'xpath=>/html/body/div[3]/div/div[2]/h2/div[2]/button/span[2]/span'
    inputcom = 'xpath=>/html/body/div[3]/div/div[2]/h2/div[2]/div/div/input'
    searchinput = 'xpath=>/html/body/div[3]/div/div[2]/div[2]/div[1]/div[3]/input'
    tab_product = 'xpath=>//*[@id="tab_product"]/div[2]/div[2]/div[4]/div[1]/span[2]/span/button/span[2]'
    copy = 'xpath=>//*[@id="copyBtn"]'
    dele_copy = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[2]/a[5]/i'
    sync = 'xpath=>//*[@id="sync_data"]'

    # BMS
    click_price = 'xpath=>/html/body/div[1]/div/div[2]/ul[1]/li[1]/a'  # 点击价签管理
    click_increase = 'xpath=>//*[@id="add_price"]'  # 点击新增
    type_month = 'xpath=>//*[@id="duration"]'  # 输入有效时长
    type_price = 'xpath=>//*[@id="price"]'  # 输入价格（分）
    click_save = 'xpath=>//*[@id="register_price"]'  # 点击保存
    # click_search = 'xpath=>//*[@id="search_name"]'  # 点击搜索
    click_edit1 = 'xpath=>//*[@id="table"]/tbody/tr/td[3]/a/i'  # 点击编辑
    click_save2 = 'xpath=>//*[@id="edit_price"]'  # 点击保存
    click_demand = 'xpath=>//*[@id="dianbo"]'  # 点击点播
    click_delete = 'xpath=>//*[@id="delete_price"]'  # 点击删除
    click_add = 'xpath=>//*[@id="discount_create_btn"]'  # 点击新增
    # type_discount2 = 'xpath=>//*[@id="value"]'  # 输入折扣值
    click_time1 = 'xpath=>//*[@id="effectTimeDiv"]/span/span'  # 点击生效时间
    click_time2 = 'xpath=>//*[@id="expireTimeDiv"]/span/span'  # 点击失效时间
    click_save3 = 'xpath=>//*[@id="register_discount"]'  # 点击保存
    click_Determine = 'xpath=>/html/body/div[10]/div/div/div[3]/button'  # 点击确认
    click_Determine3 = 'xpath=>/html/body/div[3]/div/div[2]/div[4]/div[2]/div[2]/table/tbody/tr/td[3]/a/i'  # 点击编辑
    click_save4 = 'xpath=>//*[@id="edit_discount"]'  # 点击保存
    click_delete2 = 'xpath=>//*[@id="discount_delete_btn"]'  # 点击删除
    click_add2 = 'xpath=>//*[@id="vendorPolicy_create_btn"]'  # 点击新增
    type_party = 'xpath=>//*[@id="policyCode"]'  # 输入三方计费代码
    type_channel = 'xpath=>//*[@id="policyName"]'  # 输入渠道定价策略
    type_content = 'xpath=>//*[@id="showName"]'  # 输入显示名称
    type_discount = 'xpath=>//*[@id="showDiscountValue"]'  # 输入折扣取值
    click_save5 = 'xpath=>//*[@id="register_vendorPolicy"]'  # 点击保存
    click_save6 = 'xpath=>//*[@id="edit_vendorPolicy"]'  # 编辑后点击保存
    click_delete3 = 'xpath=>//*[@id="vendorPolicy_delete_btn"]'  # 点击删除
    click_channel = 'xpath=>//*[@id="packageTree"]/ul/li[3]/span[5]/span'  # 点击电视剧渠道定价
    click_whole = 'xpath=>//*[@id="customId_0"]/td[1]/input'  # 点击渠道策略-包时段复选框
    click_confirm = 'xpath=>//*[@id="bindPackageSubmit"]'  # 点击确认
    click_delete4 = 'xpath=>//*[@id="policyAssetsTable"]/tbody/tr/td[3]/a[1]/i'  # 点击删除图标
    click_add3 = 'xpath=>//*[@id="packageTree"]/ul/li[3]/span[2]'  # 点击电视剧加号图标
    click_add4 = 'xpath=>//*[@id="packageTree"]/ul/li[4]/span[3]'  # 点击电视剧子栏目加号图标
    click_channel2 = 'xpath=>//*[@id="packageTree"]/ul/li[4]/span[6]/span'  # 点击电视剧子栏目渠道定价
    click_box = 'xpath=>//*[@id="packageTree"]/ul/li[3]/span[4]'  # 点击电视剧复选框
    click_box2 = 'xpath=>//*[@id="packageTree"]/ul/li[1]/span[3]'  # 点击AgentZero栏目树复选框
    click_prod = 'xpath=>//*[@id="bindPackage"]'  # 点击产品包批量定价
    click_prod1 = 'xpath=>//*[@id="unSelectedProductTable"]/tbody/tr[1]/td[1]/input'  # 点击第一个产品名称复选框
    click_Determine4 = 'xpath=>//*[@id="productInfo"]'  # 点击确认
    click_dan = 'xpath=>//*[@id="radio_1200190106010797914460005"]'  # 点击单选
    click_Determine5 = 'xpath=>//*[@id="bindProductSubmit"]'  # 点击确认
    click_attribute = 'xpath=>//*[@id="btnExtra"]'  # 点击附加属性
    click_Plus = 'xpath=>//*[@id="addExtraAttr"]/span'  # 点击+号
    type_no = 'xpath=>//*[@id="extra_new"]/td[3]/input'  # 输入免费期数
    click_nike = 'xpath=>//*[@id="extra_new_add"]/span'  # 点击对勾
    click_fork = 'xpath=>//*[@id="extra_list_dialog"]/div/div/div[1]/button/span'  # 点击叉号
    click_channel = 'xpath=>//*[@id="packageTree"]/ul/li[2]/span[5]/span'  # 点击渠道定价
    type_prod = 'xpath=>//*[@id="agentVendorAssetNameInput"]'  # 请输入商品名称
    click_search3 = 'xpath=>//*[@id="agentVendorSearchByName"]'  # 点击搜索
    click_edit3 = 'xpath=>//*[@id="policyAssetsTable"]/tbody/tr/td[3]/a[2]/i'  # 点击编辑
    click_synchronization = 'xpath=>//*[@id="policyAssetsTable"]/tbody/tr[1]/td[3]/a[3]/i'  # 点击同步
    click_vod = 'xpath=>//*[@id="radio_1200190106010797371810004"]'  # 点击单片点播10元
    type_prod2 = 'xpath=>//*[@id="assetName"]'  # 輸入搜索的商品名稱
    click_add5 = 'xpath=>//*[@id="createOrder_btn"]'  # 点击新增
    click_search4 = 'xpath=>//*[@id="choose_product_package"]'  # 点击选择产品包
    click_search5 = 'xpath=>//*[@id="package_table"]/tbody/tr/td[1]/input'  # 点击选择产品包复选框
    click_confirm2 = 'xpath=>//*[@id="pro_confirm"]'  # 点击确认
    click_generate = 'xpath=>//*[@id="createOrder"]'  # 点击生成工单
    click_confirm3 = 'xpath=>/html/body/div[15]/div/div/div[3]/button'  # 点击确认
    type_tripartite = 'xpath=>//*[@id="externalUserId"]'  # 输入三方用户

    # bms_interface
    click_ad1 = 'xpath=>//*[@id="packageTree"]/ul/li[2]/span[2]'  # 点击agentzero综艺加号
    click_ad2 = 'xpath=>//*[@id="packageTree"]/ul/li[3]/span[3]'  # 点击agentzero综艺加号
    click_box3 = 'xpath=>//*[@id="packageTree"]/ul/li[5]/span[6]'  # 点击az20180312az复选框
    click_box4 = 'xpath=>//*[@id="customId_13"]/td[1]/input'  # 点击agentzero渠道定价
    click_search6 = 'xpath=>//*[@id="searchProduct"]'  # 点击搜索
    click_box5 = 'xpath=>//*[@id="policyAssetsTable"]/tbody/tr/td[1]/input'  # 点击复选框
    click_box6 = 'xpath=>//*[@id="policyAssetsTable"]/thead/tr/th[1]/div[1]/input'  # 点击复选框
    click_delete5 = 'xpath=>//*[@id="deleteBind"]'  # 点击批量删除
    click_edit4 = 'xpath=>//*[@id="table"]/tbody/tr[1]/td[3]/a/i'  # 点击编辑


    def type_search(self, text):
        self.type(self.input_usr, text)
        self.sleep(1)

    def type_search2(self, text):
        self.type(self.input_pas, text)
        self.sleep(1)

    def send_fm1(self):
        self.click(self.fm1)
        self.sleep(2)

    def search_Content(self):
        self.click(self.search_Con)
        self.sleep(2)

    def send_submit_btn(self):
        self.click(self.search_submit_btn)
        self.sleep(2)

    def clear_edit(self):
        self.clear(self.add_edit)
        self.sleep(2)

    def edit_name(self, text):
        self.type(self.add_edit, text)
        self.sleep(2)

    def send_deter(self):
        self.click(self.deter)
        self.sleep(2)

    def determine(self):
        self.click(self.b_deter)
        self.sleep(3)

    def table_input(self):
        self.click(self.tab_input)
        self.sleep(1)

    def table_input1(self):
        self.click(self.tab_input1)
        self.sleep(2)

    def check_shenhe(self):
        self.click(self.check_1)
        self.sleep(2)

    def check_series_form(self):
        self.click(self.check_series)
        self.sleep(1)

    def button_1(self):
        self.click(self.but_1)
        self.sleep(3)

    def button_2(self):
        self.click(self.but_2)
        self.sleep(3)

    def searchBtn(self):
        self.click(self.search)
        self.sleep(2)

    def add_names(self, text):
        self.type(self.add_name, text)
        self.sleep(2)

    def clear_names(self):
        self.clear(self.add_name)
        self.sleep(2)

    def searchByName(self):
        self.click(self.search_B)
        self.sleep(4)

    def searchReset(self):
        self.click(self.search_R)
        self.sleep(3)

    def table_2(self):
        self.click(self.tab_2)
        self.sleep(2)

    def offline_series_form(self):
        self.click(self.offline_series)
        self.sleep(2)

    def searchDiv(self):
        self.click(self.search_D)
        self.sleep(2)

    def searchDivInput(self, text):
        self.type(self.search_D_input, text)
        self.sleep(2)

    def searchMore(self):
        self.click(self.search_M)
        self.sleep(2)

    def seriesName(self, text):
        self.type(self.series_N, text)
        self.sleep(1)

    def cp_xlakuang(self):
        self.click(self.cp_xlk)
        self.sleep(2)

    def hq_cp_mc(self, text):
        self.type(self.hq_cp_name, text)
        self.sleep(1)

    def dj_xuanding(self):
        self.click(self.dj_xd)
        self.sleep(2)

    def fenlei_one(self, text):
        self.type(self.fl_one, text)
        self.sleep(1)

    def fenlei_two(self, text):
        self.type(self.fl_two, text)
        self.sleep(1)

    def dj_sous(self):
        self.click(self.dj_seach)
        self.sleep(5)

    def dj_shuaxin(self):
        self.click(self.dj_shuax)
        self.sleep(1)

    def online_1(self):
        self.click(self.on_line)
        self.sleep(3)

    def qd_anniu(self):
        self.click(self.qd_ann)
        self.sleep(3)

    def offline(self):
        self.click(self.off_line)
        self.sleep(3)

    def clear_number(self):
        self.clear(self.del_num)

    def add_num(self, text):
        self.type(self.del_num, text)
        self.sleep(1)

    def clear_ji(self):
        self.clear(self.ji_num)

    def add_ji(self, text):
        self.type(self.ji_num, text)
        self.sleep(1)

    def btnSaveVolumn(self):
        self.click(self.btnSave)
        self.sleep(3)

    def qs_anniu(self):
        self.click(self.qs_ann)
        self.sleep(2)

    def collapseOnes(self):
        self.click(self.collapseO)
        self.sleep(3)

    def check_program_form(self):
        self.click(self.check_program)
        self.sleep(3)

    def dj_jiemj(self):
        self.click(self.dj_jmj)
        self.sleep(2)

    def dj_shangxx(self):
        self.click(self.dj_sxx)
        self.sleep(2)

    def offline_program_from(self):
        self.click(self.offline_program)
        self.sleep(3)

    def sc_anniu(self):
        self.click(self.sc_ann)
        self.sleep(2)

    def seriescode(self, text):
        self.type(self.series_C, text)
        self.sleep(2)

    def cp_dianji(self):
        self.click(self.cp_dj)
        self.sleep(2)

    def cp_shuru(self, text):
        self.type(self.cp_sr, text)
        self.sleep(2)

    def gj_jmmc(self, text):
        self.type(self.gj_jm, text)
        self.sleep(2)

    def gj_jmjmc(self, text):
        self.type(self.gj_jmj, text)
        self.sleep(2)

    def dj_cpkuang(self):
        self.click(self.dj_cpk)
        self.sleep(2)

    def sr_cpneirong(self, text):
        self.type(self.sr_cpnr, text)
        self.sleep(2)

    def dj_fenfayu(self):
        self.click(self.dj_ffy)
        self.sleep(3)

    def ffy_sx_queding(self):
        self.click(self.ffy_sx_qd)
        self.sleep(3)

    def dj_chanpguanl(self):
        self.click(self.dj_cp_gl)
        self.sleep(3)

    def custom_toolbar(self):
        self.click(self.custom)
        self.sleep(3)

    def custom_toolbar1(self):
        self.click(self.customT)
        self.sleep(3)

    def sr_mingchen(self, text):
        self.type(self.sr_mc, text)
        self.sleep(2)

    def sr_zs_mingchen(self, text):
        self.type(self.sr_zs_mc, text)
        self.sleep(2)

    def xz_chanping(self):
        self.click(self.xz_cp)
        self.sleep(3)

    def cp_mingchen(self, text):
        self.type(self.cp_mc, text)
        self.sleep(2)

    def sr_chanp(self):
        self.click(self.sr_cp_mc)
        self.sleep(3)

    def sr_cp_mingchen(self, text):
        self.type(self.sr_cp_mingc, text)
        self.sleep(2)

    def dj_duig(self):
        self.click(self.dj_dg)
        self.sleep(1)

    def click_duig(self):
        self.click(self.click_dg)
        self.sleep(1)

    def prd_add(self):
        self.click(self.pd_add)
        self.sleep(3)

    def prd_Remove(self):
        self.click(self.pd_Remove)
        self.sleep(3)

    def pd_dialog(self):
        self.click(self.pd_dia)
        self.sleep(2)

    def btnSaves(self):
        self.click(self.btn)
        self.sleep(3)

    def btnCreat(self):
        self.click(self.btn_c)
        self.sleep(2)

    def confirm_1(self):
        self.click(self.confirm)
        self.sleep(1)

    def package_name(self, text):
        self.type(self.pk_name, text)
        self.sleep(2)

    def edit_package_form(self):
        self.click(self.edit_pac)
        self.sleep(2)

    def edit_product(self):
        self.click(self.edit_p)
        self.sleep(2)

    def delete_an(self):
        self.click(self.del_an)
        self.sleep(2)

    def dc_shuju(self):
        self.click(self.dc_sj)
        self.sleep(2)

    def jc_peizhi(self):
        self.click(self.jc_pz)
        self.sleep(2)

    def collapseThree(self):
        self.click(self.coll)
        self.sleep(2)

    def online_program_form(self):
        self.click(self.online_program)
        self.sleep(2)

    def collapseOne(self):
        self.click(self.collapse)
        self.sleep(2)

    def product_name(self, text):
        self.type(self.product_N, text)
        self.sleep(2)

    def product_name_clear(self):
        self.clear(self.product_N)
        self.sleep(2)

    def edit_product_form(self):
        self.click(self.edit_product_f)
        self.sleep(2)

    def s_PkgName(self, text):
        self.type(self.s_Pkg, text)
        self.sleep(2)

    def s_PkgCode(self, text):
        self.type(self.s_PkgC, text)
        self.sleep(2)

    def s_BtnSearch(self):
        self.click(self.s_Btn)
        self.sleep(2)

    def unbindPkgTable(self):
        self.click(self.unbind)
        self.sleep(2)

    def add_package_dialog(self):
        self.click(self.add_package)
        self.sleep(2)

    def add_package_span(self):
        self.click(self.package_span)
        self.sleep(2)

    def searchByContentName(self):
        self.click(self.searchBy)
        self.sleep(2)

    def glyphicon_edit(self):
        self.click(self.glyphicon)
        self.sleep(2)

    def column_M(self):
        self.click(self.column)
        self.sleep(2)

    def treeAdd(self):
        self.click(self.tree)
        self.sleep(2)

    def managename(self, text):
        self.type(self.manage, text)
        self.sleep(2)

    def description(self, text):
        self.type(self.descrip, text)
        self.sleep(2)

    def clear_description(self):
        self.clear(self.descrip)
        self.sleep(2)

    def btnCreateTree(self):
        self.click(self.btnCreate)
        self.sleep(3)

    def btnStartup(self):
        self.click(self.btnStart)
        self.sleep(2)

    def btnStartdown(self):
        self.click(self.btnStart1)
        self.sleep(2)

    def tab_Deta(self):
        self.click(self.tab_D)
        self.sleep(2)

    def categoryRoot(self):
        self.click(self.category)
        self.sleep(2)

    def selectorTable(self):
        self.click(self.selector)
        self.sleep(2)

    def btnSelected(self):
        self.click(self.btn_S)
        self.sleep(2)

    def categoryRoot1(self):
        self.click(self.category_R)
        self.sleep(2)

    def categoryRoot2(self):
        self.click(self.category_Ro)
        self.sleep(2)

    def html_1(self):
        self.click(self.html)
        self.sleep(2)

    def packageSearchText(self, text):
        self.type(self.packageSearch, text)
        self.sleep(2)

    def btnPkgSearch(self):
        self.click(self.btnPkg)
        self.sleep(2)

    def libPkgTable(self):
        self.click(self.libPkg)
        self.sleep(2)

    def bindProduct(self):
        self.click(self.bind)
        self.sleep(3)

    def categoryRoot_1(self):
        self.click(self.category1)
        self.sleep(2)

    def categoryRoot_2(self):
        self.click(self.category2)
        self.sleep(2)

    def categoryRoot_3(self):
        self.click(self.category3)
        self.sleep(2)

    def cleanProduct(self):
        self.click(self.clean)
        self.sleep(2)

    def productPkg(self):
        self.click(self.product)
        self.sleep(2)

    def categoryRoot_4(self):
        self.click(self.category4)
        self.sleep(2)

    def categoryRoot_5(self):
        self.click(self.category5)
        self.sleep(2)

    def btnSaveTree(self):
        self.click(self.btnSave_t)
        self.sleep(2)

    def htmlbody(self):
        self.click(self.html2)
        self.sleep(2)

    def treeRemove(self):
        self.click(self.tree_R)
        self.sleep(2)

    def btnCreates(self):
        self.click(self.btn_C)
        self.sleep(3)

    def servicegrouping(self):
        self.click(self.service)
        self.sleep(2)

    def customtoolbar(self):
        self.click(self.custom1)
        self.sleep(2)

    def customtoolbar2(self):
        self.click(self.custom2)
        self.sleep(2)

    def searchText(self, text):
        self.type(self.search_T, text)
        self.sleep(2)

    def table_Input(self):
        self.click(self.table_I)
        self.sleep(2)

    def table_Bj(self):
        self.click(self.table_B)
        self.sleep(2)

    def custom_button(self):
        self.click(self.custom_B)
        self.sleep(2)

    def body_right(self):
        self.click(self.body_r)
        self.sleep(2)

    def pkgStyleSearchText(self, text):
        self.type(self.pkgStyle, text)
        self.sleep(1)

    def heartPackage(self):
        self.click(self.heart)
        self.sleep(2)

    def exportBtn(self):
        self.click(self.export)
        self.sleep(2)

    def body_rights(self):
        self.click(self.body)
        self.sleep(1)

    def body_rights1(self):
        self.click(self.body1)
        self.sleep(1)

    def body_rights2(self):
        self.click(self.body2)
        self.sleep(1)

    def prdName(self,text):
        self.type(self.prd, text)
        self.sleep(2)

    def clear_prdName(self):
        self.clear(self.prd)
        self.sleep(2)

    def domain_form(self):
        self.click(self.domain)
        self.sleep(3)

    def recommend(self):
        self.click(self.recomm)
        self.sleep(2)

    def add_recomm(self):
        self.click(self.add)
        self.sleep(2)

    def productTable(self):
        self.click(self.productT)
        self.sleep(2)

    def btnAppend(self):
        self.click(self.btnA)
        self.sleep(5)

    def poolSearchName(self, text):
        self.type(self.pool, text)
        self.sleep(1)

    def frmRecommendItemDoc(self):
        self.click(self.frmRecommend)
        self.sleep(2)

    def collapseThree1(self):
        self.click(self.collapse_t)
        self.sleep(2)

    def interfaceURL(self,text):
        self.type(self.interface, text)
        self.sleep(1)

    def cmsID(self,text):
        self.type(self.cms, text)
        self.sleep(1)

    def sopID(self,text):
        self.type(self.sop, text)
        self.sleep(1)

    def prioritys(self,text):
        self.type(self.priority, text)
        self.sleep(1)

    def table_10_input(self):
        self.click(self.table_10)
        self.sleep(2)

    def custom4_toolbar(self):
        self.click(self.custom4)
        self.sleep(2)

    def i_tables(self):
        self.click(self.i_table)
        self.sleep(2)

    def i_tables_3(self):
        self.click(self.i_table_3)
        self.sleep(2)

    def create_template_form(self):
        self.click(self.create)
        self.sleep(2)

    def templateTable(self):
        self.click(self.template)
        self.sleep(2)

    def edit_template_form(self):
        self.click(self.edit_tem)
        self.sleep(2)

    def templateTable2(self):
        self.click(self.template2)
        self.sleep(2)

    def show_domainTemplate_dialog(self):
        self.click(self.show_domainTemplate)
        self.sleep(2)

    def table_delete(self):
        self.click(self.tab_del)
        self.sleep(2)

    def collapseThrees(self):
        self.click(self.collaps)
        self.sleep(2)

    def templateName(self,text):
        self.type(self.template_N, text)
        self.sleep(1)

    def edit_table(self):
        self.click(self.e_table)
        self.sleep(2)

    def templateFileSubmit(self):
        self.click(self.templateFile)
        self.sleep(2)

    def deleteTemplateFileBtn(self):
        self.click(self.deleteTemplate)
        self.sleep(2)

    def cp_collapseThree(self):
        self.click(self.cp_collapse)
        self.sleep(2)

    def toolbar(self):
        self.click(self.new_custom)
        self.sleep(2)

    def frmCP(self,text):
        self.type(self.frm, text)
        self.sleep(1)

    def frmCP_code(self,text):
        self.type(self.code, text)
        self.sleep(1)

    def startDate(self):
        self.click(self.startD)
        self.sleep(1)

    def emdDate(self):
        self.click(self.endD)
        self.sleep(1)

    def btnAdds(self):
        self.click(self.btnAdd)
        self.sleep(2)

    def cpNames(self,text):
        self.type(self.cpName, text)
        self.sleep(1)

    def btnSearch(self):
        self.click(self.btnS)
        self.sleep(2)

    def btnUps(self):
        self.click(self.btnUp)
        self.sleep(2)

    def btnDowns(self):
        self.click(self.btnDown)
        self.sleep(2)

    def dj_edits(self):
        self.click(self.dj_edit)
        self.sleep(1)

    def btnUpdates(self):
        self.click(self.btnUpdate)
        self.sleep(2)

    def custom_delete(self):
        self.click(self.custom_del)
        self.sleep(2)

    def domaininjection_form(self):
        self.click(self.domaininjection)
        self.sleep(2)

    def edit_package_tag(self,text):
        self.type(self.edit_package, text)
        self.sleep(1)

    def custom_add_toolbar(self):
        self.click(self.custom_add)
        self.sleep(2)

    def btnCreateGlobalNav(self):
        self.click(self.btnCreateGlobal)
        self.sleep(2)

    def navName(self,text):
        self.type(self.nav, text)
        self.sleep(1)

    def btnSaveGlobalNav(self):
        self.click(self.btnSaveGlobal)
        self.sleep(2)

    def btnSelCategory(self):
        self.click(self.btnSel)
        self.sleep(2)

    def categoryTreeTable(self):
        self.click(self.categoryTree)
        self.sleep(1)

    def categoryTable(self):
        self.click(self.category_T)
        self.sleep(1)

    def btnSelComment(self):
        self.click(self.btnSelC)
        self.sleep(1)

    def btnCreateNav(self):
        self.click(self.btnCreateN)
        self.sleep(2)

    def addServiceGroupBlackProduct(self):
        self.click(self.addService)
        self.sleep(2)

    def detailTable(self):
        self.click(self.detail)
        self.sleep(1)

    def btnSaveNav(self):
        self.click(self.btnSaveN)
        self.sleep(2)

    def recommendName(self,text):
        self.type(self.recommendN,text)
        self.sleep(2)

    def clear_recommendName(self):
        self.clear(self.recommendN)
        self.sleep(2)

    def btnRecommendSearch(self):
        self.click(self.btnRecommend)
        self.sleep(2)

    def detailTable2(self):
        self.click(self.detailT)
        self.sleep(2)

    def detailTable3(self):
        self.click(self.detailT1)
        self.sleep(2)

    def detailTable4(self):
        self.click(self.detailT2)
        self.sleep(2)

    def detailTable5(self):
        self.click(self.detailT3)
        self.sleep(2)

    def detailTable6(self):
        self.click(self.detailT4)
        self.sleep(2)

    def html_small(self):
        self.click(self.small)
        self.sleep(2)

    def busines_com(self):
        self.click(self.busines)
        self.sleep(2)

    def comboKey(self,text):
        self.type(self.combo, text)
        self.sleep(1)

    def startup(self):
        self.click(self.start)
        self.sleep(2)

    def shutdown(self):
        self.click(self.shut)
        self.sleep(3)

    def business_edit(self):
        self.click(self.bus_edit)
        self.sleep(2)

    def bound_ser(self):
        self.click(self.bound)
        self.sleep(2)

    def unbindTable(self):
        self.click(self.unbindT)
        self.sleep(2)

    def svcgrpBind(self):
        self.click(self.svcgrp)
        self.sleep(2)

    def bindSvcgrp(self):
        self.click(self.bindS)
        self.sleep(2)

    def navigation_bind(self):
        self.click(self.navigation)
        self.sleep(2)

    def navigationTable(self):
        self.click(self.navigationT)
        self.sleep(2)

    def btnNavigationBind(self):
        self.click(self.btnNavigation)
        self.sleep(2)

    def navigation_details(self):
        self.click(self.details)
        self.sleep(2)

    def recommend_names(self,text):
        self.type(self.recommend_n, text)
        self.sleep(1)

    def recommendListTable(self):
        self.click(self.recommendList)
        self.sleep(2)

    def btnComboRecommendSave(self):
        self.click(self.btnComboRecommend)
        self.sleep(2)

    def recommendListTable1(self):
        self.click(self.recommendList1)
        self.sleep(2)

    def recommendListTable2(self):
        self.click(self.recommendList2)
        self.sleep(2)

    def combo_nav_list(self):
        self.click(self.combo_nav)
        self.sleep(2)

    def combo_nav_list_button(self):
        self.click(self.combo_nav_button)
        self.sleep(2)

    def bindTable(self):
        self.click(self.bindT)
        self.sleep(2)

    def svcgrpUnbind(self):
        self.click(self.svcgrpUn)
        self.sleep(2)

    def Remove_navigation(self):
        self.click(self.relieve)
        self.sleep(2)

    def collapseTwo(self):
        self.click(self.collapseT)
        self.sleep(2)

    def mac_type2(self):
        self.click(self.mac_type)
        self.sleep(2)

    def startMac(self,text):
        self.type(self.startM, text)
        self.sleep(1)

    def endMac(self,text):
        self.type(self.endM, text)
        self.sleep(1)

    def create_devicerule_form(self):
        self.click(self.create_devicerule)
        self.sleep(2)

    def startbutton(self):
        self.click(self.startbutt)
        self.sleep(2)

    def stopbutton(self):
        self.click(self.stopbutt)
        self.sleep(2)

    def program_list_dialog(self):
        self.click(self.program_list)
        self.sleep(2)

    def special_poster(self):
        self.click(self.poster)
        self.sleep(2)

    def spec_table(self):
        self.click(self.spec)
        self.sleep(2)

    def spec_input_table(self):
        self.click(self.spec_input)
        self.sleep(2)

    def spec_pkg_pic(self):
        self.click(self.spec_pkg)
        self.sleep(2)

    def btnAddSeries(self):
        self.click(self.btnAddS)
        self.sleep(2)

    def addSeriesName(self,text):
        self.type(self.addSeries,text)
        self.sleep(2)

    def sgAddSeriesTable(self):
        self.click(self.sgAddSeries)
        self.sleep(2)

    def terminal_edit(self):
        self.click(self.ter_edit)
        self.sleep(2)

    def edit_devicerule_form(self):
        self.click(self.edit_devicerule)
        self.sleep(2)

    def handoff_ser(self):
        self.click(self.handoff)
        self.sleep(2)

    def change_servicecombo_form(self):
        self.click(self.change_servicecombo)
        self.sleep(2)

    def unbound_edit(self):
        self.click(self.unbound)
        self.sleep(2)

    def collapseTwo2(self):
        self.click(self.collapse2)
        self.sleep(2)

    def intomac(self,text):
        self.type(self.mac, text)
        self.sleep(1)

    def unbound_edit1(self):
        self.click(self.unbound1)
        self.sleep(2)

    def addUpgradeType(self):
        self.click(self.addUpgrade)
        self.sleep(2)

    def upload_versionSeq(self,text):
        self.type(self.upload_version, text)
        self.sleep(1)

    def upload_md5(self,text):
        self.type(self.md5, text)
        self.sleep(1)

    def submitTitle(self):
        self.click(self.submitT)
        self.sleep(13)

    def addMacs(self):
        self.click(self.addMac)
        self.sleep(2)

    def btnDeviceUpgrade(self):
        self.click(self.btnDevice)
        self.sleep(2)

    def upgradeSeq(self,text):
        self.type(self.upgradeS, text)
        self.sleep(1)

    def deleteModify(self):
        self.click(self.deleteM)
        self.sleep(2)

    def apkVersionSeq(self,text):
        self.type(self.apkVersion, text)
        self.sleep(1)

    def searchDiv_lable(self):
        self.click(self.searchDiv_lab)
        self.sleep(1)

    def searchDiv_lable_input(self,text):
        self.type(self.searchDiv_lab_input,text)
        self.sleep(1)

    def search_mac(self,text):
        self.type(self.search_m, text)
        self.sleep(1)

    def create_vendor_form(self,text):
        self.type(self.create_vendor, text)
        self.sleep(1)

    def create_vendor_form_textarea(self,text):
        self.type(self.create_vendor_text, text)
        self.sleep(1)

    def create_vendor_form_button(self):
        self.click(self.create_vendor_button)
        self.sleep(2)

    def search_name(self,text):
        self.type(self.search_n, text)
        self.sleep(1)

    def edit_vendor_form(self):
        self.click(self.edit_vendor)
        self.sleep(2)

    def coLLapseTwo(self):
        self.click(self.coLL)
        self.sleep(2)

    def create_type_form(self,text):
        self.type(self.create_type, text)
        self.sleep(1)

    def create_type_form_text(self,text):
        self.type(self.create_type_text, text)
        self.sleep(1)

    def create_type_form_button(self):
        self.click(self.create_type_button)
        self.sleep(2)

    def edit_type_form(self):
        self.click(self.edit_type)
        self.sleep(2)

    def create_chipvendor_form(self,text):
        self.type(self.create_chipvendor, text)
        self.sleep(1)

    def create_chipvendor_form_text(self,text):
        self.type(self.create_chipvendor_text, text)
        self.sleep(1)

    def create_chipvendor_form_button(self):
        self.click(self.create_chipvendor_button)
        self.sleep(2)

    def edit_chipvendor_form(self):
        self.click(self.edit_chipvendor)
        self.sleep(2)

    def custom_toolbar_button(self):
        self.click(self.custom_tool)
        self.sleep(2)

    def title_N(self,text):
        self.type(self.title, text)
        self.sleep(1)

    def clear_title_N(self):
        self.clear(self.title)
        self.sleep(1)

    def content_test(self,text):
        self.type(self.content, text)
        self.sleep(1)

    def create_msg_form(self):
        self.click(self.create_msg)
        self.sleep(2)

    def saveComboMacs(self):
        self.click(self.saveCombo)
        self.sleep(2)

    def btnCreateMsg(self):
        self.click(self.btnCreateM)
        self.sleep(2)

    def ltitle_N(self,text):
        self.type(self.ltitle, text)
        self.sleep(1)

    def clear_ltitle_N(self):
        self.clear(self.ltitle)
        self.sleep(1)

    def toolbar_custom(self):
        self.click(self.tool_custom)
        self.sleep(2)

    def logs_table(self):
        self.click(self.logs)
        self.sleep(2)

    def toolbar_cust(self):
        self.click(self.toolbar_cus)
        self.sleep(2)

    def logs_table_input(self):
        self.click(self.logs_input)
        self.sleep(2)

    def button_custom_toolbar(self):
        self.click(self.button_custom)
        self.sleep(2)

    def btnExamineMsg(self):
        self.click(self.btnExamine)
        self.sleep(2)

    def logs_table_i(self):
        self.click(self.logs_i)
        self.sleep(3)

    def preview_msg_form(self):
        self.click(self.preview_msg)
        self.sleep(2)

    def logs_table_a3(self):
        self.click(self.logs_a3)
        self.sleep(2)

    def searchUserId(self,text):
        self.type(self.searchUser, text)
        self.sleep(2)

    def delete_custom(self):
        self.click(self.del_custom)
        self.sleep(2)

    def searchDiv_button(self):
        self.click(self.search_button)
        self.sleep(2)

    def OnecollapseOne(self):
        self.click(self.Onecollapse)
        self.sleep(2)

    def custom_new_toolbar(self):
        self.click(self.custom_new)
        self.sleep(2)

    def add_url(self,text):
        self.type(self.url, text)
        self.sleep(1)

    def node_name(self,text):
        self.type(self.node, text)
        self.sleep(1)

    def secret_key(self,text):
        self.type(self.secret, text)
        self.sleep(1)

    def opt_btn(self):
        self.click(self.opt)
        self.sleep(2)

    def msg_server_table(self):
        self.click(self.msg_server)
        self.sleep(2)

    def reset_table(self):
        self.click(self.reset)
        self.sleep(2)

    def msg_server_table_input(self):
        self.click(self.msg_server_input)
        self.sleep(2)

    def msg_server_table_input1(self):
        self.click(self.msg_server_input1)
        self.sleep(2)

    def stop_custom_toolbar(self):
        self.click(self.stop_custom)
        self.sleep(2)

    def start_custom_toolbar(self):
        self.click(self.start_custom)
        self.sleep(2)

    def table_msg_server(self):
        self.click(self.t_msg_server)
        self.sleep(2)

    def del_msg_server_table(self):
        self.click(self.del_msg_server)
        self.sleep(2)

    def frmRecommendDoc_button(self):
        self.click(self.frmRecommend_button)
        self.sleep(2)

    def frmRecommendDoc_span(self):
        self.click(self.frmRecommend_span)
        self.sleep(2)

    def specialName(self,text):
        self.type(self.special, text)
        self.sleep(1)

    def clear_specialName(self):
        self.clear(self.special)
        self.sleep(1)

    def ordinaryName(self,text):
        self.type(self.ordinary, text)
        self.sleep(1)

    def AgentvendorAB(self,text):
        self.type(self.Agentvendor,text)
        self.sleep(2)

    def sure(self):
        self.click(self.Sure)
        self.sleep(2)

    def AgentvendorTp(self,text):
        self.type(self.AgentvendorType,text)
        self.sleep(2)

    def Descriptive(self,text):
        self.type(self.Descriptive_information,text)
        self.sleep(2)

    def preservation1(self):
        self.click(self.Preservation1)
        self.sleep(2)

    def preservation2(self):
        self.click(self.Preservation2)
        self.sleep(2)

    def system_attribute(self):
        self.click(self.System_attribute)
        self.sleep(2)

    def chinese_name(self,text):
        self.type(self.Chinese_name,text)
        self.sleep(2)

    def attribute_value(self,text):
        self.type(self.Attribute_value,text)
        self.sleep(2)

    def newly_build(self):
        self.click(self.Newly_build)
        self.sleep(2)

    def search1(self):
        self.click(self.Search1)
        self.sleep(2)

    def property_name1(self,text):
        self.type(self.Property_name1,text)
        self.sleep(2)

    def clear_Property_name1(self):
        self.clear(self.Property_name1)
        self.sleep(2)

    def property_name2(self,text):
        self.type(self.Property_name2,text)
        self.sleep(2)

    def edit(self):
        self.click(self.Edit)
        self.sleep(2)

    def preservation3(self):
        self.click(self.Preservation3)
        self.sleep(2)

    def edit_name1(self,text):
        self.type(self.Edit_name1,text)
        self.sleep(2)

    def clear_edit_name1(self):
        self.clear(self.Edit_name1)
        self.sleep(2)

    def radio(self):
        self.click(self.Radio)
        self.sleep(2)

    def delete1(self):
        self.click(self.Delete1)
        self.sleep(2)

    def system_attribute_group(self):
        self.click(self.System_attribute_group)
        self.sleep(2)

    def remarks(self,text):
        self.type(self.Remarks,text)
        self.sleep(2)

    def newly_build1(self):
        self.click(self.Newly_build1)
        self.sleep(2)

    def api_address(self):
        self.click(self.Api_address)
        self.sleep(2)

    def newly_added(self):
        self.click(self.Newly_added)
        self.sleep(2)

    def preservation4(self):
        self.click(self.Preservation4)
        self.sleep(2)

    def edit(self):
        self.click(self.Edit)
        self.sleep(2)

    def delete2(self):
        self.click(self.Delete2)
        self.sleep(2)

    def login_name1(self,text):
        self.type(self.Login_name1,text)
        self.sleep(2)

    def login_pwd(self,text):
        self.type(self.Login_pwd,text)
        self.sleep(2)

    def login_pwd_2(self,text):
        self.type(self.Login_pwd_2,text)
        self.sleep(2)

    def binding(self):
        self.click(self.Binding)
        self.sleep(2)

    def select_all(self):
        self.click(self.Select_all)
        self.sleep(2)

    def telephone1(self,text):
        self.click(self.Telephone)
        self.sleep(2)

    def telephone2(self,text):
        self.type(self.Telephone,text)
        self.sleep(2)

    def inputname(self,text):
        self.type(self.Inputname,text)
        self.sleep(2)

    def click_search(self):
        self.click(self.Click_search)
        self.sleep(2)

    def click_edit(self):
        self.click(self.Click_edit)
        self.sleep(2)

    def edit_name2(self,text):
        self.type(self.Edit_name2,text)
        self.sleep(2)

    def click_del(self):
        self.click(self.Click_del)
        self.sleep(2)


    def type_role1(self, text):
        self.type(self.Type_role, text)
        self.sleep(2)

    def click_edit2(self):
        self.click(self.Click_edit2)
        self.sleep(2)

    def click_distribution(self):
        self.click(self.Click_distribution)
        self.sleep(2)

    def click_del2(self):
        self.click(self.Click_del2)
        self.sleep(2)

    def type_role2(self, text):
        self.type(self.Type_role2, text)
        self.sleep(2)

    def click_wallpaper(self):
        self.click(self.Click_wallpaper)
        self.sleep(2)

    def click_binding2(self):
        self.click(self.Click_binding2)
        self.sleep(2)

    def click_search2(self):
        self.click(self.Click_search2)
        self.sleep(2)

    def click_search3(self):
        self.click(self.Click_search3)
        self.sleep(2)

    def NsearchName(self,text):
        self.type(self.N_search, text)
        self.sleep(1)

    def upLoadbtn(self):
        self.click(self.upLoad)
        self.sleep(3)

    def allKeyword(self, text):
        self.type(self.allK, text)
        self.sleep(2)

    def btnAllKeywordSearch(self):
        self.click(self.btnAll)
        self.sleep(5)

    def btnAllSelected(self):
        self.click(self.btnAllS)
        self.sleep(2)

    def product_play_info(self):
        self.click(self.product_play)
        self.sleep(1)

    def catSelector(self):
        self.click(self.catS)
        self.sleep(1)

    def btnSelectNext(self):
        self.click(self.btnSelect)
        self.sleep(5)

    def btnSelectCategory(self):
        self.click(self.btnSelectC)
        self.sleep(1)

    def table_input0(self):
        self.click(self.tab_input0)
        self.sleep(1)

    def pictureDeletebtn(self):
        self.click(self.pictureDelete)
        self.sleep(1)

    def searchDetailbtn(self, text):
        self.type(self.searchDetail, text)
        self.sleep(1)

    def searchDetailbtnc(self):
        self.clear(self.searchDetail)
        self.sleep(1)

    def moveTo(self):
        self.click(self.moveT)
        self.sleep(1)

    def btnMoveTo(self):
        self.click(self.btnMoveT)
        self.sleep(1)

    def upMovebtn(self):
        self.click(self.upMove)
        self.sleep(1)

    def remove(self):
        self.click(self.removE)
        self.sleep(1)

    def doubleclickbtn(self):
        self.click(self.doubleclick)
        self.sleep(1)

    def epgVersion4(self):
        self.click(self.epgVersion)
        self.sleep(1)

    def AppendColumnbutn(self):
        self.click(self.AppendColumnbtn)
        self.sleep(1)

    def columnNamebtn(self, text):
        self.type(self.columnName, text)
        self.sleep(2)

    def Appendbutn(self):
        self.click(self.Appendbtn)
        self.sleep(2)

    def previewbtn(self):
        self.click(self.preview)
        self.sleep(1)

    def returnbutn(self):
        self.click(self.returnbtn)
        self.sleep(2)

    def authName(self,text):
        self.type(self.authN, text)
        self.sleep(1)

    def clear_authName(self):
        self.clear(self.authN)
        self.sleep(1)

    def searchButton(self):
        self.click(self.searchB)
        self.sleep(2)

    def chooseProduct(self):
        self.click(self.choose)
        self.sleep(2)

    def search_span_button(self):
        self.click(self.search_span)
        self.sleep(2)

    def productAllSelector(self):
        self.click(self.productAll)
        self.sleep(3)

    def selectorTabl(self):
        self.click(self.selectorT)
        self.sleep(1)

    def search_detail_showName(self,text):
        self.type(self.search_detail, text)
        self.sleep(1)

    def manualOpenToolbar(self):
        self.click(self.manualOpen)
        self.sleep(1)

    def combo_div_input(self,text):
        self.type(self.combo_div, text)
        self.sleep(1)

    def input_search_test(self,text):
        self.type(self.input_search, text)
        self.sleep(1)

    def clear_input_search(self):
        self.clear(self.input_search)
        self.sleep(2)

    def customId_0(self):
        self.click(self.customId)
        self.sleep(1)

    def manualOpenToolbar_butt(self):
        self.click(self.manualOpen_butt)
        self.sleep(1)

    def manualOpenToolbar_butt3(self):
        self.click(self.manualOpen_butt3)
        self.sleep(1)

    def showname(self,text):
        self.type(self.shown, text)
        self.sleep(1)

    def customId_4(self):
        self.click(self.customId4)
        self.sleep(1)

    def customId_2(self):
        self.click(self.customId2)
        self.sleep(1)

    def manualOpenToolbar4(self):
        self.click(self.manualOpen4)
        self.sleep(1)

    def manualOpenToolbar5(self):
        self.click(self.manualOpen5)
        self.sleep(1)

    def manualToolbar(self):
        self.click(self.manualTool)
        self.sleep(1)

    def confirm_button(self):
        self.click(self.confirm_butt)
        self.sleep(2)

    def manualToolbar3(self):
        self.click(self.manualTool3)
        self.sleep(1)

    def collapseTwo3(self):
        self.click(self.collapse3)
        self.sleep(1)

    def selectedProductName(self,text):
        self.type(self.selectedProduct, text)
        self.sleep(1)

    def btnPoolSearch(self):
        self.click(self.btnPool)
        self.sleep(2)

    def ToolbarmanualOpen(self):
        self.click(self.Toolbar)
        self.sleep(2)

    def manualOpenToolbarinput(self,text):
        self.type(self.Toolbarinput, text)
        self.sleep(1)

    def ToolOpenspan(self):
        self.click(self.Toolbarspan)
        self.sleep(2)

    def Openinputcom(self,text):
        self.type(self.inputcom, text)
        self.sleep(1)

    def searchinputcom(self,text):
        self.type(self.searchinput, text)
        self.sleep(1)

    def clear_searchinputcom(self):
        self.clear(self.searchinput)
        self.sleep(2)

    def tab_product_button(self):
        self.click(self.tab_product)
        self.sleep(1)

    def copyBtn(self):
        self.click(self.copy)
        self.sleep(2)

    def delete_copy(self):
        self.click(self.dele_copy)
        self.sleep(2)

    def sync_data(self):
        self.click(self.sync)
        self.sleep(8)

        # bms

    def Click_price(self):
        self.click(self.click_price)
        self.sleep(2)

    def Click_increase(self):
        self.click(self.click_increase)
        self.sleep(2)

    def Type_month(self, text):
        self.type(self.type_month, text)
        self.sleep(2)

    def Type_price(self, text):
        self.type(self.type_price, text)
        self.sleep(2)

    def clear_edit2(self):
        self.clear(self.type_price)
        self.sleep(2)

    def Click_save(self):
        self.click(self.click_save)
        self.sleep(2)

    def Click_search1(self):
        self.click(self.click_search)
        self.sleep(2)

    def Click_edit1(self):
        self.click(self.click_edit1)
        self.sleep(2)

    def Click_save2(self):
        self.click(self.click_save2)
        self.sleep(2)

    def Click_demand(self):
        self.click(self.click_demand)
        self.sleep(2)

    def Click_delete(self):
        self.click(self.click_delete)
        self.sleep(2)

    def Click_delete2(self):
        self.click(self.click_delete2)
        self.sleep(2)

    def Click_add(self):
        self.click(self.click_add)
        self.sleep(2)

    def Type_discount2(self, text):
        self.type(self.type_discount2, text)
        self.sleep(2)

    def Click_time1(self):
        self.click(self.click_time1)
        self.sleep(2)

    def Click_time2(self):
        self.click(self.click_time2)
        self.sleep(2)

    def Click_save3(self):
        self.click(self.click_save3)
        self.sleep(2)

    def Click_Determine(self):
        self.click(self.click_Determine)
        self.sleep(2)

    def Click_Determine2(self):
        self.click(self.click_Determine2)
        self.sleep(2)

    def Click_Determine3(self):
        self.click(self.click_Determine3)
        self.sleep(2)

    def Click_save4(self):
        self.click(self.click_save4)
        self.sleep(2)

    def Click_add2(self):
        self.click(self.click_add2)
        self.sleep(2)

    def Type_party(self, text):
        self.type(self.type_party, text)
        self.sleep(2)

    def Type_channel1(self, text):
        self.type(self.type_channel, text)
        self.sleep(2)

    def Type_content(self, text):
        self.type(self.type_content, text)
        self.sleep(2)

    def Type_discount(self, text):
        self.type(self.type_discount, text)
        self.sleep(2)

    def Tlick_save5(self):
        self.click(self.click_save5)
        self.sleep(2)

    def Tlick_save6(self):
        self.click(self.click_save6)
        self.sleep(2)

    def Click_delete3(self):
        self.click(self.click_delete3)
        self.sleep(2)

    def Click_channel(self):
        self.click(self.click_channel)
        self.sleep(2)

    def Click_whole(self):
        self.click(self.click_whole)
        self.sleep(2)

    def Click_confirm(self):
        self.click(self.click_confirm)
        self.sleep(2)

    def Click_delete4(self):
        self.click(self.click_delete4)
        self.sleep(2)

    def Click_add3(self):
        self.click(self.click_add3)
        self.sleep(2)

    def Click_add4(self):
        self.click(self.click_add4)
        self.sleep(2)

    def Click_channel2(self):
        self.click(self.click_channel2)
        self.sleep(2)

    def Click_box(self):
        self.click(self.click_box)
        self.sleep(2)

    def search_name1(self):
        self.click(self.search_n)
        self.sleep(1)

    def Click_box1(self):
        self.click(self.click_box)
        self.sleep(1)

    def Click_prod(self):
        self.click(self.click_prod)
        self.sleep(1)

    def Click_prod1(self):
        self.click(self.click_prod1)
        self.sleep(1)

    def Click_Determine4(self):
        self.click(self.click_Determine4)
        self.sleep(1)

    def Click_dan(self):
        self.click(self.click_dan)
        self.sleep(1)

    def Click_Determine5(self):
        self.click(self.click_Determine5)
        self.sleep(1)

    def Click_attribute(self):
        self.click(self.click_attribute)
        self.sleep(1)

    def Click_Plus(self):
        self.click(self.click_Plus)
        self.sleep(1)

    def Type_no(self, text):
        self.type(self.type_no, text)
        self.sleep(2)

    def Click_nike(self):
        self.click(self.click_nike)
        self.sleep(1)

    def Click_fork(self):
        self.click(self.click_fork)
        self.sleep(1)

    def Click_channel(self):
        self.click(self.click_channel)
        self.sleep(1)

    def Type_prod(self, text):
        self.type(self.type_prod, text)
        self.sleep(2)

    def Type_prod2(self, text):
        self.type(self.type_prod2, text)
        self.sleep(2)

    def Type_tripartite(self, text):
        self.type(self.type_tripartite, text)
        self.sleep(1)

    def Clear_prod2(self, text):
        self.clear(self.type_prod2)
        self.sleep(2)

    def Clear_prod(self, text):
        self.clear(self.type_prod)
        self.sleep(2)

    def Click_searh3(self):
        self.click(self.click_search3)
        self.sleep(1)

    def Click_edit3(self):
        self.click(self.click_edit3)
        self.sleep(1)

    def Click_synchronization(self):
        self.click(self.click_synchronization)
        self.sleep(1)

    def Click_vod(self):
        self.click(self.click_vod)
        self.sleep(1)

    def Click_add5(self):
        self.click(self.click_add5)
        self.sleep(1)

    def Click_search4(self):
        self.click(self.click_search4)
        self.sleep(1)

    def Click_search5(self):
        self.click(self.click_search5)
        self.sleep(1)

    def Click_confirm2(self):
        self.click(self.click_confirm2)
        self.sleep(1)

    def Click_confirm3(self):
        self.click(self.click_confirm3)
        self.sleep(1)

    def Click_generate(self):
        self.click(self.click_generate)
        self.sleep(1)

    # bms interface

    def Click_ad1(self):
        self.click(self.click_ad1)
        self.sleep(1)

    def Click_ad2(self):
        self.click(self.click_ad2)
        self.sleep(1)

    def Click_box3(self):
        self.click(self.click_box3)
        self.sleep(1)

    def Click_box4(self):
        self.click(self.click_box4)
        self.sleep(1)

    def Click_search6(self):
        self.click(self.click_search6)
        self.sleep(1)

    def Click_box5(self):
        self.click(self.click_box5)
        self.sleep(1)

    def Click_box6(self):
        self.click(self.click_box6)
        self.sleep(1)

    def Click_delete5(self):
        self.click(self.click_delete5)
        self.sleep(1)


    def Click_edit4(self):
        self.click(self.click_edit4)
        self.sleep(1)

