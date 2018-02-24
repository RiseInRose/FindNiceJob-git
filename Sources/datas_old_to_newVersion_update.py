# 为了版本更新，暂时不更改爬虫，只需要每次使用这个程序更新数据库即可。
# 后来发现，这样是对的，因为不同爬虫得到的数据不一样，最后都要再次处理的。
'''
# 优先更新数据，尽量不删除。这样可以不使用双数据库。
    if now_time == 0:
        job_detail = NiceJob.job_detail_all
    else:
        job_detail = NiceJob.job_detail1
双数据库，可以保证用户访问时，正常工作，但是注意在main里面，需要在数据有跟新时才发动。

数据库建立时，新数据库最好不要使用detail，因为基础数据库依靠detail识别。
# 可以建立数据库索引，先去索引里面查找。
数据跟新方式：
1。missionlist里来了新任务，去索引里查找，如果有，则不执行。如果没有，则执行
2。新任务完成后，采用upsert方法，添加。

先不考虑海量数据时，数据库的查询效率。


'''



import time
def old_to_new():
    import pymongo
    client = pymongo.MongoClient('localhost', 27017)
    NiceJob = client.NiceJob
    i = NiceJob.collection_names()
    now_time0 = time.asctime(time.localtime(time.time()))
    # now_time = int(now_time0.split(' ')[4].split(':')[1])%2
    JobDetail = NiceJob.JobDetail


    count = 0
    for chart_name in i:
        # print(str(chart_name).split('_')[0])
        try:
            check = str(chart_name).split('_')
            if str(chart_name).split('_')[1]=='detail':
                chart_name_0 = str(chart_name).split('_')[0]
                chart_name = NiceJob[chart_name]
                datas = chart_name.find()
                for each in datas:
                    count +=1
                    try:
                        update_time = each['update_time']
                    except:
                        update_time = '01-22'
                    # print(each)
                    data = {
                        'address': each['address'],
                        'location': each['location'],
                        'job': each['job'],
                        'job_url': each['job_url'],
                        'experience': each['experience'],
                        'job_requirements': each['job_requirements'],
                        'job_category': each['job_category'],
                        'company': each['company'],
                        'company_url': each['company_url'],
                        'area': each['area'],
                        'pay_frist': each['pay_frist'],
                        'pay_last': each['pay_last'],
                        'pub_time_frist': each['pub_time_frist'],
                        'pub_time_last': each['pub_time_last'],
                        'job_status': each['job_status'],
                        'update_time':update_time,
                        'chart_name':chart_name_0
                    }
                    JobDetail.update({'chart_name': chart_name_0,'job_url':each['job_url']}, {'$set': data}, True)
        except:
            pass
    print(count)
if __name__ == '__main__':
    old_to_new()