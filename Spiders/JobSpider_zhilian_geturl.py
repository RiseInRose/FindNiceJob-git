import requests
from bs4 import BeautifulSoup
import time
import pymongo
import urllib.parse
import configs as cf
import re

# 搜索爬虫工程师
i = time.strftime("%d/%m/%Y").split('/')
times = str(i[2]) + str(i[1]) + str(i[0])
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client['NiceJob']

def Job_search(search_key):
    client_name = search_key +'Job_'+ times
    client_name = NiceJob[client_name]
    # + str(times)
    # 将搜索词转换成网页能够接受的模式。
    search_key = urllib.parse.quote(search_key)
    page = 1
    url_0 = 'https://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&p={}&isadv=0'.format('上海',search_key,page)
    pages = get_page_num(url_0)  # 获取页面数目
    for page in range(1,pages+1):
        url ='https://sou.zhaopin.com/jobs/searchresult.ashx?jl={}&kw={}&p={}&isadv=0'.format('上海',search_key,page)
        get_list(url,client_name)
        print('page=',page)
# i = '爬虫工程师'
# j = urllib.quote(i)
def get_list(url,client_name):
    r = requests.get(url,headers=cf.headers2)
    r.encoding = 'utf-8'
    # print(r.text)
    soup = BeautifulSoup(r.text, 'lxml')

    i = len(soup.select('table.newlist')) # 获取列表长度
    # 这里有一个问题，如何选择多个css的内容。可以使用select叠加。
    # print(soup.select('table.newlist'))
    # print(i)

    for j in range(1,i):
        data = {
            'job': soup.select('table.newlist')[j].select('tr')[0].select('td.zwmc div a')[0].text.strip(),
            'job_url': soup.select('table.newlist')[j].select('tr')[0].select('td.zwmc div a')[0].get('href'),
            'company': soup.select('table.newlist')[j].select('tr')[0].select('td.gsmc a')[0].text.strip(),
            'company_url': soup.select('table.newlist')[j].select('tr')[0].select('td.gsmc a')[0].get('href'),
        }
        # print(j)
        # print(data)
        client_name.insert_one(data)

        # insert_one的方式，是增加数据
        # print(data)
def get_page_num(url):
    r = requests.get(url, headers=cf.headers2)
    r.encoding = 'utf-8'
    soup = BeautifulSoup(r.text, 'lxml')
    # print(soup)
    page_all = soup.select('div.seach_yx span.search_yx_tj em ')[0].text.strip()
    page_num_0 = int(page_all)/60
    page_num = int(page_num_0)+1
    # print(page_all)
    # print(page_num_0)
    # print(page_num)
    return int(page_num)
if __name__ == '__main__':
    search_key = '量化研究'
    Job_search(search_key)

