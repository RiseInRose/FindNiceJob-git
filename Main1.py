from Job_GetDetail_51job import get_detail
from JobSpider_51job_GetUrl import Job_search
import pymysql,urllib.parse,re,pymongo,time
'''
这个负责从任务列表获取任务，然后从网络获取原始数据，然后移除任务列表。
'''
# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
mission_list = NiceJob.mission_list
mission_lists_check = NiceJob.mission_lists_check

while True:
    mission_lists = mission_list.find()
    for i in mission_lists:
        mission_lists_check.update({'get_mission_lists_statue':'1'},{'$set':{'mission_lists_statue':True}})
        Job_search(i['name'])
        get_detail(i['name'])
        print('i have done {}'.format(i['name']))
        mission_list.remove({'name':i['name']})
        print('i have remove {}!'.format(i['name']))
    time.sleep(3)

