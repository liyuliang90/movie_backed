#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

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
    #print(cinemas_list)
    #return
    for i in cinemas_list:
        c = Cinema()
        c.ID = i['id']
        c.cityId = i['cityId']
        c.name = i['nm']
        c.addr = i['addr']
        c.lat = i['lat']
        c.lng = i['lng']
        c.poiId = i['poiId']
        c.shopId = i['shopId']
        c.endorse = i['tag']['endorse']
        c.allowRefund = i['tag']['allowRefund']
        c.snack = i['tag']['snack']
        #c.hallType = i['tag']['hallType']
        c.vipDesc = i['tag']['vipTag']
        c.showTimes = i['showTimes']
        c.cardPromotionTag = i['promotion']['cardPromotionTag']
        c.gis = 'POINT(%s %s)' % (i['lng'],i['lat'])
        db_save(c)
    return
   
if __name__ == '__main__':
    get(60)
