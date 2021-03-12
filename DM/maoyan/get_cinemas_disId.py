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
from core.DB import db_save, DBSession
from models.cinema import Cinema

def get(city_id=1, districtId=0, offset=0, limit=12):
    url = 'https://wx.maoyan.com/hostproxy/mmcs/cinema/v1/select/cinemas.json?cityId=60&limit=12&offset=0&channelId=70001&brandId=-1&areaId=-1&districtId=-1&lineId=-1&stationId=-1&hallType=-1&serviceId=-1&lng=120.39629&lat=36.30744'
    url = 'https://wx.maoyan.com/hostproxy/mmcs/cinema/v1/select/cinemas.json'
    form = {
            'cityId':city_id,
            'limit':1000,
            'offset':0,
            'channelId':70001,
            'brandId':-1,
            'areaId':-1,
            'districtId':districtId,
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
    session = DBSession()
    for i in cinemas_list:
        session.begin()
        session.query(Cinema).filter(Cinema.ID==i['id']).update({'districtId':districtId})
        session.commit()
    session.close()
    return
   
if __name__ == '__main__':
    get(60,3185)
