# i = '12-24'
# j = '1-31'
# print(i.split('-')[0])
import time
import pymongo
import requests
from bs4 import BeautifulSoup
import configs as cf
from baidu_api_address_convert import get_baidu_location
import re
def date_count(a,b):
    month_b = int(b.split('-')[0])
    day_b = int(b.split('-')[1])
    month_a = int(a.split('-')[0])
    day_a = int(a.split('-')[1])
    if month_b == 12:
        month_b = 0
    if month_a == 12:
        month_a = 0
    cnt = (month_b - month_a)*30 + day_b-day_a
    return cnt


i = time.strftime("%d/%m/%Y").split('/')
times = str(i[2])+str(i[1])+str(i[0])
search_key = '爬虫工程师'
client_name = search_key +'Job_'+ times
detail_name = search_key + '_detail'

client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
detail_name = NiceJob[detail_name]
# for each in detail_name.find():
#     url = each['job_url']
#     print(url)
#     r = requests.get(url, headers=cf.headers2)
#     print(r.status_code)
#     if r.status_code == 404:
#         # 修改状态为已删除。
#         data = {
#             'job_status': '该职位已删除'
#         }
#         detail_name.update({'job_url': url}, {'$set': data})
#     #删除超过一个月的职位
#     print(each)
#     if date_count(each['pub_time_frist'],each['pub_time_last'])>30:
#         detail_name.remove({'job_url': url})
kk = NiceJob[client_name]
kk.drop()