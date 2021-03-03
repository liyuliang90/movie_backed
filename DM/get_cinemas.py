import json
import requests
from core.DB import db_save
from models.cinema import Cinema

def get(city_id=1, offset=0, limit=12):
    url = 'https://wx.maoyan.com/hostproxy/mmcs/cinema/v1/select/cinemas.json?cityId=60&limit=12&offset=0&channelId=70001&brandId=-1&areaId=-1&districtId=-1&lineId=-1&stationId=-1&hallType=-1&serviceId=-1&lng=120.39629&lat=36.30744'
    url = 'https://wx.maoyan.com/hostproxy/mmcs/cinema/v1/select/cinemas.json'
    form = {
            'cityId':city_id,
            'limit':1000,
            'offset':0,
            'channelId':70001,
            'brandId':-1,
            'areaId':-1,
            'districtId':-1,
            'lineId':-1,
            'stationId':-1,
            'hallType':-1,
            'serviceId':-1,
            'lng':120.39629,
            'lat':36.30744,
    }
    headers = {
        "x-host": "http://maoyanapi.vip.sankuai.com",
    }
    r = requests.get(url, headers=headers, params=form)
    #r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    flag = r_json['success']
    if not flag:
        print('response is not success')
        return 
    data = r_json['data']
    cinemas_list = data['cinemas']
    for i in cinemas_list:
        c = Cinema()
        c.cinemaId = i['id']
        c.cityId = i['cityId']
        c.name = i['nm']
        c.addr = i['addr']
        c.lat = i['lat']
        c.lng = i['lng']
        c.poiId = i['poiId']
        c.shopId = i['shopId']
        db_save(c)
    return
   
if __name__ == '__main__':
    get()
