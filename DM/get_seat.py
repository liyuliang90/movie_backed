#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

from core.DB import DBSession
from get_cinemas import get
from models.citys import Citys

import json
import requests
from core.DB import db_save
from models.cinema import Cinema

def get(city_id=1, offset=0, limit=12):
    url = 'https://wx.maoyan.com/hostproxy/seat/v8/show/seats.json?seqNo=202103040611781&channelId=70001&deviceInfoByQQ=%7B%22identityInfo%22%3A%7B%22appid%22%3A%22wxdbb4c5f1b8ee7da1%22%2C%22openid%22%3A%22o31Py0P6iKX4skE2wSI6kk7t5Y4w%22%7D%2C%22user_type%22%3A%22wx%22%2C%22wechatRiskParams%22%3A%7B%22latitude%22%3A36.30744%2C%22longitude%22%3A120.39629%2C%22speed%22%3A-1%2C%22accuracy%22%3A-1%2C%22networkType%22%3A%22wifi%22%2C%22model%22%3A%22microsoft%22%2C%22pixelRatio%22%3A1%2C%22windowWidth%22%3A414%2C%22windowHeight%22%3A632%2C%22language%22%3A%22zh_CN%22%2C%22version%22%3A%227.0.9%22%2C%22system%22%3A%22Windows%2010%20x64%22%2C%22platform%22%3A%22windows%22%2C%22touchPoint%22%3A%22%7B%7D%22%2C%22app_name%22%3A%22group%22%2C%22user_type%22%3A%22wx%22%2C%22openid%22%3A%22o31Py0P6iKX4skE2wSI6kk7t5Y4w%22%2C%22gender%22%3A0%2C%22city%22%3A%22undefined%22%2C%22province%22%3A%22undefined%22%2C%22avatarUrl%22%3A%22https%3A%2F%2Fimg.meituan.net%2Fmaoyanuser%2F80cdf9a184d40eb9ecc0e5d170f3e45d11928.png%22%2C%22unionId%22%3A%22%7B%7B%20unionId%20%7D%7D%22%7D%7D'
    #url = 'https://wx.maoyan.com/hostproxy/seat/v8/show/seats.json?seqNo=202103040611781&channelId=70001&deviceInfoByQQ={"identityInfo":{"appid":"wxdbb4c5f1b8ee7da1","openid":"o31Py0P6iKX4skE2wSI6kk7t5Y4w"},"user_type":"wx","wechatRiskParams":{"latitude":36.30744,"longitude":120.39629,"speed":-1,"accuracy":-1,"networkType":"wifi","model":"microsoft","pixelRatio":1,"windowWidth":414,"windowHeight":632,"language":"zh_CN","version":"7.0.9","system":"Windows 10 x64","platform":"windows","touchPoint":"{}","app_name":"group","user_type":"wx","openid":"o31Py0P6iKX4skE2wSI6kk7t5Y4w","gender":0,"city":"undefined","province":"undefined","avatarUrl":"https://img.meituan.net/maoyanuser/80cdf9a184d40eb9ecc0e5d170f3e45d11928.png","unionId":"{{ unionId }}"}}'
    
    #url = 'https://wx.maoyan.com/hostproxy/mmcs/cinema/v1/select/cinemas.json?cityId=60&limit=12&offset=0&channelId=70001&brandId=-1&areaId=-1&districtId=-1&lineId=-1&stationId=-1&hallType=-1&serviceId=-1&lng=120.39629&lat=36.30744'
    #url = 'https://wx.maoyan.com/hostproxy/mmcs/cinema/v1/select/cinemas.json'
    '''
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
    '''
    headers = {
        "content-type": "application/x-www-form-urlencoded",
        "x-host": "http://maoyanapi.vip.sankuai.com",
        "uuid": "3e9073d3ce1dbc994b91806b7409f35c",
        "token": "MY_aZKdH5nVgK8SWlHyjSyHEcDWiaIAAAAwQPz5P8tWzkSTHUNX8WSu9PzpthoMn9n223zyjNafNFOjLbgBgz8C1HwzWVGul1F_AAAAUAAAAAEB",
        'x-wxa-page': 'pages/cinema/seat',
        'x-wxa-query': '%7B%22seqNo%22%3A%22202103040611781%22%2C%22showId%22%3A%22611781%22%7D',
        'x-wxa-referer': 'pages/cinema/cinema',
        'X-Requested-With': 'wxapp'
    }
    data = {
        'version': 'wallet-v2.12.3',
        'uuid': '3e9073d3ce1dbc994b91806b7409f35c',
        'platform': '13',
        'partner': 1,
        'riskLevel': 71,
        'optimusCode': 10,
    }
    #r = requests.get(url, headers=headers, params=form)
    r = requests.post(url, headers=headers, data=json.dumps(data))
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    print(r_json)
    

if __name__ == '__main__':
    get()