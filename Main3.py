from Job_GetDetail_51job import get_detail
from JobSpider_51job_GetUrl import Job_search
from database_maintain import database_maintain,maintain_delete_database
import pymysql,urllib.parse,re,pymongo,time
from datas_old_to_newVersion_update import old_to_new
'''
定时维护数据库，3个任务并列运行。
'''
# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
mission_list = NiceJob.mission_list
JobDetail = NiceJob.JobDetail
mission_lists_check = NiceJob.mission_lists_check

now_time0 = time.asctime(time.localtime(time.time()))
now_time_H = now_time0.split(' ')[3].split(':')[0]
# ！！！这里now_time_H 爆出bug，说超过列表。原因可能因为升级，导致获取的年月日位置换了。
while True:
    # 下面执行数据库方式不行，会在删除前，不停的往数据库添加老的数据，导致大量重复数据。
    # 优先使用数据更新？对于数据量大的影响？

    # 每6小时从基础数据更新所有内容到django数据库
    if int(now_time_H)%6 == 0 :
        mission_lists_check = NiceJob.mission_lists_check
        # 因为设置了数据库连接关闭，所以，每次启动数据库相关都需要重新开一次？
        mission_lists_check = mission_lists_check.find({'get_mission_lists_statue': '1'})
        for i in mission_lists_check:
            print(i['mission_lists_statue'])
            if i['mission_lists_statue'] == True:
                old_to_new()
                mission_lists_check = NiceJob.mission_lists_check
                mission_lists_check.update({'get_mission_lists_statue': '1'}, {'$set': {'mission_lists_statue': False}})
            print('old_to_new updata done')

    # 每天3点维护基础数据库
    if str(now_time_H) == '03':
        # 获取所有用户监控内容，维护
        all_user_job_monitor = []
        for each in all_user_job_monitor:
            database_maintain(each)
            maintain_delete_database(each)

    time.sleep(3)
