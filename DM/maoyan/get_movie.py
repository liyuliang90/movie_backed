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
from models.movie import Movie
from core.DB import db_save

def get():
    url = 'https://api.maoyan.com/mmdb/movie/v4/list/hot.json?channelId=70001&ci=60&utm_medium=android&open=on&homepage=off&limit=10'
    url = 'https://api.maoyan.com/mmdb/movie/v4/list/hot.json'
    form = {
        'channelId':70001,
        'ci':60,
        'utm_medium':'android',
        'open':'on',
        'homepage':'off',
        'limit':30
    }
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }
    r = requests.get(url, headers=headers, params=form,timeout=10)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    movie_list = r_json['data']['hot']
    for i in movie_list:
        item = Movie()
        item.ID = i.get('id')
        item.Name = i.get('nm')
        item.Star = i.get('star')
        item.Director = i.get('dir')
        item.rt = i.get('rt')
        item.img = i.get('img')
        item.version = i.get('ver')
        item.sc = i.get('sc')
        item.globalReleased = i.get('globalReleased')
        item.wish = i.get('wish')
        item.showInfo = i.get('showInfo')
        item.showst = i.get('showst')
        item.wishst = i.get('wishst')
        item.showCinemaNum = i.get('showCinemaNum')
        item.dur = i.get('dur')
        item.desc = i.get('desc')
        db_save(item)

if __name__ == '__main__':
    get()
