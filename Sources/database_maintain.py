# 断点续爬，获取数据库内容，数据不是今天的，且状态是正常招聘的。
# ---------------连接数据库------------
import time
import pymongo
import requests
from bs4 import BeautifulSoup
import configs as cf
import re

client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob

def maintain_get_detail(i,detail_name,detail_ex,update_time):
    url = i['job_url']
    # print(r.status_code)
    # 检查网页是否在输入域名范围内，超出则不爬取。
    check_webs_list = [r'jobs.51job.com',r'sou.zhaopin.com']
    once_check_webs_web = False
    for each in check_webs_list:
        try:
            re.search(each, url).group(0)
            check_webs_web = True
        except:
            check_webs_web = False

        if check_webs_web == True:
            once_check_webs_web = True

    if not once_check_webs_web:
        detail_ex.update({'job_url': url},{'$set':{'job_url': url}},True)
        return 0

    try:
        r = requests.get(url, headers=cf.headers2)
    except :
        return 0
    if r.status_code == 404:
        # 修改状态为已删除。
        data = {
            'job_status': '该职位已删除'
        }
        detail_name.update({'job_url': url}, {'$set': data})
        return 0
    else:
        job_status = '该职位仍在招聘'

    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, 'lxml')

    try:
        experience_0 = soup.select('div.jtag.inbox div.t1')[0].text.strip()
        # print(experience_0)
        p = r'(.+发布)'
        pub_time = re.search(p,experience_0).group(0).split('发布')[0]
        # print(pub_time)
        pay = soup.select('div.tHeader.tHjob div.in div.cn strong')[0].text.strip()
        # print(pay)
    except:pass

    # url = {'none'}
    # 到数据库中查询，看是否为新职位。如果没有，则添加，如果有则修改。
    data = {
        'pay_last': pay,
        'pub_time_last': pub_time,
        'job_status' : job_status,
        'update_time': update_time,
    }
    detail_name.update({'job_url': i['job_url']},{'$set':data})
    # detail.insert_one(data)
    print('正在更新数据')

def database_maintain(search_key):
    i = time.strftime("%d/%m/%Y").split('/')
    date_today = i[1]+'-'+i[0]
    # print(date_today)
    detail_name = search_key + '_detail'
    detail_name = NiceJob[detail_name]
    detail_ex = NiceJob['detail_ex']
    datas = detail_name.find()
    for each in datas:
        # 如果更新时间不是今天，而且职位仍然在招聘中，那么继续更新。
        try:
            if each['update_time'] != date_today and each['job_status']=='该职位仍在招聘':
                maintain_get_detail(each,detail_name,detail_ex,date_today)
        except:
            detail_name.update({'job_url': each['job_url']}, {'$set': {'update_time': date_today}})
            maintain_get_detail(each, detail_name, detail_ex, date_today)

# 日期计算
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

# 数据库维护,删除超过两个月的职位
# 确定职位状况
def maintain_delete_database(search_key):
    detail_name = search_key + '_detail'
    detail_name = NiceJob[detail_name]
    for each in detail_name.find():
        url = each['job_url']
        print(url)
        r = requests.get(url, headers=cf.headers2)
        print(r.status_code)
        if r.status_code == 404:
            # 修改状态为已删除。
            data = {
                'job_status': '该职位已删除'
            }
            detail_name.update({'job_url': url}, {'$set': data})
        #删除超过一个月的职位
        if date_count(each['pub_time_frist'],each['pub_time_last'])>60:
            detail_name.remove({'job_url': url})


if __name__ == '__main__':
    search_key = '爬虫开发'
    database_maintain(search_key)
    # maintain_delete_database(search_key)



