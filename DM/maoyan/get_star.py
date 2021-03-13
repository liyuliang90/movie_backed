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
from models.star import Actor

def get(movie_id=1):
    #url = 'https://api.maoyan.com/mmdb/v7/movie/1299372/celebrities.json?channelId=70001'
    url = 'https://api.maoyan.com/mmdb/v7/movie/%s/celebrities.json' % movie_id
    form = {
            'channelId':70001,
    }
    headers = {
        "x-host": "http://maoyanapi.vip.sankuai.com",
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36 MicroMessenger/7.0.9.501 NetType/WIFI MiniProgramEnv/Windows WindowsWechat"
    }
    r = requests.get(url, headers=headers, params=form)
    #r = requests.get(url, headers=headers)
    if r.status_code != 200:
        print(r.status_code)
        return
    r_json = json.loads(r.text)
    person_set = r_json['data']
    for data in person_set:
        for i in data:
            c = Actor()
            c.MovieId = movie_id
            c.PersonId = i['id']
            c.Name = i['cnm']
            c.avatar = i['avatar']
            c.desc = i['desc']
            c.ocr = i['ocr']
            c.roles = i['roles']
            c.still = i['still']
            db_save(c)
    return
   
if __name__ == '__main__':
    get(1299372)
