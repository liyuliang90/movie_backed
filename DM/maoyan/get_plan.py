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
from models.plan import PlanMovie, PlanMovieDate, Plan

def get(ci=60, cinema_id=1, offset=0, limit=12):
    url = 'https://wx.maoyan.com/hostproxy/mmcs/show/v2/cinema/shows.json?cinemaId=16254&ci=60&uuid=3e9073d3ce1dbc994b91806b7409f35c&channelId=70001&userid=234046447&version=wallet-v2.12.9&platform=13&partner=1&riskLevel=71&optimusCode=10'
    url = 'https://wx.maoyan.com/hostproxy/mmcs/show/v2/cinema/shows.json'
    form = {
            'cinemaId':cinema_id,
            'ci':ci,
            'uuid':'3e9073d3ce1dbc994b91806b7409f35c',
            'channelId':70001,
            'userid':234046447,
            'version':'wallet-v2.12.9',
            'platform':13,
            'partner':1,
            'riskLevel':71,
            'optimusCode':10
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
    movies_list = data['movies']
    canema_id = data['cinemaId']
    session = DBSession()
    session.begin()
    for i in movies_list:
        pm = PlanMovie()
        pm.CinemaId = canema_id
        pm.MovieId = i.get('id')
        session.add(pm)
        session.flush()
        shows = i.get('shows')
        for j in shows:
            pmd = PlanMovieDate()
            pmd.PlanMovieId = pm.ID
            pmd.ShowDate = j.get('showDate')
            session.add(pmd)
            session.flush()
            plist = j.get('plist')
            for k in plist:
                p = Plan()
                p.pmdId = pmd.ID
                p.dt = k.get('dt')
                p.tm = k.get('tm')
                p.seqNo = k.get('seqNo')
                p.th = k.get('th')
                p.lang = k.get('lang')
                p.tp = k.get('tp')
                p.vipPrice = k.get('vipPrice')
                p.vipPriceName = k.get('vipPriceName')
                p.vipPriceNameNew = k.get('vipPriceNameNew')
                p.extraDesc = k.get('extraDesc')
                session.add(p)
                session.flush()
    session.commit()
    session.close()
    return
   
if __name__ == '__main__':
    get(60,16254)
