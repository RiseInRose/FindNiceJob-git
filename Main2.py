'''
这个同步更新数据库
'''
import pymysql,urllib.parse,re,pymongo,time
from datas_old_to_newVersion_update import old_to_new,old_to_news

# 循环列表，当有新内容加入时，开始执行
# 连接mongodb
client = pymongo.MongoClient('localhost', 27017)
NiceJob = client.NiceJob
mission_lists_check = NiceJob.mission_lists_check
# mission_lists_check.insert({'get_mission_lists_statue': '1', 'mission_lists_statue': True})
# mission_lists_check.remove()
while True:
    mission_list = NiceJob.mission_list
    # 这里只循环更新mission_list 内的列表。
    for each in mission_list.find():
        # print(each['name'])
        old_to_news(each['name'])

    time.sleep(3)

    # 目前同步数据，还是全部同步，比较高效的是同步更新过的数据。

