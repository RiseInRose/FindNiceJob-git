import time
import pymongo
import requests
from bs4 import BeautifulSoup
import configs as cf
from baidu_api_address_convert import get_baidu_location
import re
import multiprocessing

'''
这个是jobdetail的多进程版本，经过测试可用

'''
i = time.strftime("%d/%m/%Y").split('/')
times = str(i[2])+str(i[1])+str(i[0])
client = pymongo.MongoClient('localhost', 27017,connect=False)
NiceJob = client.NiceJob
detail_ex = NiceJob['detail_ex']


'''下面这个方法不行，因为，nicejob后面的点，会直接使用函数的方法，而我们用一个代数，是找不到这个方法的。
 k = NiceJob.job_20171215.find()
 后来采用上面这个办法，kk = NiceJob[client_name_0]    k = kk.find() 搞定！
 '''
def progress_get_detail(url,search_key,i):

    # 下面表要求只有一个成功，即匹配。所以报错。
    print('yes')
    detail_name = search_key + '_detail'
    detail_name = NiceJob[detail_name]
    timess = time.strftime("%d/%m/%Y").split('/')
    update_time = timess[1] + '-' + timess[0]
    check_webs_list = [r'jobs.51job.com', r'sou.zhaopin.com']
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
        if detail_name.find({'job_url': url})[0]['update_time'] == update_time:
            print('skip this!,because updated!')
            return 0
    except:
        pass

    if not once_check_webs_web:
        detail_ex.update({'job_url': url}, {'$set': {'job_url': url}}, True)
        print('detail_ex')
        return 0

    try:
        r = requests.get(url, headers=cf.headers2)
    except:
        print('times out!')
        time.sleep(10)
        return
    if r.status_code == 404:
        return 0
    else:
        job_status = '该职位仍在招聘'
    print(r.status_code)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, 'lxml')
    try:
        address = soup.select(
            'body > div.tCompanyPage > div.tCompany_center.clearfix > div.tCompany_main > div:nth-of-type(3) > div > p')[
            0].text.strip().split('：')[1]
    except:
        address = '无地址'
    print(url)

    try:
        job_requirements = \
        soup.select('div.tCompany_main div.tBorderTop_box div.bmsg.job_msg.inbox')[0].text.strip().split('职能类别')[0]
        job_category = soup.select('div.tCompany_main div.tBorderTop_box div.bmsg.job_msg.inbox p.fp')[0].text.strip()
    except:
        pass
    try:
        experience_0 = soup.select('div.jtag.inbox div.t1')[0].text.strip()
        # print(experience_0)
        p = r'(.+经验)'
        experience = re.search(p, experience_0).group(0)
        # print(url)
        p = r'(.+发布)'
        pub_time = re.search(p, experience_0).group(0).split('发布')[0]
        # print(pub_time)
        pay = soup.select('div.tHeader.tHjob div.in div.cn strong')[0].text.strip()
        # print(pay)
    except:
        pass

    # url = {'none'}
    # 到数据库中查询，看是否为新职位。如果没有，则添加，如果有则修改。
    check_new = detail_name.find()
    check_0 = 0

    for each in check_new:
        try:
            if each['job_url'] == url:
                check_0 = 1
        except:
            pass
    # if detail.find({'job_url': url}):
    if check_0 == 1:
        data = {
            'pay_last': pay,
            'pub_time_last': pub_time,
            'job_status': job_status,
            'update_time': update_time,
        }
        detail_name.update({'job_url': i['job_url']}, {'$set': data})
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
            'update_time': update_time,
        }
        detail_name.insert_one(data)
        print('正在添加数据')
def tests(i,j,k):
    print(i)
    print(j)
    print(k)
    time.sleep(3)

def get_detail(search_key):
    client_name = search_key + 'Job_' + times
    kk = NiceJob[client_name]
    k = kk.find()
    # 从列表读取数据，获取详细信息。
    pool = multiprocessing.Pool(processes=4)
    rst = []
    for i in k:
        # print(i)
        url = i['job_url']
        # pool.apply_async(tests, (url,'lili','sdsa'))
        # progress_get_detail(url,detail_name,update_time,i)
        pool.apply_async(progress_get_detail, (url,search_key,i,))

        # 异步开启进程, 非阻塞型, 能够向池中添加进程而不等待其执行完毕就能再次执行循环
        # ！！！进程池设计，只要函数有错误，就不会执行，而且不会报错！这里问题在第二个参数detail_name，前面把detail_name变成数据库了！所以函数直接不能执行！
        # 也就是说，进程池只接受参数，不接受类似数据库的数据结构！！！

    print("--" * 10)
    pool.close()  # 关闭pool, 则不会有新的进程添加进去
    pool.join()  # 必须在join之前close, 然后join等待pool中所有的线程执行完毕
    print("All process done.")
    for i in rst:
        print(i.get())
    # 删除当天的目录表。
    # kk.drop()
if __name__ == '__main__':
    search_key = '爬虫工程师'
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


