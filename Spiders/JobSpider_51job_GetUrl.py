import requests
from bs4 import BeautifulSoup
import time
import pymongo
import urllib.parse
import configs as cf
import re
import multiprocessing

'''
多线程版本
'''

# 搜索爬虫工程师
i = time.strftime("%d/%m/%Y").split('/')
times = str(i[2]) + str(i[1]) + str(i[0])
client = pymongo.MongoClient('localhost', 27017,connect=False)
NiceJob = client['NiceJob']

def Job_search(search_key):

    # + str(times)
    # 将搜索词转换成网页能够接受的模式。
    search_key = urllib.parse.quote(urllib.parse.quote(search_key))
    # 使用unquote ，反解码。
    page = 1
    url_0 = 'http://search.51job.com/list/020000,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(search_key,page)
    pages = get_page_num(url_0)
    pool = multiprocessing.Pool(processes=4)
    for page in range(1,pages+1):
        url ='http://search.51job.com/list/020000,000000,0000,00,9,99,{},2,{}.html?lang=c&stype=1&postchannel=0000&workyear=99&cotype=99&degreefrom=99&jobterm=99&companysize=99&lonlat=0%2C0&radius=-1&ord_field=0&confirmdate=9&fromType=1&dibiaoid=0&address=&line=&specialarea=00&from=&welfare='.format(search_key,page)
        pool.apply_async(get_list, (url, search_key,))
        print(page)
    print("--" * 10)
    pool.close()  # 关闭pool, 则不会有新的进程添加进去
    pool.join()  # 必须在join之前close, 然后join等待pool中所有的线程执行完毕
    print("All process done.")
# i = '爬虫工程师'
# j = urllib.quote(i)
def get_list(url,search_key):
    client_name = search_key + 'Job_' + times
    client_name = NiceJob[client_name]
    r = requests.get(url,headers=cf.headers2)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, 'lxml')
    i = len(soup.select('p.t1 span a'))

    for j in range(i):
        data = {
            'job': soup.select('p.t1 span a')[j].text.strip(),
            'job_url': soup.select('p.t1 span a')[j].get('href'),
            'company': soup.select('span.t2 a')[j].text.strip(),
            'company_url': soup.select('span.t2 a')[j].get('href'),
            'area': soup.select('span.t3')[j].text.strip(),
        }
        client_name.insert_one(data)

        # insert_one的方式，是增加数据
        # print(data)
def get_page_num(url):
    r = requests.get(url, headers=cf.headers2)
    r.encoding = 'gb2312'
    soup = BeautifulSoup(r.text, 'lxml')
    page_all_0 = soup.select('div.p_box div.p_wp div.p_in span.td')[0].text.strip()
    p = r'(共)(.+?)(页)'
    page_all = re.search(p,page_all_0).group(2)
    # print(page_all)
    return int(page_all)
if __name__ == '__main__':
    search_key = '瑜伽'
    Job_search(search_key)

