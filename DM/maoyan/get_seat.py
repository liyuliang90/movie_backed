#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

import os
import sys
current_dir = os.path.abspath(os.path.dirname(__file__))
parent_dir = os.path.dirname(os.path.dirname(current_dir))
sys.path.append(parent_dir)

from core.DB import DBSession
from get_cinemas import get
from models.citys import Citys

import json
import requests
from core.DB import db_save
from models.cinema import Cinema

from urllib import parse

def get(city_id=1, offset=0, limit=12):
    url_base = 'https://wx.maoyan.com/hostproxy/seat/v8/show/seats.json?'
    url = 'https://wx.maoyan.com/hostproxy/seat/v8/show/seats.json?seqNo=202103050482192&channelId=70001&deviceInfoByQQ=%7B%22identityInfo%22%3A%7B%22appid%22%3A%22wxdbb4c5f1b8ee7da1%22%2C%22openid%22%3A%22o31Py0P6iKX4skE2wSI6kk7t5Y4w%22%7D%2C%22user_type%22%3A%22wx%22%2C%22wechatRiskParams%22%3A%7B%22latitude%22%3A36.30744%2C%22longitude%22%3A120.39629%2C%22speed%22%3A-1%2C%22accuracy%22%3A-1%2C%22networkType%22%3A%22wifi%22%2C%22model%22%3A%22microsoft%22%2C%22pixelRatio%22%3A1%2C%22windowWidth%22%3A414%2C%22windowHeight%22%3A632%2C%22language%22%3A%22zh_CN%22%2C%22version%22%3A%227.0.9%22%2C%22system%22%3A%22Windows%2010%20x64%22%2C%22platform%22%3A%22windows%22%2C%22touchPoint%22%3A%22%7B%7D%22%2C%22app_name%22%3A%22group%22%2C%22user_type%22%3A%22wx%22%2C%22openid%22%3A%22o31Py0P6iKX4skE2wSI6kk7t5Y4w%22%2C%22gender%22%3A0%2C%22city%22%3A%22undefined%22%2C%22province%22%3A%22undefined%22%2C%22avatarUrl%22%3A%22https%3A%2F%2Fimg.meituan.net%2Fmaoyanuser%2F80cdf9a184d40eb9ecc0e5d170f3e45d11928.png%22%2C%22unionId%22%3A%22%7B%7B%20unionId%20%7D%7D%22%7D%7D'
    #s=parse.unquote(url)
    #print(s)
    info = {"appid":"wxdbb4c5f1b8ee7da1","openid":"o31Py0P6iKX4skE2wSI6kk7t5Y4w"}
    deviceInfoByQQ = {
                    "identityInfo":info,
                    "user_type":"wx",
                    "wechatRiskParams":{
                        "latitude":36.30744,
                        "longitude":120.39629,
                        "speed":-1,
                        "accuracy":-1,
                        "networkType":"wifi",
                        "model":"microsoft",
                        "pixelRatio":1,
                        "windowWidth":414,
                        "windowHeight":632,
                        "language":"zh_CN",
                        "version":"7.0.9",
                        "system":"Windows 10 x64",
                        "platform":"windows",
                        "touchPoint":"{}",
                        "app_name":"group",
                        "user_type":"wx",
                        "openid":"o31Py0P6iKX4skE2wSI6kk7t5Y4w",
                        "gender":0,
                        "city":"undefined",
                        "province":"undefined",
                        "avatarUrl":"https://img.meituan.net/maoyanuser/80cdf9a184d40eb9ecc0e5d170f3e45d11928.png",
                        "unionId":"{{ unionId }}"
                    }
                }
    query = { 'seqNo':202103050482192,
              'channelId':70001,
              'deviceInfoByQQ':	json.dumps(deviceInfoByQQ, separators=(',',':'))
    }
    
    url_query = parse.urlencode(query, quote_via=parse.quote)
    url2 = url_base + url_query
    headers = {
        "x-host": "http://maoyanapi.vip.sankuai.com",
        'token': 'MY_00hHSRENj7QSyZ5NSxQmXqj2lscAAAAw-auhnYEWLSL9DYp4VQv0S_zpthoMn9n223zyjNafNFOjLbgBgz8C1HwzWVGul1F_AAAAUAAAAAEB',
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat'
    }
    data = {
        'version': 'wallet-v2.12.3',
        'uuid': '3e9073d3ce1dbc994b91806b7409f35c',
        'platform': '13',
        'partner': 1,
        'riskLevel': 71,
        'optimusCode': 10,
    }
    r = requests.post(url2, headers=headers, data=data)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    print(r_json)
    

if __name__ == '__main__':
    get()