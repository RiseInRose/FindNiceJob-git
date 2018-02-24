from Job_GetDetail_51job import get_detail
from JobSpider_51job_GetUrl import Job_search
from database_maintain import database_maintain,maintain_delete_database
import pymysql,urllib.parse,re,pymongo,time
from datas_old_to_newVersion_update import old_to_new
# # 打开数据库连接
# db = pymysql.connect("localhost", "root", "hb123456", "nicejob")
#
# # 使用 cursor() 方法创建一个游标对象 cursor
# cursor = db.cursor()
#
# sql = "SELECT * FROM job_web_monitor_list "
# search_key = []
# try:
#    # 执行SQL语句
#    cursor.execute(sql)
#    # 获取所有记录列表
#    results = cursor.fetchall()
#    p = r"(, ')(.+)(')"
#    # mysql中取出的数据，需要转换为字符串才能使用。为什么？
#    for result in results:
#        search_key.append(urllib.parse.unquote(re.search(p,str(result)).group(2)))
# except:
#     print('error!')

# print(search_key)

# 循环列表，当有新内容加入时，开始执行
# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
mission_list = NiceJob.mission_list
JobDetail = NiceJob.JobDetail
mission_lists_check = NiceJob.mission_lists_check

now_time0 = time.asctime( time.localtime(time.time()) )
now_time_H = now_time0.split(' ')[4].split(':')[0]
while True:
    mission_lists = mission_list.find()
    for i in mission_lists:
        mission_lists_check.update({'get_mission_lists_statue':'1'},{'$set':{'mission_lists_statue':True}})
        Job_search(i['name'])
        get_detail(i['name'])
        print('i have done {}'.format(i['name']))
        mission_list.remove({'name':i['name']})
        print('i have remove {}!'.format(i['name']))
    # 下面执行数据库方式不行，会在删除前，不停的往数据库添加老的数据，导致大量重复数据。
    # 优先使用数据更新？对于数据量大的影响？

    if str(now_time_H) == '03':
        # 获取所有用户监控内容，维护
        all_user_job_monitor = []
        for each in all_user_job_monitor:
            database_maintain(each)
            maintain_delete_database(each)

    time.sleep(3)





# search_key = ['爬虫工程师','数据工程师','数据 运维工程师','爬虫开发']
#
# for each in search_key:
#     Job_search(each)
#     get_detail(each)
#
# for each in search_key:
#     database_maintain(each)
#     maintain_delete_database(each)

