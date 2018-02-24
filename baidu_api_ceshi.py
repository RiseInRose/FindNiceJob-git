

# address = '北京市海淀区上地十街10号'
# my_ak = '4BNYmGY6bFkg2knNx7tbKGqZDGA9cG0c'
# url = 'http://api.map.baidu.com/geocoder/v2/?address='+ address + '&output=json&ak=' + my_ak +'&callback=showLocation'
#
# import requests
# import json
# import re
# r = requests.get(url)
# j = r.text
# print(r.text)
# # print(j.get('location'))
# in_json = json.dumps(r.text)
# print(type(in_json))

# print(json.loads(in_json))
#
# p = r'(cation\()(.+?)(\))'
# name = re.search(p, str(j)).group(2)
# print(name.get('result'))
# print(json.dumps(name).get('result'))
# print(name["result"])

# import time
# time = time.strftime("%d/%m/%Y")
# print(time)

# import urllib.parse
# i = '测试'
# print(urllib.parse.quote(i))
#
# search_key = '爬虫工程师'
# search_key = urllib.parse.quote(urllib.parse.quote(search_key))
# print(search_key)

# import time
# times = time.strftime("%d/%m/%Y")
# i = times.split('/')
# print(i)

# import re
# url2 = 'http://jobs.51job.com/shanghai/97288672.html?s=01&t=0'
# url = 'http://meituan.51job.com/sc/job_shuoming.php?jobid=87287903'
# each = r'jobs.51job.com'
# # i = re.search(each, url).group(0)
# # print(i)
# check_webs_list = [r'jobs.51job.com',r'sou.zhaopin.com']
# once_check_webs_web = False
# for each in check_webs_list:
#     try:
#         re.search(each, url2).group(0)
#         check_webs_web = True
#     except:
#         check_webs_web = False
#     if check_webs_web == True:
#         once_check_webs_web = True
# print(once_check_webs_web)

# a = 'true'
# if a:
#     print('take me go')

# --------数据库手动维护----------

# import pymongo
# url = 'http://jobs.51job.com/shanghai-ypq/96745156.html?s=01&t=0'
#
# client = pymongo.MongoClient('localhost', 27017)
# NiceJob = client.NiceJob
# search_key = '爬虫工程师'
# detail_name = search_key + '_detail'
# detail_name = NiceJob[detail_name]
# # detail_name.remove({'set':{'update_time': '01-12'}})
# i = detail_name.find({'job_url':url})
# print(i[0]['job_url'])
# # i = 'false'
# # print(not i)

# import urllib.parse
# search_key = '量化'
# search_key = urllib.parse.quote(search_key)
# print(search_key)

# for i in range(1,3):
#     print(i)

# ----------测试 网页解码------------
# import requests
# url = 'http://jobs.zhaopin.com/CZ521559630J00025197104.htm?ssidkey=y&ss=201&ff=03&sg=d27259a5b1de43fa81726164a6f48ec3&so=7'
# r = requests.get(url)
# r.encoding = 'utf-8'
# print(r.text)

# ----------测试 网页中文转码------------
# import urllib.parse
# search_key = '中国'
# search_key1 = urllib.parse.quote(search_key)
# search_key = urllib.parse.unquote(search_key1)
# print(search_key1)
# print(search_key)

# ----------测试转码------------

# i = "\u65e5\u672c1\u6708\u6c42\u624d\u6c42\u804c\u6bd4"
# i.encode('utf-8')
# print(i)

# ----------测试某个元素是否在数组内------------
# i = input('please input some:')
# m_list = [1,3,5,7,8,10,12]
# if int(i) in m_list:
#     print('yes!')
# else:print("no!")


# ----------测试mongodb------------
import pymongo
# 激活manggodb
client = pymongo.MongoClient('localhost' , 27017)
# 新建数据库economic
economic = client['tests']
# 在新建economic中新建表 Gold
# day_name = 'jin10_'+ times
tests = economic['tests']
tests.insert({'dates':'hahaha'}) # 这里需要插入字典，才可以