#!/usr/bin/env python
# -*- coding: UTF-8 -*-
__author__ = 'kevin'

from core.logger import logger
from core.base_controller import BaseHandler
from core.DB import DBSession
from models.movie import Movie

result = {
        "coming":[
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"喜剧",
                "civilPubSt":0,
                "comingTitle":"3月10日 周三",
                "desc":"主演:袁春波,叶思齐,刘昌伟",
                "dir":"袁春波",
                "dur":95,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1255353,
                "img":"http://p0.meituan.net/w.h/moviemachine/e77568bfbe2a7413c9ec13fe410be72a1805925.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"有梦就飞",
                "pn":8,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615305600000,
                "pubDesc":"2021-03-10中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-10",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showNum":0,
                "showst":1,
                "snum":14,
                "star":"袁春波,叶思齐,刘昌伟",
                "ver":"2D",
                "videoId":463026,
                "videoName":"有梦就飞预告片：一部感人的励志电影",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/6f1111d15285890815046963391/v.f42906.mp4",
                "vnum":1,
                "vodPlay":False,
                "weight":1,
                "wish":200,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"喜剧,爱情",
                "civilPubSt":0,
                "comingTitle":"3月12日 周五",
                "desc":"主演:李治廷,张榕容,白客",
                "dir":"黄雷",
                "dur":106,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1212538,
                "img":"http://p1.meituan.net/w.h/movie/b7383bb5a78d70f0a1ef35b4b0f295f43266884.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"合法伴侣",
                "pn":57,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615478400000,
                "pubDesc":"2021-03-12 08:00中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-12",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showInfo":"2021-03-12 本周五上映",
                "showNum":0,
                "showst":4,
                "snum":407,
                "star":"李治廷,张榕容,白客",
                "ver":"2D",
                "videoId":463275,
                "videoName":"黄建新监制爱情喜剧《合法伴侣》曝终极预告，3月12日持证秀恩爱",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/ad32124f5285890815064900587/v.f42905.mp4",
                "vnum":5,
                "vodPlay":False,
                "weight":1,
                "wish":39314,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"剧情,爱情",
                "civilPubSt":0,
                "comingTitle":"3月12日 周五",
                "desc":"主演:海莉·露·理查森,科尔·斯普罗斯,莫伊塞斯·阿里亚斯",
                "dir":"贾斯汀·贝尔杜尼",
                "dur":117,
                "effectShowNum":0,
                "followst":0,
                "fra":"阿根廷,黎巴嫩,加拿大,印度尼西亚,美国,菲律宾,巴西,哥伦比亚,意大利,科威特,秘鲁,新加坡,乌拉圭,英国,爱尔兰,墨西哥,中国香港,印度,中国台湾,越南,韩国,爱沙尼亚,俄罗斯,匈牙利,芬兰,立陶宛,罗马尼亚,波兰,丹麦,葡萄牙,沙特阿拉伯,荷兰,德国",
                "frt":"2019-03-14,2019-03-14,2019-03-15,2019-03-15,2019-03-15,2019-03-20,2019-03-21,2019-03-21,2019-03-21,2019-03-21,2019-03-21,2019-03-21,2019-03-21,2019-03-22,2019-03-22,2019-03-22,2019-03-28,2019-03-29,2019-03-29,2019-03-29,2019-04-11,2019-04-19,2019-05-01,2019-05-02,2019-05-03,2019-05-03,2019-05-03,2019-05-10,2019-05-16,2019-05-16,2019-05-23,2019-06-13,2019-06-20",
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1219636,
                "img":"http://p0.meituan.net/w.h/movie/eaea6a447b20366f682203c6710d0ff22149802.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"五尺天涯",
                "pn":108,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615478400000,
                "pubDesc":"2021-03-12中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-12",
                "sc":0,
                "scm":"愿你我永远不舍弃爱与被爱的能力",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showInfo":"2021-03-12 本周五上映",
                "showNum":0,
                "showst":4,
                "snum":427,
                "star":"海莉·露·理查森,科尔·斯普罗斯,莫伊塞斯·阿里亚斯",
                "ver":"2D",
                "videoId":463391,
                "videoName":"电影《五尺天涯》曝心动版预告 白色情人节约定甜甜的爱情",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/f9ea84345285890815096199253/v.f42905.mp4",
                "vnum":14,
                "vodPlay":False,
                "weight":1,
                "wish":27663,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"剧情,悬疑,恐怖",
                "civilPubSt":0,
                "comingTitle":"3月12日 周五",
                "desc":"主演:郭晋东,林子煊,周纪伟",
                "dir":"江稚仑",
                "dur":85,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1310470,
                "img":"http://p0.meituan.net/w.h/moviemachine/41c353f0e60dc244140b357d5d78f17f141518.webp",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"夜守",
                "pn":22,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615478400000,
                "pubDesc":"2021-03-12中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-12",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showInfo":"2021-03-12 本周五上映",
                "showNum":0,
                "showst":4,
                "snum":72,
                "star":"郭晋东,林子煊,周纪伟",
                "ver":"2D",
                "videoId":463285,
                "videoName":"《夜守》曝“惊魂”终极预告海报，年度亚洲最佳惊悚来袭开启预售",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/0e6137ef5285890815174968004/v.f42905.mp4",
                "vnum":3,
                "vodPlay":False,
                "weight":1,
                "wish":5202,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"悬疑,惊悚",
                "civilPubSt":0,
                "comingTitle":"3月12日 周五",
                "desc":"主演:郑希怡,姚尧,许绍雄",
                "dir":"张建春",
                "dur":86,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1336148,
                "img":"http://p0.meituan.net/w.h/movie/816bb3675664dec2fec537abf635c7e02083864.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"背后的凶手",
                "pn":1,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615478400000,
                "pubDesc":"2021-03-12中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-12",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showInfo":"2021-03-12 本周五上映",
                "showNum":0,
                "showst":4,
                "snum":20,
                "star":"郑希怡,姚尧,许绍雄",
                "ver":"2D",
                "videoId":0,
                "vnum":0,
                "vodPlay":False,
                "weight":1,
                "wish":1708,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"剧情",
                "civilPubSt":0,
                "comingTitle":"3月12日 周五",
                "desc":"主演:张光北,朱宏嘉,贾旭明",
                "dir":"陈茂林",
                "dur":95,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1327499,
                "img":"http://p0.meituan.net/w.h/movie/bb3419bfe14e3f29872273381dc642292537364.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"大事",
                "pn":48,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615478400000,
                "pubDesc":"2021-03-12中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-12",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showNum":0,
                "showst":1,
                "snum":11,
                "star":"张光北,朱宏嘉,贾旭明",
                "ver":"2D",
                "videoId":390296,
                "videoName":"李翠翠祝福视频",
                "videourl":"https://vod.pipi.cn/43903a81vodtransgzp1251246104/e76ebfec5285890801960045197/v.f42906.mp4",
                "vnum":3,
                "vodPlay":False,
                "weight":1,
                "wish":102,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"喜剧,爱情",
                "civilPubSt":0,
                "comingTitle":"3月14日 周日",
                "desc":"主演:王亚楠,刘凯菲,丁宇辰",
                "dir":"李耀东",
                "dur":93,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1355723,
                "img":"http://p0.meituan.net/w.h/movie/a3841040cffab344988d7e608dacdb4b4869034.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"折腾出来的金窝窝",
                "pn":9,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615651200000,
                "pubDesc":"2021-03-14中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-14",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showNum":0,
                "showst":1,
                "snum":19,
                "star":"王亚楠,刘凯菲,丁宇辰",
                "ver":"2D",
                "videoId":462744,
                "videoName":"《折腾出来的金窝窝》预告：小姐姐回村了，会干点啥呢？",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/6f5a95d15285890814837924225/v.f42905.mp4",
                "vnum":3,
                "vodPlay":False,
                "weight":1,
                "wish":231,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"剧情,青春,悬疑",
                "civilPubSt":0,
                "comingTitle":"3月18日 周四",
                "desc":"主演:张竞达,李月,曾凡博",
                "dir":"鹤轩",
                "dur":90,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1372081,
                "img":"http://p0.meituan.net/w.h/movie/30f321cb0cc71f60e4e86c3730497a32437305.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"岁月江城",
                "pn":7,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1615996800000,
                "pubDesc":"2021-03-18中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-18",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showNum":0,
                "showst":1,
                "snum":21,
                "star":"张竞达,李月,曾凡博",
                "ver":"2D",
                "videoId":436662,
                "videoName":"预告片",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/d8f69e425285890810150096532/v.f42906.mp4",
                "vnum":1,
                "vodPlay":False,
                "weight":1,
                "wish":364,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"喜剧,奇幻",
                "civilPubSt":0,
                "comingTitle":"3月19日 周五",
                "desc":"主演:黄才伦,张慧雯,沈腾",
                "dir":"冯一平,刘峻萌,郝心悦",
                "dur":106,
                "effectShowNum":0,
                "followst":0,
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1218437,
                "img":"http://p0.meituan.net/w.h/movie/8de713ce22b34faf8d033f1aa62918dc857749.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"日不落酒店",
                "pn":77,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1616083200000,
                "pubDesc":"2021-03-19 08:00中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-19",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showInfo":"2021-03-19 下周五上映",
                "showNum":0,
                "showst":4,
                "snum":1848,
                "star":"黄才伦,张慧雯,沈腾",
                "ver":"2D",
                "videoId":463166,
                "videoName":"《日不落酒店》笑果版预告片，最后一句你笑了吗",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/23176a8d5285890815093865114/v.f42905.mp4",
                "vnum":5,
                "vodPlay":False,
                "weight":1,
                "wish":77271,
                "wishst":0
            },
            {
                "bingeWatch":0,
                "boxInfo":"喵，即将上映",
                "cat":"剧情",
                "civilPubSt":0,
                "comingTitle":"3月19日 周五",
                "desc":"主演:吴彦姝,英泽,国村隼",
                "dir":"鹏飞",
                "dur":97,
                "effectShowNum":0,
                "followst":0,
                "fra":"上海国际电影节",
                "frt":"2020-07-31",
                "globalReleased":False,
                "haspromotionTag":False,
                "headLineShow":False,
                "headLinesVO":[

                ],
                "id":1298359,
                "img":"http://p0.meituan.net/w.h/movie/be18568991776e2ec73bf7cd5fae41bf1033278.jpg",
                "isRevival":False,
                "late":False,
                "localPubSt":0,
                "mark":False,
                "mk":0,
                "movieType":0,
                "nm":"又见奈良",
                "pn":65,
                "preShow":False,
                "proScore":0,
                "proScoreNum":0,
                "pubDate":1616083200000,
                "pubDesc":"2021-03-19中国大陆上映",
                "pubShowNum":0,
                "recentShowDate":0,
                "recentShowNum":0,
                "rt":"2021-03-19",
                "sc":0,
                "scm":"",
                "scoreLabel":"暂无评分",
                "showCinemaNum":0,
                "showInfo":"2021-03-19 下周五上映",
                "showNum":0,
                "showst":4,
                "snum":84,
                "star":"吴彦姝,英泽,国村隼",
                "ver":"2D",
                "videoId":460164,
                "videoName":"电影《又见奈良》定档3月19日，开年口碑佳作温暖上映 ",
                "videourl":"https://vod.pipi.cn/fec9203cvodtransbj1251246104/879587b05285890813739540905/v.f42905.mp4",
                "vnum":4,
                "vodPlay":False,
                "weight":1,
                "wish":9843,
                "wishst":0
            }
        ],
        #"hot":Array[0],
        "movieIds":[
            1255353,
            1212538,
            1219636,
            1310470,
            1336148,
            1327499,
            1355723,
            1372081,
            1218437,
            1298359,
            1229373,
            1220837,
            1355793,
            1403466,
            1309640,
            1281464,
            1377765,
            343568,
            1280929,
            1355834,
            1302233,
            1222234,
            345006,
            1229308,
            1322057,
            1338984,
            1297996,
            1375624,
            337487,
            1285582,
            1211009,
            248836,
            1212303,
            1359285,
            1405621,
            1241385,
            1211382,
            1383416,
            1301501,
            1320283,
            1366776,
            1302287,
            1301020,
            1204322,
            1336183,
            1378057,
            1370805,
            1218188,
            1357145,
            1371295,
            1212627,
            1375543,
            1363244,
            1220824,
            1368677,
            1401786,
            1287590,
            1356063,
            1284360,
            672203,
            1301249,
            1298381,
            1300115,
            1359034
        ],
        "stid":"110189035512576"
}

class ComingListHandler(BaseHandler):
    def get(self, *args, **kwargs):
        logger.info('this is in MostExpectedHandler')
        
        self.JsonResponse(result)