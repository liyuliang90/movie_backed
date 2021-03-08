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
from models.city_section import CityBrand, CityDistrict, CityDistrictSub, CitySubway, CitySubwayStation

def get(city_id=60):
    url = 'https://wx.maoyan.com/proxy/mmcs/cinema/v1/select/items.json?cityId=60&channelId=70001'
    url = 'https://wx.maoyan.com/proxy/mmcs/cinema/v1/select/items.json'
    form = {
            'cityId':city_id,
            'channelId':70001
    }
    headers = {
        "x-host": "http://maoyanapi.vip.sankuai.com",
    }
    #r = requests.get(url, params=form)
    r = requests.get(url, params=form, headers=headers)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    code = r_json.get('code')
    r_json = r_json.get('data')
    if not r_json:
        print('data is empty')
        return
    brands = r_json.get('brand').get('subItems')
    if brands:
        for i in brands:
            if i.get('id') <= 0:
                continue
            cb = CityBrand()
            cb.ID = i.get('id')
            cb.CityId = city_id
            cb.Name = i.get('name')
            cb.Count = i.get('count')
            db_save(cb)
    district_set = r_json.get('district').get('subItems')
    if district_set:
        for i in district_set:
            if i.get('id') < 0:
                continue
            subitems = i.get('subItems')
            district_id = i.get('id')
            for j in subitems:
                if j.get('id') < 0:
                    continue
                cds = CityDistrictSub()
                cds.ID = j.get('id')
                cds.DistrictId = district_id
                cds.Name = j.get('name')
                cds.Count = j.get('count')
                db_save(cds)
            cd = CityDistrict()
            cd.ID = district_id
            cd.CityId = city_id
            cd.Name = i.get('name')
            cd.Count = i.get('count')
            db_save(cd)
            
    subway = r_json.get('subway')
    if subway:
        subway_set = subway.get('subItems')
        for i in subway_set:
            if i.get('id') < 0:
                continue
            subitems = i.get('subItems')
            subway_id = i.get('id')
            for j in subitems:
                if j.get('id') < 0:
                    continue
                css = CitySubwayStation()
                css.ID = j.get('id')
                css.SubwayId = subway_id
                css.Name = j.get('name')
                css.Count = j.get('count')
                db_save(css)
            cs = CitySubway()
            cs.ID = subway_id
            cs.CityId = city_id
            cs.Name = j.get('name')
            cs.Count = j.get('count')
            db_save(cs)

if __name__ == '__main__':
    get()
