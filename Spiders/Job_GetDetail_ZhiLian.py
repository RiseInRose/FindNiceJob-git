import time
import pymongo
import requests
from bs4 import BeautifulSoup
import configs as cf
from baidu_api_address_convert import get_baidu_location
import re


i = time.strftime("%d/%m/%Y").split('/')
times = str(i[2])+str(i[1])+str(i[0])
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob

'''下面这个方法不行，因为，nicejob后面的点，会直接使用函数的方法，而我们用一个代数，是找不到这个方法的。
 k = NiceJob.job_20171215.find()
 后来采用上面这个办法，kk = NiceJob[client_name_0]    k = kk.find() 搞定！
 '''

def get_detail(search_key):
    client_name = search_key + 'Job_' + times
    detail_name = search_key + '_detail'
    detail_name = NiceJob[detail_name]
    detail_ex = NiceJob['detail_ex']
    i = time.strftime("%d/%m/%Y").split('/')
    update_time = i[1]+'-'+i[0]
    kk = NiceJob[client_name]
    k = kk.find()
    # print(type(client_name_0))
    # .limit(20)
    list_address = []
    # 从列表读取数据，获取详细信息。
    for i in k:
        # print(i)
        url = i['job_url']
        # 下面表要求只有一个成功，即匹配。所以报错。
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
        # 查看之前是否更新过，如果今天跟新过，则不用处理。用于重启服务。
        try:
            if detail_name.find({'job_url':url})[0]['update_time'] == update_time:
                print('skip this!,because updated!')
                break
        except:pass

        if not once_check_webs_web:
            detail_ex.update({'job_url': url}, {'$set': {'job_url': url}}, True)
            print('detail_ex')
            break

        try:
            r = requests.get(url, headers=cf.headers2)
        except:
            print('times out!')
            time.sleep(10)
            return 0
        if r.status_code == 404:
            break
        else:
            job_status = '该职位仍在招聘'
        print(r.status_code)
        r.encoding = 'utf-8'
        soup = BeautifulSoup(r.text, 'lxml')
        try:
            address = soup.select('body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(3) > div > p')[0].text.strip().split('：')[1]
        except:
            address = '无地址'
        print(url)

        try:
            job_requirements = soup.select('div.tCompany_main div.tBorderTop_box div.bmsg.job_msg.inbox')[0].text.strip().split('职能类别')[0]
            job_category = soup.select('div.tCompany_main div.tBorderTop_box div.bmsg.job_msg.inbox p.fp')[0].text.strip()
        except:
            pass
        try:
            experience_0 = soup.select('div.jtag.inbox div.t1')[0].text.strip()
            # print(experience_0)
            p = r'(.+经验)'
            experience = re.search(p,experience_0).group(0)
            # print(url)
            p = r'(.+发布)'
            pub_time = re.search(p,experience_0).group(0).split('发布')[0]
            # print(pub_time)
            pay = soup.select('div.tHeader.tHjob div.in div.cn strong')[0].text.strip()
            # print(pay)
        except:pass

        # url = {'none'}
        # 到数据库中查询，看是否为新职位。如果没有，则添加，如果有则修改。
        check_new = detail_name.find()
        check_0 = 0

        for each in check_new:
            try:
                if each['job_url'] == url:
                    check_0 = 1
            except:pass
        # if detail.find({'job_url': url}):
        if check_0 == 1:
            data = {
                'pay_last': pay,
                'pub_time_last': pub_time,
                'job_status' : job_status,
                'update_time': update_time,
            }
            detail_name.update({'job_url': i['job_url']},{'$set':data})
            # detail.insert_one(data)
            print('正在更新数据')
# 12月4日更改，在添加新数据时才会去解析新地址（因为解析地址API次数有限）
#         删除if地址需要手动解析的报错
        else:
            location = get_baidu_location(address)
            data = {
                'address': address,
                'location': location,
                'job': i['job'],
                'job_url': i['job_url'],
                'experience': experience,
                'job_requirements': job_requirements,
                'job_category': job_category,
                'company': i['company'],
                'company_url': i['company_url'],
                'area': i['area'],
                'pay_frist': pay,
                'pay_last': pay,
                'pub_time_frist': pub_time,
                'pub_time_last': pub_time,
                'job_status': job_status,
                'update_time':update_time,
            }
            detail_name.insert_one(data)
            print('正在添加数据')

        # 这里不知道为什么，增加不了数据库，那先用另外的表储存吧。/这个问题已经修正，看上面解释
        # NiceJob.Job_.update(i,{$addToSet:data})
        # print(data)
    # ''

    # 删除当天的目录表。
    kk.drop()
if __name__ == '__main__':
    search_key = '量化研究'
    get_detail(search_key)

'''
有些详细数据不能解析，先放一边，后面在地图里面搞定。
这里需要数据需要加入
：
详情页面：数据结构。
要求经验
学历
招聘人数
职位信息
上班地址
'''


