#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler
from core.DB import DBSession
from models.movie import Movie

class MovieHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in MovieHandler')
        result = {
            "movieList":[
                {
                    "id":1299372,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/movie/48774506dc0e68805bc25d2cd087d1024316392.jpg",
                    "version":"",
                    "nm":"你好，李焕英",
                    "preShow":False,
                    "sc":9.5,
                    "globalReleased":True,
                    "wish":1162302,
                    "star":"贾玲,张小斐,沈腾",
                    "rt":"2021-02-12",
                    "showInfo":"今天75家影院放映928场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1300936,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/movie/8a1ad4ec0d81f240e4d8c2d1b10c2ec53475644.jpg",
                    "version":"",
                    "nm":"人潮汹涌",
                    "preShow":False,
                    "sc":9.1,
                    "globalReleased":True,
                    "wish":246956,
                    "star":"刘德华,肖央,万茜",
                    "rt":"2021-02-12",
                    "showInfo":"今天75家影院放映408场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1217023,
                    "haspromotionTag":False,
                    "img":"http://p1.meituan.net/w.h/movie/ece9ff81e6f0af2c859aa151e42a33312706648.jpg",
                    "version":"v2d imax",
                    "nm":"唐人街探案3",
                    "preShow":False,
                    "sc":8.8,
                    "globalReleased":True,
                    "wish":4468547,
                    "star":"王宝强,刘昊然,妻夫木聪",
                    "rt":"2021-02-12",
                    "showInfo":"今天74家影院放映475场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1048268,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/movie/9ef2f7d8d6f11c55723d7be5fa77218d1022103.jpg",
                    "version":"v3d imax",
                    "nm":"刺杀小说家",
                    "preShow":False,
                    "sc":8.6,
                    "globalReleased":True,
                    "wish":500948,
                    "star":"雷佳音,杨幂,董子健",
                    "rt":"2021-02-12",
                    "showInfo":"今天73家影院放映314场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1225754,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/moviemachine/778ef027d0fe90fd27448d8369d4cf9e2820477.jpg",
                    "version":"",
                    "nm":"猫和老鼠",
                    "preShow":False,
                    "sc":7.9,
                    "globalReleased":True,
                    "wish":298926,
                    "star":"科洛·格蕾斯·莫瑞兹,迈克尔·佩纳,郑肯",
                    "rt":"2021-02-26",
                    "showInfo":"今天68家影院放映274场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1298938,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/movie/72291e1cbc83311656e01e828ca79ddd2106074.jpg",
                    "version":"v3d",
                    "nm":"熊出没·狂野大陆",
                    "preShow":False,
                    "sc":8.9,
                    "globalReleased":True,
                    "wish":390157,
                    "star":"张秉君,谭笑,张伟",
                    "rt":"2021-02-12",
                    "showInfo":"今天46家影院放映93场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1299124,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/moviemachine/6766681dc599e1964e9acbf86391207377187.jpg",
                    "version":"v3d imax",
                    "nm":"新神榜：哪吒重生",
                    "preShow":False,
                    "sc":8.7,
                    "globalReleased":True,
                    "wish":266547,
                    "star":"杨天翔,张赫,宣晓鸣",
                    "rt":"2021-02-12",
                    "showInfo":"今天59家影院放映138场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1199007,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/movie/12b0e9d3c645cda41a9c787066d52279388947.jpg",
                    "version":"",
                    "nm":"侍神令",
                    "preShow":False,
                    "sc":8.5,
                    "globalReleased":True,
                    "wish":537583,
                    "star":"陈坤,周迅,陈伟霆",
                    "rt":"2021-02-12",
                    "showInfo":"今天40家影院放映89场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1309692,
                    "haspromotionTag":False,
                    "img":"http://p1.meituan.net/w.h/moviemachine/32f40a66d85c24bee19c57d86773520e14797735.jpg",
                    "version":"",
                    "nm":"千顷澄碧的时代",
                    "preShow":False,
                    "sc":0,
                    "globalReleased":True,
                    "wish":1967,
                    "star":"李东学,宋佳伦,苏丽",
                    "rt":"2021-02-26",
                    "showInfo":"今天28家影院放映92场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":657668,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/moviemachine/6fd84eee211a0b58f1e60b7dbc1581d1181864.jpg",
                    "version":"",
                    "nm":"日暮",
                    "preShow":False,
                    "sc":7.6,
                    "globalReleased":True,
                    "wish":4702,
                    "star":"弗拉德·伊凡诺夫,苏珊娜·伍艾斯特,比约恩·弗赖贝格",
                    "rt":"2021-02-09",
                    "showInfo":"今天1家影院放映1场",
                    "showst":3,
                    "wishst":0
                },
                {
                    "id":1301774,
                    "haspromotionTag":False,
                    "img":"http://p1.meituan.net/w.h/movie/7eb748695cf975cf876f7d3524a865d71100054.jpg",
                    "version":"",
                    "nm":"错爱迷踪",
                    "preShow":False,
                    "sc":0,
                    "globalReleased":False,
                    "wish":43354,
                    "star":"尹亚森,曾晨,马翼",
                    "rt":"2021-03-05",
                    "showInfo":"2021-03-05 本周五上映",
                    "showst":4,
                    "wishst":0
                },
                {
                    "id":1218437,
                    "haspromotionTag":False,
                    "img":"http://p0.meituan.net/w.h/movie/0b754a350a4e74b16378e71c9f62877b2763706.jpg",
                    "version":"",
                    "nm":"日不落酒店",
                    "preShow":False,
                    "sc":0,
                    "globalReleased":False,
                    "wish":72840,
                    "star":"黄才伦,张慧雯,沈腾",
                    "rt":"2021-03-19",
                    "showInfo":"2021-03-19上映",
                    "showst":4,
                    "wishst":0
                }
            ]
        }
        session = DBSession()
        movie_set = session.query(Movie).order_by(Movie.showCinemaNum.desc()).order_by(Movie.sc.desc()).all()
        session.close()
        movie_list = []
        for i in movie_set:
            item = {
                "id":i.ID,
                "img":i.img,
                "version":i.version,
                "nm":i.Name,
                "sc":i.sc,
                "globalReleased":i.globalReleased,
                "wish":i.wish,
                "star":i.Star,
                "rt":i.rt,
                "showInfo":i.showInfo,
                "showst":i.showst,
                "wishst":i.wishst
            }
            movie_list.append(item)
        data = {
            "movieList": movie_list
        }
        self.JsonResponse(data)