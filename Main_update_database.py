from Job_GetDetail_51job import get_detail
from JobSpider_51job_GetUrl import Job_search
from database_maintain import database_maintain,maintain_delete_database
import pymysql,urllib.parse,re,pymongo,time
from datas_old_to_newVersion_update import old_to_new

# 循环列表，当有新内容加入时，开始执行
# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
mission_lists_check = NiceJob.mission_lists_check
# mission_lists_check.insert({'get_mission_lists_statue': '1', 'mission_lists_statue': True})
# mission_lists_check.remove()
while True:
    mission_list = NiceJob.mission_list
    for each in mission_list.find():
        print(each['name'])
    mission_lists_check = NiceJob.mission_lists_check
    # 因为设置了数据库连接关闭，所以，每次启动数据库相关都需要重新开一次？
    mission_lists_check = mission_lists_check.find({'get_mission_lists_statue': '1'})
    for i in mission_lists_check:
        print(i['mission_lists_statue'])
        if i['mission_lists_statue'] == True:
            old_to_new()
            mission_lists_check = NiceJob.mission_lists_check
            mission_lists_check.update({'get_mission_lists_statue':'1'},{'$set':{'mission_lists_statue':False}})
        print('old_to_new done')

    time.sleep(3)

    # 目前同步数据，还是全部同步，比较高效的是同步更新过的数据。

