address = '淞虹路207明基广场D#6楼AD单元'
my_ak = '4BNYmGY6bFkg2knNx7tbKGqZDGA9cG0c'
# 地址后面有时间做一个区分，将漏掉的地址处理。
import requests
import re

def get_baidu_location_revise(address):
    url = 'http://api.map.baidu.com/geocoder/v2/?address=' + address + '&output=json&ak=' + my_ak + '&callback=showLocation'
    r = requests.get(url)
    j = r.text
    try:
        p = r'(tion":{)(.+?)(})'
        data = re.search(p,j).group(2)
        location = {
            'lng': data.split(':')[1].split(',')[0],
            'lat': data.split(':')[2]
        }
        # print(data)
        # print(location)
    except:
        location = '无相关结果:' + address
        # print(j)
    return location

def get_baidu_location(address):
    i3 = {'lng': '121.0', 'lat': '31.0'}
    i4 = {'lng': '120.0', 'lat': '31.0'}
    i0 = get_baidu_location_revise(address)
    # print('i0=',i0)
    if i0 == '无相关结果:' + address:
        print(address)
        try:
            p = r'(.+?号)'
            address_1 = re.search(p,address).group(0)
        except:
            try:
                p = r'(.+?路\d{0,6})'
                address_1 = re.search(p, address).group(0)
            except:
                return i4
        print(address_1)
        i1 = get_baidu_location_revise(address_1)
        if i1 != '无相关结果:' + address_1:
            return i1
        else:
            p = r'(.+?路)'
            address_2 = re.search(p, address).group(0)
            # print(address_2)
            i2 = get_baidu_location_revise(address_2)
            if i2 != '无相关结果:' + address_2:
                return i2
            else:
                return i3
    else: return i0
if __name__ == '__main__':
    print(get_baidu_location(address))

'''
有些详细数据不能解析，先放一边，后面在地图里面搞定。
'''