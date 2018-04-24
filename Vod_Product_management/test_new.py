# coding=utf-8
# import re
# a = '名称:中国'
# b = re.split(':',a)[-1]
# print(b)

import urllib.request
import json
from selenium import webdriver
import re

# url = 'http://10.3.1.107:8804/vod_api/commodityList!getCommodityListBySerach?serviceGroupCode=1100122022055962258270018&keyword=dmct'
# url = 'http://10.3.1.107:8804/vod_api/assetList!getProductList?serviceGroupCode=1100122022055962258270018&packageCodes=2100130106013186735100002&pageLimit=200&pageNum=0&isAll=1'
# url = 'http://10.3.1.107:8804/vod_api/assetList!getProductList?serviceGroupCode=1100122022055962258270018&packageCodes=2100130106019243997040019'
url = 'http://10.3.1.107:8804/vod_api/category!getCategoryList?serviceGroupCode=1100122023863706454960019'
# url = 'http://10.3.1.107:8804/vod_api/seriesInfo!getSeriesInfoByCode?domainCodes=2100090022055992407651202&serviceGroupCode=1100122022055962258270018&userCode=1300110023465748663090001&productCode=2100140023646355680780332'
# url1 = 'http://10.3.1.107:8804/vod_api/commodityList!getCommodityListBySerach?serviceGroupCode=1100122022055962258270018&pageNum=100&pageLimit=1'

get_url = urllib.request.urlopen(url).read()
get = get_url.decode('utf-8')
# print(get)
ret = json.loads(get)
# print(ret)
device_id = ret["retCode"]
# print(device_id)
m = ret["retMsg"][3]
# print(m)
# a = re.findall('"retCode":"(.*?)"',get)
c = re.findall(".*?'name': '(.*?)'",str(m))[1]
# b = ''.join(c)
print(c)




# import requests
# import re
# import time
# # head = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:56.0) Gecko/20100101 Firefox/56.0'}
# def sinaname(ID, pages):
#     ii = 0
#     while ii <= pages:
#         ii = ii + 1
#         print('正在提取第%d%s' % (ii, '页'))
#         url_next = 'https://m.weibo.cn/api/comments/showid=' + ID + '&page=' + str(ii)
#         html = requests.get(url_next)  # 请求网址信息
#         try:
#             for jj in range(1, len(html.json()['data'])):
#                 data1 = html.json()['data'][jj]['text']
#                 with open('D:\\Windows7Documents\\Desktop\\My\\weibo456.txt', 'a', encoding='utf-8') as ff:
#                     hanzi = ''.join(re.findall('[\u4e00-\u9fa5]', data1))
#                     ff.write(hanzi + '\n')
#         except:
#             None
#         time.sleep(2)
#
#
# sinaname(ID, pages)


code_name = open('D:\\code.txt').read()
# lines = code_name.readlines()#读取全部内容
# for line in lines:
#     print (line)
# print(code_name)
