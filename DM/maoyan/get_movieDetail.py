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
from models.photo import Photo
from core.DB import db_save, DBSession

def get(movie_id=1):
    url = 'https://wx.maoyan.com/hostproxy/mmdb/movie/v5/1299372.json?ci=60&channelId=70001&utm_medium=android&version=wallet-v2.12.13&uuid=3e9073d3ce1dbc994b91806b7409f35c&platform=13&partner=1&riskLevel=71&optimusCode=10'
    url = 'https://wx.maoyan.com/hostproxy/mmdb/movie/v5/%s.json' % movie_id
    form = {
        'ci':60,
        'channelId':70001,
        'utm_medium':'android',
        'version':'wallet-v2.12.13',
        'uuid':'3e9073d3ce1dbc994b91806b7409f35c',
        'platform':13,
        'partner':1,
        'riskLevel':71,
        'optimusCode':10
    }
    headers = {
        "x-host": "http://maoyanapi.vip.sankuai.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }
    r = requests.get(url, headers=headers, params=form,timeout=10)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    session = DBSession()
    session.begin()
    movie_dict = r_json['data']['movie']
    m = session.query(Movie).get(movie_id)
    m.enm = movie_dict.get('enm')
    m.cat = movie_dict.get('cat')
    m.dra = movie_dict.get('dra')
    m.videoImg = movie_dict.get('videoImg')
    m.pubDesc = movie_dict.get('pubDesc')
    m.src = movie_dict.get('src')
    session.add(m)
    for i in movie_dict.get('photos'):
        item = Photo()
        item.MovieId = movie_id
        item.img = i
        session.add(item)
    session.commit()
    session.close()

if __name__ == '__main__':
    get(1299372)
